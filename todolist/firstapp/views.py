
from django.shortcuts import render, redirect,get_object_or_404
from .models import Task

def index(request):
    if request.method == 'POST':
        title = request.POST.get('task_title')
        description = request.POST.get('task_description')
        if title:
            Task.objects.create(title=title, description=description)
        return redirect('index')  # Prevent resubmission on refresh

    tasks = Task.objects.order_by('completed', '-created_at')
    return render(request, 'index.html', {'tasks': tasks})
                



def complete_task(request, task_id):
    tasks = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        tasks.completed = not tasks.completed
        tasks.save()
    return redirect('index')

def delete_task(request,task_id):
        tasks = get_object_or_404(Task, id = task_id)
        if request.method == 'POST':
            tasks.delete()
        return redirect('index')

# def update_task(request, task_id):
#     tasks = get_object_or_404(Task, id = task_id)
#     if request.method == "PATCH":
#         tasks.update()
#     return redirect('index')

def edit_task(request, task_id):
    tasks = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        tasks.title = request.POST.get('title')
        tasks.description = request.POST.get('description')
        tasks.save()
        return redirect('index')
    return redirect('index')
     








