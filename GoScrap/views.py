from imaplib import _Authenticator
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.

def index(request):
    return render (request, 'home.html')


def home(request):
    return render (request, 'home.html')



def about(request):
    return render (request, 'about.html')


def ratecard(request):
    return render (request, 'ratecard.html')


def calculator(request):
    return render (request, 'calculator.html')


def schedule_pickup(request):
    return render (request, 'schedule.html')



def signin(request):

    if request.method == 'POST':
        email = request.POST["email"]
        password1 = request.POST["pass1"]


        user = authenticate(email = email , password= password1)

        if  user is not None:
            login(request ,user)
            return render(request , "home.html")

        else:
            return redirect('home')

    return render (request, 'signin.html')



def signup(request):

    if request.method == 'POST':
        email = request.POST["email"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        password1 = request.POST["pass1"]
        password2 = request.POST["pass2"]

        myuser = User.objects.create_user(email , password1)

        myuser.first_name = fname
        myuser.last_name = lname


        myuser.save()

        return redirect('signin')


    return render (request, 'signup.html')


