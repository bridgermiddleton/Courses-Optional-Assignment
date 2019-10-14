from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course

def mainpage(request):
    context = {
        "all_the_courses": Course.objects.all()
    }
    return render(request, "main_app/mainpage.html", context)

def add(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect("/")

def destroypage(request, id):
    context = {
        "course": Course.objects.get(id=id)
    }
    return render(request, "main_app/destroypage.html", context)

def destroy(request, id):
    Course.objects.get(id=id).delete()
    return redirect("/")


# Create your views here.
