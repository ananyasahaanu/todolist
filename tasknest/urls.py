from django.contrib import admin
from django.urls import path
from tasksapp import views as task_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication
    path('register/', task_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Tasks
    path('', task_views.task_list, name='task_list'),
    path('task/add/', task_views.task_create, name='task_create'),
    path('task/<int:pk>/edit/', task_views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', task_views.task_delete, name='task_delete'),
]
