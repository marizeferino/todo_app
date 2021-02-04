from django.shortcuts import redirect, render

from tasks.forms import TaskForm
from .models import Task
from .forms import TaskForm

# Create your views here.

def index_view (request, *args, **kwargs):
    tasks = Task.objects.all()
    form = TaskForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/index.html', context)


def update_task_view(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task) 
        if form.is_valid():
            form.save()
            return redirect('/')   

    context = {'form':form}
    return render(request, 'tasks/update_task.html', context)


def delete_task_view(request,pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {'task':task}
    return render(request, 'tasks/delete.html', context)