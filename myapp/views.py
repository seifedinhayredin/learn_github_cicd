from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, welcome to the Airline application!")
def login(request):
    return HttpResponse("This is the login page.")
def about(request):
    return render(request, "myapp/about.html")
def register(request):
    return render(request, "myapp/register.html")