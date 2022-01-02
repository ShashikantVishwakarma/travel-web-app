from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def open(request):
    return render(request,'mumbai.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'!!! invalid username or password !!!')
            return redirect('login')

    else:
        return render(request,'login.html')
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email= request.POST['email']
        password1 = request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'user taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print("email taken")
            else:
                user=User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=last_name)
                user.save()
                print('done')
        return redirect('/')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect("/")

