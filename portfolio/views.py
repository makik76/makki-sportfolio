from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def skills(request):
    return render(request, 'portfolio/skills.html')

def works(request):
    return render(request, 'portfolio/works.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def chartboard(request):
    return render(request, 'portfolio/chartboard.html')

def contact(request):
    return render(request, 'portfolio/contact.html')
