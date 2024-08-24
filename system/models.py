from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    
    STATUS_CHOICES_P = [
        ("Active", "active"),
        ("Inactive", "inactive"),
        ("Archived", "archived"),
    ]
    
    title = models.CharField(max_length=200)
    creator_of_project = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name= 'member', blank=True)

    description = models.TextField()
    image = models.ImageField(upload_to='static/img/projects/', blank=True)
    link = models.URLField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES_P, default='active')
    
    def __str__(self):
        return self.title
    
    

class Task(models.Model):
    
    STATUS_CHOICES = [
        ("To-Do", "todo"),
        ("In Progress", "in_progress"),
        ("Done", "done"),
        ("Ideas", "ideas"),
    ]
    
    PRIORITY_CHOICES = [
        ("Low", "low"),
        ("Medium", "medium"),
        ("High", "high"),
        ("God Dammit", "gd"),  # why not ;) 
    ]
    
    title = models.CharField(max_length=256)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks_in_project",  blank=True, null=True)

    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="todo")
    priority = models.CharField(max_length=20, choices= PRIORITY_CHOICES, default="medium")
    due_date = models.DateField(null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True, null=True )

    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="task")
    commenters = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenters")
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.commenters.username} on {self.task.title}'
# Create your models here.
 