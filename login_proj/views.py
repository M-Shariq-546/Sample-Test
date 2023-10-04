from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("welcome/")
        else:
            return render(request, 'index.html', {'error_message': "invalid"})
    return render(request , "index.html")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('index.html')  # Replace 'login' with the URL name of your login page
        else:
            messages.error(request, 'Sorry')

    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})
