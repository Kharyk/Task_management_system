from django.urls import path
from system import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name="task-list"),
    path("<int:pk>/", views.TaskDetailView.as_view(), name="task-detail")
]