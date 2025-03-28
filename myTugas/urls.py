"""
URL configuration for myTugas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views
from tasks.views import edit_profile
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Authentication
    path('', views.user_login, name='login'),
    path("logout/", views.user_logout, name='logout'),
    path("register/", views.register, name='register'),

    # Dashboard & Task Management
    path("home/", views.index, name='index'),
    path("add_task/", views.add_todo, name="add_task"),
    path("tugas/", views.tugas_list, name="tugas_list"),
    path("ask/", views.ask_ai, name="ask_ai"),

    # Task Actions
    path("restore/<int:task_id>/", views.restore_task, name="restore_task"),
    path("edit/<int:task_id>/", views.edit_task, name="edit_task"),
    path("delete/<int:task_id>/", views.delete_task, name="delete_task"),
    path("started/<int:task_id>/", views.started_task, name="started_task"),
    path("short_tasks/", views.short_task, name="short_task"),

    # Profile
    path("profile/edit/", views.edit_profile, name="edit_profile"),

    # Admin
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



