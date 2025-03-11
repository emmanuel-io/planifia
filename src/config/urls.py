"""
URL configuration for area project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from apps.tasks import views as tasks_views
from apps.users import views as users_views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('admin/', admin.site.urls),
    path('', tasks_views.index, name='index'),
    path('create/', users_views.create_user, name='create_user'),
    path('delete/<int:user_id>/', users_views.delete_user, name='delete_user'),
    path('list/', users_views.user_list, name='user_list'),
    path('task-types/', tasks_views.task_type_list, name='task_type_list'),
    path('task-types/<uuid:task_uuid>', tasks_views.task_type_details, name='task_type_details'),
    path('project-templates/', tasks_views.project_template_list, name='project_template_list'),
    path('project-templates/<uuid:template_uuid>', tasks_views.project_template_details, name='project_template_details'),

    # path("", views.index, name="index"),
]
