from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.views import (
    UserRegistrationView,
    UserProfileView,
    UserListView,
    UserDeleteView,
    LogoutView
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('profile/', UserProfileView.as_view(), name='profile'),
    
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
]