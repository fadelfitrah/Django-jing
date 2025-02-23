from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def index(request):
    query = request.GET.get('search')
    if query:
        tasks = Task.objects.filter(title__icontains=query)
    else:
        tasks = Task.objects.all()

    if request.method == 'POST':
        title = request.POST.get('task-title')
        description = request.POST.get('task-desc')
        if title:
            Task.objects.create(title=title, description=description)
            return redirect('index')

    return render(request, 'tasks/index.html', {'tasks': tasks, 'search_query': query})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.completed = not task.completed  # Toggle status
        task.save()
        return redirect('index')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('index')