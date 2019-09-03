from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from bot import templates
from django.contrib.auth.forms import UserCreationForm
# from .forms import NameForm

# Create your views here.
def home(request):
    return render(request,'bot.html')

def register(request):
    if request.method == 'POST':
        #  creates instance and populates it with data from the request
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/welcome puta")
        # if any other response return blank form

        else:
            form = NameForm()

        return render(request,'register.html',{'form':form})