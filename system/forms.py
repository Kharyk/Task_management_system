from django import forms
from system.models import Task, Comment, Project
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')
class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'image', 'link', 'due_date', "project"]
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['text',"task", "commenters"]
        
class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'link', 'status', "members"]
        
class ProjectUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'link', 'status']
        
class TaskUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'image', 'link', 'due_date', "project"]
        