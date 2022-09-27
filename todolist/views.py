from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from todolist.models import Task
from datetime import datetime 
import itertools


# Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    # id = request.user.id
    # user = request.user
    context = {
        'username': request.user.username,
        'task_list': Task.objects.filter(user=request.user),
    }
    return render(request, "todolist.html", context)


def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login_user')
    
    context = {'form':form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('todolist:login_user')

@login_required(login_url="/todolist/login")
def create_task(request):
    if request.method == "POST":
        judul = request.POST.get("title")
        deskripsi = request.POST.get("description")
        add_todolist = Task(user=request.user, title=judul, description=deskripsi, date=datetime.now())
        add_todolist.save()
        return redirect("todolist:show_todolist")
    return render(request, 'create_task.html')

def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect("todolist:show_todolist")
    
def change_status(request, id):
    task = Task.objects.get(id=id)
    task.is_finished = not task.is_finished
    task.save()
    return redirect("todolist:show_todolist")