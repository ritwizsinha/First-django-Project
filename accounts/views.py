from django.shortcuts import render,redirect

def login(request):
    if request.method == 'POST': 
        print('SUBMITTED REG')
        return redirect('login')
    return render(request,'accounts/login.html')

def logout(request):
    return render(request, 'pages/index.html')


def register(request):
    if request.method == 'POST': 
        print('Submitted reg')
        return redirect('register')

    return render(request, 'accounts/register.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')