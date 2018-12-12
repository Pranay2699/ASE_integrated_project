from django.shortcuts import render,get_object_or_404,redirect
from .models import industry
from . import forms
from final_app.models import Review
# Create your views here.

def index(request):
    queryset = industry.objects.all()

    queryset2 = industry.objects.filter(category__contains="Manufacturing")

    queryset3 = industry.objects.filter(category__contains="Automobile")

    queryset4 = industry.objects.filter(category__contains="Assembling")

    queryset5 = industry.objects.filter(category__contains="IT Companies")


    context = {
        "objects" : queryset,
        "objects2" : queryset2,
        "objects3":queryset3,
        "objects4":queryset4,
        "objects5":queryset5,

    }
    return render(request,'searchBarApp/index.html',context)

def result(request,name=None):

    queryset = industry.objects.all()

    queryset2 = industry.objects.filter(category__contains="Manufacturing")

    queryset3 = industry.objects.filter(category__contains="Automobile")

    queryset4 = industry.objects.filter(category__contains="Assembling")

    queryset5 = industry.objects.filter(category__contains="IT Companies")


    query = request.POST['query']
    temp = query.upper()
    k=404
    for object in queryset:
        if object.id_name.upper() == temp:
            k = object.id

    test = industry.objects.get(pk=k)
    related = industry.objects.filter(category=test.category)
    no_related = industry.objects.filter(category=test.category).count()
    rel_location = industry.objects.filter(category = test.location)
    no_rel_location = industry.objects.filter(category = test.location).count()



    if(k==404):
        k = None
        context = {
            "key" : False,
            "objects" : queryset,
            "objects2" : queryset2,
            "objects3":queryset3,
            "objects4":queryset4,
            "objects5":queryset5,
        }
    else:
        context = {
            "instance" : get_object_or_404(industry, id = k),
            "objects" : queryset,
            "objects2" : queryset2,
            "objects3":queryset3,
            "objects4":queryset4,
            "objects5":queryset5,
            "reviews": Review.objects.filter(industry_id = k),
            "no_r": Review.objects.filter(industry_id = k).count(),
            "key" : True,
            "related" : related,
            "no_related" : no_related,
            "rel_location" : rel_location,
            "no_rel_location" : no_rel_location,

        }
    return render(request,'searchBarApp/result.html',context)

def AddReview(request):
    if request.method == 'POST':
        ind= request.POST['ind']
        ind = industry.objects.filter(id_name=ind).first()
        # Review.objects.create(industry_id=ind,user_id=request.user,user_name=username,comment=comment,rating=rating)
        newReview = Review()
        newReview.industry_id = ind
        newReview.user_id = request.user
        newReview.user_name = request.user.username
        newReview.comment = request.POST['comment']
        newReview.rating = int(request.POST['rating'])
        newReview.save()
        null = True
        return redirect('index')

    else:
        return redirect('index')

def Assembling(request,name=None):

    queryset = industry.objects.all()

    queryset2 = industry.objects.filter(category__contains="Manufacturing")

    queryset3 = industry.objects.filter(category__contains="Automobile")

    queryset4 = industry.objects.filter(category__contains="Assembling")

    queryset5 = industry.objects.filter(category__contains="IT Companies")


    context = {
        "objects" : queryset,
        "objects2" : queryset2,
        "objects3":queryset3,
        "objects4":queryset4,
        "objects5":queryset5,

    }
    return render(request,'searchBarApp/Assembling.html',context)

def Automobiles(request,name=None):

    queryset = industry.objects.all()

    queryset2 = industry.objects.filter(category__contains="Manufacturing")

    queryset3 = industry.objects.filter(category__contains="Automobile")

    queryset4 = industry.objects.filter(category__contains="Assembling")

    queryset5 = industry.objects.filter(category__contains="IT Companies")


    context = {
        "objects" : queryset,
        "objects2" : queryset2,
        "objects3":queryset3,
        "objects4":queryset4,
        "objects5":queryset5,

    }
    return render(request,'searchBarApp/Automobiles.html',context)

def Manufacturing(request,name=None):

    queryset = industry.objects.all()

    queryset2 = industry.objects.filter(category__contains="Manufacturing")

    queryset3 = industry.objects.filter(category__contains="Automobile")

    queryset4 = industry.objects.filter(category__contains="Assembling")

    queryset5 = industry.objects.filter(category__contains="IT Companies")


    context = {
        "objects" : queryset,
        "objects2" : queryset2,
        "objects3":queryset3,
        "objects4":queryset4,
        "objects5":queryset5,


    }
    return render(request,'searchBarApp/Manufacturing.html',context)

