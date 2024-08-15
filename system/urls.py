from django.urls import path
from system import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name="task-list"),
    path("<int:pk>/", views.TaskDetailView.as_view(), name="task-detail"),
    path("task-create", views.TaskCreateView.as_view(), name="task-create"),
    path("comments", views.CommentCreateView.as_view(), name="comments"),
    path('projects/', views.ProjectListView.as_view(), name='project-list'),
    path('projects/create/', views.ProjectCreateView.as_view(), name='project-create'),
    path('projects/<pk>/', views.ProjectDetailView.as_view(), name='project-detail'),

]

app_name =  "system"