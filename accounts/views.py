from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.models import User
from accounts.serializers import UserRegistrationSerializer, UserProfileSerializer, UserListSerializer

class UserRegistrationView(generics.CreateAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'user': UserProfileSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'message': 'User registered successfully'
        }, status=status.HTTP_201_CREATED)


class UserProfileView(generics.RetrieveUpdateAPIView):
    
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        
        return self.request.user
    
    def update(self, request, *args, **kwargs):
        
        partial = kwargs.pop('partial', True)  
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class UserListView(generics.ListAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        
        if user.role == 'admin':
            return User.objects.all()
        return User.objects.none()


class UserDeleteView(generics.DestroyAPIView):
    
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    def delete(self, request, *args, **kwargs):
        user = self.request.user
        if user.role != 'admin':
            return Response(
                {'error': 'Only admin can delete users'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().delete(request, *args, **kwargs)


class LogoutView(APIView):
    
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)