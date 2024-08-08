from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from system import models
from django.views.generic import ListView, DetailView, CreateView
from system.forms import TaskForm, CommentForm


class TaskListView(ListView):
    
    model = models.Task
    context_object_name = "tasks"
    template_name = "task_list.html"
    
class TaskDetailView(DetailView):
    
    model =models.Task
    context_object_name = "task"
    template_name = "task_detail.html"
    
class TaskCreateView(CreateView):
    model = models.Task
    template_name =  "task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("system:task-create")
    
class CommentCreateView(CreateView):
    model = models.Comment
    template_name = "comment.html"
    form_class = CommentForm
    success_url = reverse_lazy("system:comments")
# Create your views here.
