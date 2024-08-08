from django.shortcuts import render, reverse
from system import models
from django.views.generic import ListView, DetailView, CreateView


class TaskListView(ListView):
    
    model =models.Task
    context_object_name = "tasks"
    template_name = "task_list.html"
    
class TaskDetailView(DetailView):
    
    model =models.Task
    context_object_name = "task"
    template_name = "task_detail.html"
    
class TaskCreateView(CreateView):
    model = models.Task
    template_name =  "task_form.html"
    #form_class = TaskForm
    success_url = "task-list"
    
# Create your views here.
