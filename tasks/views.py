from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.conf import settings
from .models import Task
import json
import requests
import os
from groq import Groq

@login_required(login_url='login')
def index(request):
    tasks = Task.objects.filter(owner=request.user)

    query = request.GET.get('search')
    if query:
        tasks = Task.objects.filter(title__icontains=query, owner=request.user)
    else:
        tasks = Task.objects.filter(owner=request.user)

    for task in tasks:            
        if task.is_deadline_approaching():
            messages.warning(request, f"Tugas '{task.title}' hampir mencapai deadline!")

        elif task.is_overdue():
            messages.error(request, f"Tugas '{task.title}' sudah melewati deadline!")


    if request.method == "POST":
        title = request.POST.get('task-title')
        description = request.POST.get('task-desc')
        deadline = request.POST.get('task-deadline')
        new_task = Task(
            title=title, 
            description=description, 
            deadline=deadline,
            owner=request.user
        )
        new_task.save()
        return redirect('index')

    return render(request, 'tasks/index.html', {'tasks': tasks, 'search_query': query})

@login_required(login_url='login')
def ask_ai(request):
    tasks = Task.objects.filter(owner=request.user)
    if request.method == 'POST':
        question = request.POST.get('question')
        if question:
            try:
                # Inisialisasi client Groq
                client = Groq(
                    api_key=settings.GROQ_API_KEY
                )
                # Kirim permintaan ke Groq
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": question,
                        }
                    ],
                    model="llama-3.3-70b-versatile",
                )
                # Ambil jawaban dari API
                answer = chat_completion.choices[0].message.content

                if answer:
                    return render(request, "tasks/result.html", {'answer': answer, 'tasks': tasks})
                else:
                    return render(request, "tasks/result.html", {'answer': "Terjadi kesalahan!"})
            
            except Exception as e:
                # Tampilkan error jika terjadi masalah
                return HttpResponse(f"Terjadi kesalahan: {e}")

    # Jika bukan POST atau tidak ada pertanyaan, tampilkan form
    return render(request, "tasks/ask.html", {"tasks": tasks})


def user_logout(request):
    logout(request)
    return redirect('login')

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Akun untuk {username} berhasil dibuat! Silakan login.')
            return redirect('login')
        else:
            messages.error(request, "Gagal membuat akun. Coba lagi.")
    else:
        form = UserCreationForm()

    return render(request, 'tasks/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, "Username atau password salah.")
    else:
        form = AuthenticationForm()

    return render(request, 'tasks/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Akun berhasil dibuat. Silakan login.")
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'tasks/register.html', {'form': form})

@login_required(login_url='login')
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.completed = not task.completed
        task.save()
        return redirect('index')

@login_required(login_url='login')
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('index')