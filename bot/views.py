from django.shortcuts import render
from django.http import HttpResponse
from bot import Templates

# Create your views here.
def index(request):
    return render(request,'bot.html')