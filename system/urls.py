from django.urls import path
from system import views
from .views import HomepageView, LearnMoreView, ContactView

urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('learn-more/', LearnMoreView.as_view(), name='learn-more'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('tasks/', views.TaskListView.as_view(), name="task-list"),
    path("<int:pk>/", views.TaskDetailView.as_view(), name="task-detail"),
    path("task-create", views.TaskCreateView.as_view(), name="task-create"),
    path("comments", views.CommentCreateView.as_view(), name="comments"),
    path('projects/', views.ProjectListView.as_view(), name='project-list'),
    path('projects/create/', views.ProjectCreateView.as_view(), name='project-create'),
    path('projects/<pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('<int:pk>/update/task', views.TaskUpdateView.as_view(), name= 'task-update'),
    path('<int:pk>/update/project', views.ProjectUpdateView.as_view(), name= 'project-update'),
    path('<int:pk>/delete/task', views.TaskDeleteView.as_view(), name= 'task-delete'), 
    path('<int:pk>/delete.project', views.ProjectDeleteView.as_view(), name= 'project-delete'),


    #path("<int:pk>/complete/", views.TaskCompleteView.as_view(), name= "task-complete")

]

app_name =  "system"