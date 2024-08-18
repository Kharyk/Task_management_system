from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from system import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from system.forms import TaskForm, CommentForm, ProjectForm, TaskUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from system.mixins import UserIsOwnerMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

def homepage(request):
    return render(request, 'home.html')

def learn_more(request):
    return render(request, 'learn_more.html')

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
    
    model = models.Task
    context_object_name = "task"
    template_name = "task_detail.html"
    
class TaskCreateView(LoginRequiredMixin, CreateView):
    
    model = models.Task
    template_name =  "task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("system:task-create")
    
    def form_valid(self, form):
        
        form.instance.creator = self.request.user
        return super().form_valid(form)
    
class TaskUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    
    model = models.Task
    template_name = "task_update.html"
    form_class = TaskUpdateForm
    success_url = reverse_lazy("system:task-list")
    
    
class TaskDeleteView( LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    
    model = models.Task
    template_name = "task_delete.html"
    success_url = reverse_lazy("system:task-list")
    
    
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
        
"""class TaskCompleteView(LoginRequiredMixin, UserIsOwnerMixin, View):
    
    def post(self, request, *args, **kwargs):
        task = self.get_object()
        task.status = "done"
        task.save()
        return HttpResponseRedirect(reverse_lazy("system:task-list"))
    
    def get_object(self, **kwargs):
        task_id = self.kwargs.get("pk")
        return get_object_or_404(models.Task, pk=task_id)"""
# Create your views here.
