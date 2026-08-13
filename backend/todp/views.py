from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from todp import models
from todp.models import TODOO
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

def signup(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        emaiid = request.POST.get('email')
        pwd = request.POST.get('pwd')
        
        # Check if username already exists
        if User.objects.filter(username=fnm).exists():
            return render(request, 'signup.html', {'error': 'Username already taken!'})
            
        my_user = User.objects.create_user(username=fnm, email=emaiid, password=pwd)
        my_user.save()
        return redirect('/index/')
        
    return render(request, 'signup.html')


def user_login(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        
        user = authenticate(request, username=fnm, password=pwd)
        
        if user is not None:
            auth_login(request, user)
            return redirect('/todo/')
        else:
            return render(request, 'index.html', {'error': 'Invalid credentials'})
            
    return render(request, 'index.html') 


@login_required(login_url='/index/')
def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            obj = models.TODOO(title=title, user=request.user)
            obj.save()
        return redirect('/todo/')
    
    res = models.TODOO.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html', {'res': res})


@login_required(login_url='/index/')
@require_http_methods(["GET", "POST"])
def edit_todo(request, srno):
    try:
        todo = TODOO.objects.get(srno=srno, user=request.user)
    except TODOO.DoesNotExist:
        return redirect('/todo/')
    
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            todo.title = title
            todo.save()
        return redirect('/todo/')
    
    return render(request, 'edit_todo.html', {'todo': todo})


@login_required(login_url='/index/')
@require_http_methods(["GET", "POST"])
def delete_todo(request, srno):
    try:
        todo = TODOO.objects.get(srno=srno, user=request.user)
        todo.delete()
    except TODOO.DoesNotExist:
        pass
    
    return redirect('/todo/')


def user_logout(request):
    logout(request)
    return redirect('/index/')
