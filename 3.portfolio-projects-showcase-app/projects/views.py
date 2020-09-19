"""
    We're going to have two different views:
    1. An index view that shows a snippet of information about each project
    2. A details view that shows more information on a particular topic
"""
from django.shortcuts import render
from projects.models import Project

# Create your views here.
def project_index(request):
    """
        The objects.all() query allows you to create, retrieve, update, or delete objects (or rows) in db
        Dictionary 'context' assigns our Queryset containing all projects
        'context is added as an argument to render()
    """
    projects = Project.objects.all()
    context = { 'projects': projects }
    return render(request, 'project_index.html', context)

def project_details(request, pk):
    """
        This query retrieves the project with primary key (pk), equal to that in the function argument.
        We then assign that project in our context dictionary, which we pass to render()
    """
    project = Project.objects.get(pk=pk)
    context = { 'project': project }
    return render(request, 'project_details.html', context)