def IT_Companies(request,name=None):

    queryset = industry.objects.all()

    queryset2 = industry.objects.filter(category__contains="Manufacturing")

    queryset3 = industry.objects.filter(category__contains="Automobile")

    queryset4 = industry.objects.filter(category__contains="Assembling")

    queryset5 = industry.objects.filter(category__contains="IT Companies")


    context = {
        "objects" : queryset,
        "objects2" : queryset2,
        "objects3":queryset3,
        "objects4":queryset4,
        "objects5":queryset5,

    }
    return render(request,'searchBarApp/IT_Companies.html',context)

def base(request):

    queryset = industry.objects.all()

    queryset2 = industry.objects.filter(category__contains="Manufacturing")

    queryset3 = industry.objects.filter(category__contains="Automobile")

    queryset4 = industry.objects.filter(category__contains="Assembling")

    queryset5 = industry.objects.filter(category__contains="IT Companies")



    context = {
    "objects" : queryset,
    "objects2" : queryset2,
    "objects3":queryset3,
    "objects4":queryset4,
    "objects5":queryset5,

    }

    return render(request,'searchBarApp/base.html',context)

def contact(request):
    queryset = industry.objects.all()

    queryset2 = industry.objects.filter(category__contains="Manufacturing")

    queryset3 = industry.objects.filter(category__contains="Automobile")

    queryset4 = industry.objects.filter(category__contains="Assembling")

    queryset5 = industry.objects.filter(category__contains="IT Companies")


    context = {
        "objects" : queryset,
        "objects2" : queryset2,
        "objects3":queryset3,
        "objects4":queryset4,
        "objects5":queryset5,

    }
    return render(request,'searchBarApp/contact.html',context)

def blog(request):
    queryset = industry.objects.all()

    queryset2 = industry.objects.filter(category__contains="Manufacturing")

    queryset3 = industry.objects.filter(category__contains="Automobile")

    queryset4 = industry.objects.filter(category__contains="Assembling")

    queryset5 = industry.objects.filter(category__contains="IT Companies")


    context = {
        "objects" : queryset,
        "objects2" : queryset2,
        "objects3":queryset3,
        "objects4":queryset4,
        "objects5":queryset5,

    }
    return render(request,'searchBarApp/blog.html',context)

def faq(request):
    queryset = industry.objects.all()

    queryset2 = industry.objects.filter(category__contains="Manufacturing")

    queryset3 = industry.objects.filter(category__contains="Automobile")

    queryset4 = industry.objects.filter(category__contains="Assembling")

    queryset5 = industry.objects.filter(category__contains="IT Companies")


    context = {
        "objects" : queryset,
        "objects2" : queryset2,
        "objects3":queryset3,
        "objects4":queryset4,
        "objects5":queryset5,

    }
    return render(request,'searchBarApp/faq.html',context)

def about(request):
    queryset = industry.objects.all()

    queryset2 = industry.objects.filter(category__contains="Manufacturing")

    queryset3 = industry.objects.filter(category__contains="Automobile")

    queryset4 = industry.objects.filter(category__contains="Assembling")

    queryset5 = industry.objects.filter(category__contains="IT Companies")


    context = {
        "objects" : queryset,
        "objects2" : queryset2,
        "objects3":queryset3,
        "objects4":queryset4,
        "objects5":queryset5,

    }
    return render(request,'searchBarApp/about.html',context)

def services(request):
    queryset = industry.objects.all()

    queryset2 = industry.objects.filter(category__contains="Manufacturing")

    queryset3 = industry.objects.filter(category__contains="Automobile")

    queryset4 = industry.objects.filter(category__contains="Assembling")

    queryset5 = industry.objects.filter(category__contains="IT Companies")


    context = {
        "objects" : queryset,
        "objects2" : queryset2,
        "objects3":queryset3,
        "objects4":queryset4,
        "objects5":queryset5,

    }
    return render(request,'searchBarApp/services.html',context)

def read(request):
    queryset = industry.objects.all()

    queryset2 = industry.objects.filter(category__contains="Manufacturing")

    queryset3 = industry.objects.filter(category__contains="Automobile")

    queryset4 = industry.objects.filter(category__contains="Assembling")

    queryset5 = industry.objects.filter(category__contains="IT Companies")


    context = {
        "objects" : queryset,
        "objects2" : queryset2,
        "objects3":queryset3,
        "objects4":queryset4,
        "objects5":queryset5,

    }
    return render(request,'searchBarApp/read.html',context)
