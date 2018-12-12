from django.shortcuts import render,get_object_or_404
from practise.models import *
from practise.forms import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def Home(request):
    return render(request,"index.html")

@login_required
def index(request):
    if request.method == "POST":
        form = Info_form(request.POST)
        ob = Info.objects.all()
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            print(email)
            return render(request,"index.html")
        else:
            print(form.errors)
    else:
        form = Info_form()
    return render(request,"index0.html",{'form':form})

@login_required
def feedback_web(request):
    link = "http://127.0.0.1:8000/crontab/feedback/"
    if request.method == "POST":
        form = Feed_Form(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"timer.html",{'link':link})

        else:
            print(form.errors)
    else:
        form = Feed_Form()
    return render(request,"feedback.html",{'form':form,'link':link})
