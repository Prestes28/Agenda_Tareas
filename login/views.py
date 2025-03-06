from django.shortcuts import render, redirect
from .form import RegisterUserForm
from django.contrib.auth import login

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterUserForm()
    return render(request, 'registration/register.html',{'form':form})