from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from todp import models
from todp.models import TODOO
from django.contrib.auth import authenticate, login as auth_login, logout

def signup(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        emaiid = request.POST.get('email')
        pwd = request.POST.get('pwd')
        
        # Check if username already exists
        if User.objects.filter(username=fnm).exists():
            # Pass an error message to your template if you want
            return render(request, 'signup.html', {'error': 'Username already taken!'})
            
        my_user = User.objects.create_user(username=fnm, email=emaiid, password=pwd)
        my_user.save()
        return redirect('/login')
        
    return render(request, 'signup.html')


def user_login(request):  # Renamed to avoid collision with auth_login
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        
        user = authenticate(request, username=fnm, password=pwd)
        
        if user is not None:
            auth_login(request, user)  # Using the aliased auth_login function
            return redirect('/todo')
        else:
            # Ideally, pass an error message to the template here
            return redirect('/login')
            
    return render(request, 'index.html') 


def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:  # Make sure title isn't empty
            obj = models.TODOO(title=title, user=request.user)
            obj.save()
            res=models.TODOO.objects.filter(user=request.user).order_by('-date')
        return redirect('/todo',{'res':res})  # Redirect to avoid duplicate form submissions on refresh
    res=models.TODOO.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html',{'res':res})


def edit_todo(request, srno):
    obj = TODOO.objects.get(srno=srno)

    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            obj.title = title
            obj.save()
        return redirect('/todo')

    res = TODOO.objects.filter(user=request.user).order_by('-date')
    return render(request, 'edit_todo.html', {'obj': obj, 'res': res})


def delete_todo(request, srno):
    todo_item = TODOO.objects.get(srno=srno)
    todo_item.delete()
    return redirect('/todo')


def user_logout(request):
    logout(request)
    return redirect('/login')