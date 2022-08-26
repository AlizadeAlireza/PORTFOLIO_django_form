from django.shortcuts import render
from portfolio.models import Project
# Create your views here.

def project_index(request):
    projects = Project.objects.all()

    context = {
        'projects': projects
    }
    
    return render(request, 'portfolio/index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk = pk)

    context = {
        'project': project
    }

    return render(request, 'portfolio/detail.html', context)


