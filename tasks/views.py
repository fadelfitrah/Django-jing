from django.shortcuts import render, redirect
from .models import Task

def index(request):
    query = request.GET.get('search')
    if query :
        tasks = Task.objects.filter(title__icontains=query)
    else :
        tasks = Task.objects.all()
    
    # Cek jika request adalah POST untuk menambah tugas baru
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:  # Pastikan title tidak kosong
            Task.objects.create(title=title)
            return redirect('index')  # Redirect ke halaman index

    return render(request, 'tasks/index.html', {'tasks': tasks, 'search_query': query})

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('index')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')
