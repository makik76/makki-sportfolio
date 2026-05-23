from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse

def home(request):
    return render(request, 'portfolio/home.html')

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

