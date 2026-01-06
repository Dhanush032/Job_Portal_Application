from django.urls import path
from applications.views import (
    ApplicationCreateView,
    MyApplicationsView,
    JobApplicationsView,
    ApplicationStatusUpdateView,
    AllApplicationsAdminView
)

urlpatterns = [
    path('apply/', ApplicationCreateView.as_view(), name='application_create'),
    path('my-applications/', MyApplicationsView.as_view(), name='my_applications'),
    path('job/<int:job_id>/', JobApplicationsView.as_view(), name='job_applications'),
    path('<int:pk>/status/', ApplicationStatusUpdateView.as_view(), name='application_status'),
    path('admin/all/', AllApplicationsAdminView.as_view(), name='admin_all_applications'),
]