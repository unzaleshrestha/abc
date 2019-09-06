from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
    return render(request,'index.html')

'''def about(request):
    return HttpResponse("<h1>hello world </h1>")'''

'''def about(request):
    context = {
        'c': 10,
        'a': [23, 354, 54, 5, 45]
    }
    return render(request,'about/about.html',context)'''

def about(request):
    return render(request,'about/about.html')

def signup(request):
    return render(request,'signup.html')

def signin(request):
    return render(request,'login.html')