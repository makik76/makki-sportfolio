from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from .models import PersonalInfo, Skill, Project, ContactMessage

def home(request):
    personal_info = PersonalInfo.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    
    # Process tech stack for tags
    for project in projects:
        if project.tech_stack:
            project.tags_list = [tag.strip() for tag in project.tech_stack.split(',')]
        else:
            project.tags_list = []
            
    context = {
        'personal_info': personal_info,
        'skills': skills,
        'projects': projects,
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    return redirect('/#about')

def skills(request):
    return redirect('/#skills')

def works(request):
    return redirect('/#works')

def projects(request):
    return redirect('/#projects')

def chartboard(request):
    return redirect('/')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Save to database
        ContactMessage.objects.create(
            name=name, email=email, subject=subject, message=message
        )
        
        full_message = f"Message from {name} ({email}):\n\n{message}"
        
        try:
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            return JsonResponse({'status': 'success', 'message': 'Email sent successfully!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
            
    return redirect('/#contact')

