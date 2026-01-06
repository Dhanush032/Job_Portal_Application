from django.shortcuts import render
from django.shortcuts import get_object_or_404
from jobs.models import Job

def home_view(request):
    return render(request, 'home.html')

def register_view(request):
    return render(request, 'register.html')

def login_view(request):
    return render(request, 'login.html')

def profile_view(request):
    return render(request, 'profile.html')

def job_list_view(request):
    
    return render(request, 'job_list.html')

def job_detail_view(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'job_detail.html', {'job': job})

def post_job_view(request):
    return render(request, 'post_job.html')

def my_applications_view(request):
    return render(request, 'my_applications.html')

def admin_dashboard_view(request):
    return render(request, 'admin_dashboard.html')