from django.shortcuts import render, redirect
from django.http import request
# Create your views here.

def register(request):

    if request.method == 'GET':
        return render(request, 'register.html', locals())

    if request.method == 'POST':
        print(request.method)
        print(request.body)
        # username, email, password, confirmPassword
        username = request.POST.post('username', None)
        print(f'username = {username}')
        return redirect('/users/login/')

def login(request):
    return render(request, 'login.html', locals())