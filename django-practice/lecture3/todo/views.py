from django.shortcuts import render

tasks = ["get milk", "get vegetables", "get flour"]

# Create your views here.
def index(request):
    return render(request, "todo/index.html", {
        "tasks": tasks
    })