from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='/todolist/login/')

def show_todolist(request):
    # context = {

        
    # }
    return render(request, "todolist.html")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # return redirect('show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
        return redirect('show_todolist')
    context = {}
    return render(request, 'login.html', context)
    

def logout_user(request):
    logout(request)
    return redirect('login')

