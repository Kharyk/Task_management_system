from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    
    STATUS_CHOICES_P = [
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("archived", "Archived"),
    ]
    
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True)
    link = models.URLField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES_P, default='active')
    
    

class Task(models.Model):
    
    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
        ("ideas", "Ideas"),
    ]
    
    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
        ("gd", "God Dammit"),#why not ;)
    ]
    
    title = models.CharField(max_length=256)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")

    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="todo")
    priority = models.CharField(max_length=20, choices= PRIORITY_CHOICES, default="medium")
    due_date = models.DateField(null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True, null=True )

    #auth
    
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
 