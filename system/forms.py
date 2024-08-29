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
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['project'].queryset = Project.objects.filter(creator_of_project=user)
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'image', 'files', 'link', 'due_date', "project"]
        
        widgets = {
            "media": forms.FileInput()
        }
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['text']
        
class CommentUpdateForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        commenters = kwargs.pop('commenters', None)
        super().__init__(*args, **kwargs)
        if commenters:
            self.fields['project'].queryset = Project.objects.filter(commenters=commenters)
    
    class Meta:
        model = Comment
        fields = ['text']

class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'files', 'link', 'status', "members"]
        
        widgets = {
            "media": forms.FileInput()
        }
        
class ProjectUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'link','files', 'status', "members"]
        
class TaskUpdateForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['project'].queryset = Project.objects.filter(creator_of_project=user)
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'image', 'link','files', 'due_date', "project"]
        