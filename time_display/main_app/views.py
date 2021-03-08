from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
# Create your views here.
def index(request):
    context = {
        "time": strftime("%A, %B %Y", gmtime()),
        "hour": strftime("%I:%M %p", gmtime())
    }
    print(context)
    return render(request, "index.html", context)

def form(request):
    return render(request, "form.html")

def create(request):
    print(request.POST)
    # print(request.POST['name'])
    # print(request.POST['name'])
    # print(request.POST['fav_letter'])
    return redirect("/form")