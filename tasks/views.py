from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from .models import Task

def index(request):
    query = request.GET.get('search')
    if query:
        tasks = Task.objects.filter(title__icontains=query)
    else:
        tasks = Task.objects.all()

    for task in tasks:            
        if task.is_deadline_approaching():
            messages.warning(request, f"Tugas '{task.title}' hampir mencapai deadline!")

        elif task.is_overdue():
            messages.error(request, f"Tugas '{task.title}' sudah melewati deadline!")


    if request.method == 'POST':
        title = request.POST.get('task-title')
        description = request.POST.get('task-desc')
        deadline = request.POST.get('task-deadline')

        if title:
            Task.objects.create(title=title, description=description, deadline=deadline)
            return redirect('index')

    return render(request, 'tasks/index.html', {'tasks': tasks, 'search_query': query})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.completed = not task.completed
        task.save()
        return redirect('index')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('index')