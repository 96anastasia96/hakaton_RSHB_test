from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, ("You Have Been Logged In!"))
            return redirect('/main')
    else:
        return render(request, 'login.html')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            user_login = login(request, user)
            return redirect('/main')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



@login_required
def LogoutViewCustom(request):
    logout(request)
    messages.success(request, ("You Have Been Logged Out."))
    return redirect('/main')
