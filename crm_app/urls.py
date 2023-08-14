from django.urls import path
from crm_app import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create-task/',views.create_task, name='create_task'),
    path('<int:task_id>/', views.task_detail, name='task_detail'),
    ]
