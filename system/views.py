from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from system import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from system.forms import TaskForm, CommentForm, ProjectForm

class ProjectListView(ListView):
    
    model = models.Project
    context_object_name = 'projects'
    template_name = 'project_list.html'

class ProjectDetailView(DeleteView):
    
    model = models.Project
    context_object_name = 'project'
    template_name = 'project_detail.html'
    
class ProjectCreateView(CreateView):
    
    model = models.Task
    template_name =  "project_form.html"
    form_class = ProjectForm
    success_url = reverse_lazy("system:project-create")

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
    
""" def form_valid(self, form):
        form.instance.task_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('task_detail', kwargs={'pk': self.kwargs['pk']})"""
# Create your views here.
