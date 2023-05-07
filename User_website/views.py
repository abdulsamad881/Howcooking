from django.shortcuts import render, redirect
from .models import Add_recipe
from .models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    if request.user.is_anonymous:
        recipes = Add_recipe.objects.all()
        return render(request, "index.html", {"recipes":recipes})
    else:
        return redirect("/home")

def Home_page(request):
    if request.user.is_anonymous:
        return redirect("/login")
    recipes = Add_recipe.objects.all()
    
    return render(request, "home.html", {"recipes":recipes})

def add_Recipe(request):
    if request.user.is_anonymous:
        return redirect("/login")
    elif request.method == "POST":
        user = request.user
        thumbnail = request.FILES.get("thumbnail")
        title = request.POST.get("title")
        steps_to_cook = request.POST.get("steps to cook")
        description = request.POST.get("description")
        if user == "" or thumbnail == "" or title == "" or steps_to_cook == "" or description == "":
            messages.warning(request, 'please fill the form correctly')
            return render(request, "add_recipe.html")
        post_recipe = Add_recipe(user = request.user, thumbnail = thumbnail, title = title ,steps_to_cook = steps_to_cook, description = description, slug = title)
        post_recipe.save()
        messages.success(request, 'your recipe succuessfully added')
    return render(request, "add_recipe.html")

def User_contact(request):
    if request.user.is_anonymous:
        return redirect("/login")
    elif request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        query_or_problem = request.POST.get("query_or_problem")
        if name == "" or email == "" or subject == "" or query_or_problem == "":
            messages.warning(request, 'please fill form correctly')
            return render(request, "contact.html")
        contact = Contact(name = name, email = email, subject = subject, query_or_problem = query_or_problem)
        contact.save()
        messages.success(request, 'your query or problem succuessfully submit')
    return render(request, "contact.html")

def cooking(request, recipe):
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        steps = Add_recipe.objects.get(slug = recipe).steps_to_cook.split(".")
        description = Add_recipe.objects.get(slug = recipe).description
        return render(request, "cooking.html", {"steps":steps, "description":description})