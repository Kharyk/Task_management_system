from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from system import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.views import LogoutView
from system.forms import TaskForm, CommentForm, ProjectForm, TaskUpdateForm, ProjectUpdateForm, CommentUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from system.mixins import UserIsOwnerMixin, UserIsOwnerProjectMixin, UserIsOwnerCommentMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, SignupForm
from .models import Project, Task
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils.decorators import method_decorator

class SearchResultsView(View):
    @method_decorator(login_required)
    def get(self, request):
        query = request.GET.get('q')
        if query:
            tasks = Task.objects.filter(
                Q(title__icontains=query) | 
                Q(description__icontains=query) | 
                Q(creator__username__icontains=query)
            ).filter(Q(creator=request.user) | Q(project__members=request.user))
            projects = Project.objects.filter(
                Q(title__icontains=query) | 
                Q(description__icontains=query) | 
                Q(creator_of_project__username__icontains=query)
            ).filter(Q(creator_of_project=request.user) | Q(members=request.user))
        else:
            tasks = Task.objects.none()
            projects = Project.objects.none()
        return render(request, 'search_results.html', {'tasks': tasks, 'projects': projects, 'query': query})

class LoginView(View):
    template_name = 'login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('system:task-list')  
            else:
                form.add_error(None, 'Invalid username or password')
        return render(request, self.template_name, {'form': form})


class CustomLogoutView(LogoutView):

    def get(self, request):
        return super().get(request)

class SignupView(View):
    template_name = 'signup.html'
    form_class = SignupForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('system:task-list')  
        return render(request, self.template_name, {'form': form})

class HomepageView(TemplateView):
    template_name = 'home.html'

class LearnMoreView(TemplateView):
    template_name = 'learn_more.html'

class ContactView(LoginRequiredMixin, TemplateView):
    template_name = 'contact.html'

class ProjectListView(LoginRequiredMixin, ListView):
    
    model = models.Project
    template_name = 'project_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['my_projects'] = models.Project.objects.filter(creator_of_project=user)
        context['member_projects'] = models.Project.objects.filter(members=user).exclude(creator_of_project=user)
        return context

class ProjectDetailView(LoginRequiredMixin, DetailView):
    
    model = models.Project
    context_object_name = 'project'
    template_name = 'project_detail.html'
    
class ProjectCreateView(LoginRequiredMixin, CreateView):
    
    model = Project
    template_name =  "project_form.html"
    form_class = ProjectForm
    success_url = reverse_lazy("system:project-list")
    
    def form_valid(self, form):
        form.instance.creator_of_project = self.request.user
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.creator_of_project = request.user
            project.save()
            form.save_m2m()  
            return redirect(self.success_url)  
        else:
            return render(request, self.template_name, {'form': form})

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
class ProjectUpdateView(LoginRequiredMixin,UserIsOwnerProjectMixin, UpdateView):
    
    model = models.Project
    template_name = "project_update.html"
    form_class = ProjectUpdateForm
    success_url = reverse_lazy("system:project-list")
    
class ProjectDeleteView( LoginRequiredMixin, UserIsOwnerProjectMixin, DeleteView):
    
    model = models.Project
    template_name = "project_delete.html"
    success_url = reverse_lazy("system:project-list")


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "task_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        creator = self.request.user
        if creator:
            queryset = queryset.filter(creator__username=creator)
            
        if self.request.GET.get('filter_by_deadline'):
            queryset = queryset.filter(due_date__gte=datetime.today()).order_by('due_date')
        
        if self.request.GET.get('filter_overdue'):
            queryset = queryset.filter(due_date__lte=datetime.today())
        
        return queryset


class TaskDetailView(LoginRequiredMixin, DetailView):
    
    model = models.Task
    context_object_name = "task"
    template_name = "task_detail.html"
    
class TaskCreateView(LoginRequiredMixin, CreateView):
    
    model = models.Task
    template_name =  "task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("system:task-list")
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        
        form.instance.creator = self.request.user
        return super().form_valid(form)
    
    
    
class TaskUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    
    model = models.Task
    template_name = "task_update.html"
    form_class = TaskUpdateForm
    
    def get_success_url(self):
        return reverse_lazy("system:task-detail", args=[self.object.id])
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    
class TaskDeleteView( LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    
    model = models.Task
    template_name = "task_delete.html"
    success_url = reverse_lazy("system:task-list")
    
    
class CommentCreateView(LoginRequiredMixin, CreateView):
    
    model = models.Comment
    form_class = CommentForm
    
    def form_valid(self, form):

        form.instance.commenters = self.request.user
        form.instance.task_id = self.kwargs['pk'] 
        return super().form_valid(form)

    def get_queryset(self):

        task_id = self.kwargs['pk']
        return Comment.objects.filter(task_id=task_id)

    def get_success_url(self):
        return reverse_lazy("system:task-detail", kwargs={'pk': self.kwargs['pk']})
    
class CommentUpdateView(LoginRequiredMixin, UserIsOwnerCommentMixin, UpdateView):
    model = models.Comment
    template_name = "comment_edit.html"
    form_class = CommentUpdateForm
    
    def get_success_url(self):
        return reverse_lazy("system:task-detail", kwargs={'pk': self.object.task.id})

class CommentDeleteView(LoginRequiredMixin, UserIsOwnerCommentMixin, DeleteView):
    model = models.Comment
    
    def get_success_url(self):
        return reverse_lazy("system:task-detail", kwargs={'pk': self.object.task.id})
    
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
