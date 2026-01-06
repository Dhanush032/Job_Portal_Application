from django.db import models
from accounts.models import User
from jobs.models import Job

class Application(models.Model):
    
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )
    
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    applied_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.applicant.username} applied for {self.job.title}"
    
    class Meta:
        ordering = ['-applied_date']
        unique_together = ('job', 'applicant') 
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'