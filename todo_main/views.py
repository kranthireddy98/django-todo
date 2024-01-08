from django.http import HttpResponse
from django.shortcuts import render

from todo.models import Task

def home(request):
    activeTasks = Task.objects.filter(is_completed=False).order_by('-id')
    context = {
        "tasks" :activeTasks
    }
    return render(request,'home.html',context)