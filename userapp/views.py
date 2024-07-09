from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'blogapp/blog_list.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'userapp/signup.html', context)

def loginpage(request):
    message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog_list')  
        else:
            message = "Invalid credentials"
    context = {'message': message}
    return render(request, 'userapp/signin.html', context)

def user_logout(request):
    logout(request)
    return redirect('blog_list')
