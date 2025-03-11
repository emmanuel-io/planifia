from django.db.models import Prefetch
from django.shortcuts import render, get_object_or_404
from .models import TaskType
from .models import ProjectTemplate, TaskTemplate, TaskType
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.http import JsonResponse

def jwt_login_view(request):
    """Vue pour gérer l'authentification JWT"""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return JsonResponse({"access": str(refresh.access_token), "refresh": str(refresh)}, status=200)

        return JsonResponse({"error": "Invalid credentials"}, status=400)

def index(request):
    return render(request, 'index.html')

def task_type_list(request):
    task_types = TaskType.objects.all()
    return render(request, 'task_type/list.html', {'task_types': task_types})

def task_type_details(request, task_uuid):
    task_type = get_object_or_404(TaskType, uuid=task_uuid)
    return render(request, 'task_type/details.html', {'task_type': task_type})

def project_template_list(request):
    project_templates = ProjectTemplate.objects.all()
    return render(request, 'project_template/list.html', {'project_templates': project_templates})

def project_template_details(request, template_uuid):
    project_template = get_object_or_404(
        ProjectTemplate.objects.prefetch_related(
            Prefetch(
                "tasks",
                queryset=TaskTemplate.objects.select_related("task_type")
            )
        ),
        uuid=template_uuid
    )
    return render(request, 'project_template/details.html', {'template': project_template})

