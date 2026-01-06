from rest_framework import serializers
from jobs.models import Job

class JobSerializer(serializers.ModelSerializer):
    employer_name = serializers.CharField(source='employer.username', read_only=True)
    employer_email = serializers.EmailField(source='employer.email', read_only=True)
    total_applications = serializers.SerializerMethodField()
    
    class Meta:
        model = Job
        fields = [
            'id', 'employer', 'employer_name', 'employer_email', 'title', 
            'company_name', 'location', 'job_type', 'salary', 'description',
            'requirements', 'posted_date', 'updated_date', 'is_active', 'total_applications'
        ]
        read_only_fields = ['id', 'employer', 'posted_date', 'updated_date']
    
    def get_total_applications(self, obj):
        return obj.applications.count()


class JobCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            'title', 'company_name', 'location', 'job_type', 
            'salary', 'description', 'requirements'
        ]