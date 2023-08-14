from django.shortcuts import render, redirect
from crm_app.models import Task
from .forms import TaskForm

# Create your views here.

def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks':tasks}
    return render(request, 'index.html', context=context)


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html',{'form':form})

def task_detail(request,task_id):
    task = Task.objects.get(pk=task_id)
    return render(request, 'task_detail.html', {'task':task})
