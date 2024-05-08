from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from book.models import Book, Category

# Create your views here.

def home(request):
    categories = Category.objects.filter(active=True)
    books = Book.objects.all().order_by('-created')

    context = {
        'books':books,
        'categories':categories
    }

    return render(request, 'index.html', context)


def loginView(request):
    user = request.user

    if request.method == 'POST':
        password = request.POST.get('password')
        username = request.POST.get('username')
        user = authenticate(
            username=username,
            password=password 
        )
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')

    context = {
        'user':user,
        
    }
    return render(request, 'login.html', context)


def logoutView(request):
    logout(request)
    return redirect('home')


def registerView(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        
        if password == password2:
            user = User.objects.create_user(
                username=username,
                email = email,
                password= password
            )
            user.save()
            return redirect('login')
        else:
            messages.error(request, "Attention !! Les deux champs de password doivent etre identique")
            return redirect('register')

    return render(request, 'register.html')