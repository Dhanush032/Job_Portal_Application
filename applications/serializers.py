from rest_framework import serializers
from applications.models import Application
from jobs.serializers import JobSerializer

class ApplicationSerializer(serializers.ModelSerializer):
    
    applicant_name = serializers.CharField(source='applicant.get_full_name', read_only=True)
    applicant_email = serializers.EmailField(source='applicant.email', read_only=True)
    job_title = serializers.CharField(source='job.title', read_only=True)
    company_name = serializers.CharField(source='job.company_name', read_only=True)
    
    class Meta:
        model = Application
        fields = [
            'id', 'job', 'job_title', 'company_name', 'applicant', 
            'applicant_name', 'applicant_email', 'resume', 'cover_letter',
            'status', 'applied_date'
        ]
        read_only_fields = ['id', 'applicant', 'applied_date', 'status']


class ApplicationCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Application
        fields = ['job', 'resume', 'cover_letter']
    
    def validate(self, data):
        
        user = self.context['request'].user
        job = data['job']
        
        if Application.objects.filter(applicant=user, job=job).exists():
            raise serializers.ValidationError("You have already applied to this job")
        
        return data


class ApplicationDetailSerializer(serializers.ModelSerializer):
    
    job = JobSerializer(read_only=True)
    applicant_name = serializers.CharField(source='applicant.get_full_name', read_only=True)
    applicant_email = serializers.EmailField(source='applicant.email', read_only=True)
    applicant_phone = serializers.CharField(source='applicant.phone', read_only=True)
    applicant_skills = serializers.CharField(source='applicant.skills', read_only=True)
    
    class Meta:
        model = Application
        fields = [
            'id', 'job', 'applicant', 'applicant_name', 'applicant_email',
            'applicant_phone', 'applicant_skills', 'resume', 'cover_letter',
            'status', 'applied_date'
        ]