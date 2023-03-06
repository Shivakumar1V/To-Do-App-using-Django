from django.urls import path
from api import views

urlpatterns = [
    path('task-list/', views.taskList, name='taskList'),
    path('create-task/', views.createTask, name='createTask'),
    path('update-task/<str:pk>/', views.updateTask, name='updateTask'),
    path('delete-task/<str:pk>/', views.deleteTask, name='deleteTask'),
]
