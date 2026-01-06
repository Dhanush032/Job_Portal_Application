
from django.urls import path
from .views import (
    home_view, register_view, login_view, profile_view,
    job_list_view, job_detail_view, post_job_view,
    my_applications_view, admin_dashboard_view
)

urlpatterns = [
    # Frontend pages
    path('', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('jobs/', job_list_view, name='jobs'),
    path('jobs/<int:pk>/', job_detail_view, name='job_detail'),
    path('post-job/', post_job_view, name='post_job'),
    path('my-applications/', my_applications_view, name='my_applications'),
    path('admin-dashboard/', admin_dashboard_view, name='admin_dashboard'),
]