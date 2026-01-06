from django.db import models
from accounts.models import User

class Job(models.Model):
    
    JOB_TYPE_CHOICES = (
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
    )
    
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_jobs')
    title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES, default='full_time')
    salary = models.CharField(max_length=100, help_text="e.g., 50000-70000 or Negotiable")
    description = models.TextField()
    requirements = models.TextField(help_text="Skills and qualifications required")
    posted_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.title} at {self.company_name}"
    
    class Meta:
        ordering = ['-posted_date']
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'