from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method == 'GET':
        return render(request, 'events/sign_up.html')
    elif request.method == 'POST':
        try:
            body = request.POST
            first_name = body['firstName']
            last_name = body['lastName']
            email = body['email']
            user_name = body['userName']
            password = body['password']
            
            TheUser.objects.create_user(
                username=user_name,
                password=password,
                first_name=first_name,
                last_name=last_name,
                email=email )
            return redirect('home')
        except:
            return render(request, 'events/sign_up.html', {'msg': "Username already exists"})
        
@login_required(login_url='login')
def index(request):
    events = Event.objects.filter(user_id=request.user.id)
    return render(request, 'events/index.html', {'events':events, 'user': request.user})
        
def log_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    elif request.user.is_authenticated:
        return redirect('home')
    elif request.method=='GET':
        return render(request, 'events/login.html')
    elif request.method=='POST':
        body = request.POST
        user = authenticate(username=body['userName'], password=body['password'])
        
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'events/login.html', {'msg': "Username or Password is Incorrect"})

@login_required(login_url='login')
def new_event(request):
    if request.method=='GET':
        return render(request, 'events/new.html')
    elif request.method=='POST':
        body = request.POST
        name = body['name']
        desc = body['description']
        starts = body['starts']
        ends = body['ends']
        
        current_event = Event(
            name=name,
            description=desc,
            starts_at=starts, 
            ends_at=ends, 
            user_id=request.user.id )
        
        current_event.save()
        return render(request, 'events/details.html', {'current_event': current_event})

@login_required(login_url='login')
def edit(request, id):
    current_event = Event.objects.get(id=id)
    if request.method=='GET':
        return render(request, 'events/edit.html', {'current_event': current_event})
    elif request.method=='POST':
        body = request.POST
        name = body['name']
        desc = body['description']
        starts = body['starts']
        ends = body['ends']
        
        current_event.name = name
        current_event.description = desc
        current_event.starts_at = starts
        current_event.ends_at = ends
        current_event.save()
        return render(request, 'events/details.html', {'current_event': current_event}) 
    
@login_required(login_url='login')   
def detail(request, id):
    current_event = Event.objects.get(id=id)
    return render(request, 'events/details.html', {'current_event': current_event})
    
@login_required(login_url='login')
def delete_event(request, id):
    current_event = Event.objects.get(id=id)
    current_event.delete()
    return redirect('home')

@login_required(login_url='login')        
def log_out(request):
    logout(request)
    return redirect('login')