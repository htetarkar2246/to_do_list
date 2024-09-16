from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .models import Todo
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
  if request.method == 'POST':
    task_todo = request.POST.get("task")
    new_todo = Todo(user = request.user, task = task_todo)
    new_todo.save()
    
  all_todos = Todo.objects.filter(user = request.user)
  context = {
    'todos': all_todos
  }
  return render(request, 'to_do_app/todo.html', context)

def register(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    if len(password) < 3:
      messages.error(request, 'Password must be at least 3 chracters')
      return redirect('/register')
      
    get_all_users_by_username = User.objects.filter(username=username)
    if get_all_users_by_username:
      messages.error(request, 'Error, username already exists, Use another.')
      return redirect('/register')
    
    new_user = User.objects.create_user(username=username, password=password)
    new_user.save()
    
    messages.success(request, 'User successfully created, login now.')
    return redirect('/login')
    
  return render(request, 'to_do_app/register.html', {})

def logout(request):
    auth_logout(request)
    return redirect('/login')
  
def login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    validate_user = authenticate(username=username, password=password)
    if validate_user is not None:
      auth_login(request, validate_user)
      return redirect('/')
    else:
      messages.error(request, 'Error, wrong user details or user does not exist.')
      return redirect('/login')
    
  return render(request, 'to_do_app/login.html', {})

@login_required
def deleteTask(request, name):
  get_todo = Todo.objects.filter(user=request.user, task=name)
  get_todo.delete()
  return redirect('home-page')

@login_required
def update(request, name):
  todos = Todo.objects.filter(user=request.user, task=name)
  for todo in todos:
    todo.status = not todo.status
    todo.save()
  return redirect('home-page')
  