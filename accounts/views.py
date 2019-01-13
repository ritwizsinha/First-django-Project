from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
def login(request):
    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username , password = password)
        if user is not None:
            auth.login(request,user)
            messages.success(request, 'LOGGED IN SUCCESSFULLY')
            return redirect('dashboard')
        else :
            messages.error(request, 'something is wrong')
            return redirect('login')

    else:
        return render(request,'accounts/login.html')

def logout(request):
    return render(request, 'pages/index.html')


def register(request):
    if request.method == 'POST': 
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'USERNAME ALREADY TAKEN')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'EMAIL ALREADY TAKEN')
                    return redirect('register')

                else:
                    user = User.objects.create_user(username = username, email=email, last_name = last_name, first_name= first_name, password = password )
                    user.save()
                    messages.success(request, 'Registered')
                    return redirect('login') 
               
        else:
            messages.error(request,'Passwords not same')
            return redirect('register')
        

    else: 
        return render(request, 'accounts/register.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')