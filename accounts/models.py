from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('employer', 'Employer'),
        ('job_seeker', 'Job Seeker'),
    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='job_seeker')
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    
    company_name = models.CharField(max_length=200, blank=True, null=True)
    company_website = models.URLField(blank=True, null=True)
    
    skills = models.TextField(blank=True, null=True, help_text="Comma separated skills")
    experience_years = models.IntegerField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.username} ({self.role})"
    
    class Meta:
        ordering = ['-created_at']