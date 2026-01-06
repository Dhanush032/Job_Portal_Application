from django.urls import path
from jobs.views import (
    JobListView,
    JobDetailView,
    JobCreateView,
    EmployerJobListView,
    JobUpdateView,
    JobDeleteView,
    AllJobsAdminView
)

urlpatterns = [
    path('', JobListView.as_view(), name='job_list'),
    path('<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('create/', JobCreateView.as_view(), name='job_create'),
    path('my-jobs/', EmployerJobListView.as_view(), name='employer_jobs'),
    path('<int:pk>/update/', JobUpdateView.as_view(), name='job_update'),
    path('<int:pk>/delete/', JobDeleteView.as_view(), name='job_delete'),
    path('admin/all/', AllJobsAdminView.as_view(), name='admin_all_jobs'),
]