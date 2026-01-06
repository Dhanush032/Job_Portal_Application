from rest_framework import generics, permissions, status
from rest_framework.response import Response
from jobs.models import Job
from jobs.serializers import JobSerializer, JobCreateSerializer

class JobListView(generics.ListAPIView):
    queryset = Job.objects.filter(is_active=True)
    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]


class JobDetailView(generics.RetrieveAPIView):
    queryset = Job.objects.filter(is_active=True)
    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]


class JobCreateView(generics.CreateAPIView):
    serializer_class = JobCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request):
        user = request.user
        
        if user.role != 'employer':
            return Response(
                {'error': 'Only employers can post jobs'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        job = serializer.save(employer=user)
        
        return Response(
            JobSerializer(job).data,
            status=status.HTTP_201_CREATED
        )


class EmployerJobListView(generics.ListAPIView):
    
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        
        if user.role == 'employer':
            return Job.objects.filter(employer=user)
        return Job.objects.none()


class JobUpdateView(generics.UpdateAPIView):
    
    serializer_class = JobCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        # Employer can only update their own jobs
        if user.role == 'employer':
            return Job.objects.filter(employer=user)
        return Job.objects.none()


class JobDeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        
        if user.role == 'admin':
            return Job.objects.all()
        
        if user.role == 'employer':
            return Job.objects.filter(employer=user)
        
        return Job.objects.none()


class AllJobsAdminView(generics.ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Job.objects.all()
        return Job.objects.none()