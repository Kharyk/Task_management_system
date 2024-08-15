from django import forms
from system.models import Task, Comment, Project

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'image', 'link', 'due_date']
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['text',"task", "commenters"]
        
class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ('title', 'description', 'image', 'link', 'status', "user")
        
class TaskUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'image', 'link']
        