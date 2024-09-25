from django.shortcuts import render
from .models import Summary, Skill, Experience, Project, Education

def home(request):
    summary = Summary.objects.first()
    skills = Skill.objects.all()
    experiences = Experience.objects.all().order_by('-start_date')
    projects = Project.objects.all()
    education = Education.objects.all().order_by('-graduation_date')
    return render(request, 'main/home.html', {
        'summary': summary,
        'skills': skills,
        'experiences': experiences,
        'projects': projects,
        'education': education,
    })