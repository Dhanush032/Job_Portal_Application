from rest_framework import generics, permissions, status
from rest_framework.response import Response
from applications.models import Application
from applications.serializers import (
    ApplicationSerializer, 
    ApplicationCreateSerializer, 
    ApplicationDetailSerializer
)

class ApplicationCreateView(generics.CreateAPIView):
    
    serializer_class = ApplicationCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request):
        user = request.user
        
        if user.role != 'job_seeker':
            return Response(
                {'error': 'Only job seekers can apply for jobs'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        application = serializer.save(applicant=user)
        
        return Response(
            ApplicationSerializer(application).data,
            status=status.HTTP_201_CREATED
        )


class MyApplicationsView(generics.ListAPIView):
    
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.role == 'job_seeker':
            return Application.objects.filter(applicant=user)
        return Application.objects.none()


class JobApplicationsView(generics.ListAPIView):
    serializer_class = ApplicationDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        job_id = self.kwargs.get('job_id')
        
        if user.role == 'employer':
            return Application.objects.filter(
                job_id=job_id,
                job__employer=user
            )
        return Application.objects.none()


class ApplicationStatusUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        
        if user.role == 'employer':
            return Application.objects.filter(job__employer=user)
        return Application.objects.none()
    
    def update(self, request):
        application = self.get_object()
        new_status = request.data.get('status')
        
        if new_status not in ['pending', 'accepted', 'rejected']:
            return Response(
                {'error': 'Invalid status. Use pending, accepted, or rejected'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        application.status = new_status
        application.save()
        
        return Response(
            ApplicationDetailSerializer(application).data,
            status=status.HTTP_200_OK
        )


class AllApplicationsAdminView(generics.ListAPIView):
    serializer_class = ApplicationDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        
        if user.role == 'admin':
            return Application.objects.all()
        return Application.objects.none()