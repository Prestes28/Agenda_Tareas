from django.shortcuts import render, redirect
from django.utils.timezone import now
from .form import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def listTask(request):
    if request.method =='GET':
        if request.user.is_authenticated ==True:
            form = TaskForm()
            tasks = Task.objects.filter(user=request.user)
            return render(request,'list_task.html',{'form':form, 'tasks':tasks})
        else:
            return redirect('login')
    else:
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user =request.user
            task.save()
            return redirect('listTask')
        else:
            print('Algo salio mal')
            return render(request,'list_task.html',{'form':form})
    

@login_required
def formTask(request):
    form = TaskForm(initial={'date':now().date()})
    return render (request,'task_form.html',{'form':form})

@login_required
def editTask(request,task_id):
    edit = task_id
    task = Task.objects.get(id=edit)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user =request.user
            task.save()
            return redirect('listTask')
    else:
        form = TaskForm(instance=task)


    return render(request, 'edit_task.html',{'form':form,'task':task})

@login_required
def deleteTask(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('listTask')