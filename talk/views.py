from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User,auth

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        data = auth.authenticate(username=username,password=password)
        if data is not None:
            auth.login(request,data)
            return redirect('chat_view')
        return redirect('login')
    else:
        return render(request,'blank.html')
