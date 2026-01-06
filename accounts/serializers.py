from rest_framework import serializers
from accounts.models import User
from django.contrib.auth.password_validation import validate_password

class UserRegistrationSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True, label="Confirm Password")
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'role', 'first_name', 'last_name', 'phone']
        extra_kwargs = {
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
        }
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords don't match"})
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')
        
        user = User.objects.create_user(**validated_data)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name', 'role',
            'phone', 'address', 'profile_picture', 'company_name', 
            'company_website', 'skills', 'experience_years', 'created_at'
        ]
        read_only_fields = ['id', 'username', 'role', 'created_at']

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance



class UserListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'first_name', 'last_name', 'created_at']