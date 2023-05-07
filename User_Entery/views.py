from django.shortcuts import render, redirect 
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Account_info
# Create your views here.
def Signup_User(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if username == "" or email == "" or password1 == "" or password2 == "":
            messages.error(request, 'please fill form correctly')
            return render(request, "signup.html")
        if password1 != password2:
            messages.warning(request, 'your confirm password does not match')
            return render(request, "signup.html")
        else:
            User_account = Account_info(username = username, email_address = email, password = password2)
            User_account.save()
            user_signup = User.objects.create_user(first_name = username, username=username ,email=email, password=password1)
            user_signup.save()
            user_login = authenticate(username=username, password=password2)
            login(request, user_login)
            messages.success(request, 'your account has been succuessfully created')
            return redirect('/home')
    else:
        return render(request, "signup.html")
    

def Login_User(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_login = authenticate(username=username, password=password)
        if user_login is not None:
            login(request, user_login)
            messages.success(request, 'your account has been loged in')
            return redirect("/home")
        if username == "" or password == "":
            messages.error(request, 'please fil form correctly')
            return render(request, "login.html")
        else:
            messages.warning(request, 'Sorry this account does not exist click to signup button and create a new account')
            return render(request, "login.html")
    else:
        return render(request, "login.html")
    
def User_logout(request):
    logout(request)
    messages.info(request, 'your account has been loged out')
    return redirect("/")

def User_account(request):
    if request.user.is_anonymous:
        return redirect("/login")
    user_query = Account_info.objects.filter(username = request.user)
    return render(request, "user_account.html", {"user_query":user_query})
    