from django.shortcuts import render, redirect
from django.http import request
from django import http
# Create your views here.

def register(request):

    if request.method == 'GET':
        return render(request, 'register.html', locals())

    if request.method == 'POST':
        print(request.method)
        print(request.body)
        # username, email, password, confirmPassword
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        email = request.POST.get('email')
        if not all([username, email, password, confirmPassword]):
            # 進行進一步的判斷, 沒有異常才存入數據庫
            print('有數據缺少')
            return http.HttpResponseForbidden('請確實填寫各項表單數據')
        else:
            # 返回缺少數據給使用者
            print('數據正常')
        return redirect('/users/login/')

def login(request):
    return render(request, 'login.html', locals())