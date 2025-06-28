from rest_framework import serializers
from django.contrib.auth.models import User
from .models import DeveloperProfile, Skill, Project

# User Registration Serializer
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

# Skill Serializer
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']

    def validate_name(self, value):
        print(f"[DEBUG] Skill name received: '{value}'")  
        if not value.strip():
            raise serializers.ValidationError("Skill name cannot be empty.")
        return value
    
# Project Serializer
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['profile']
# Developer Profile Serializer
class DeveloperProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    skills = SkillSerializer(many=True, read_only=True)
    skill_ids = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all(), many=True, write_only=True)
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = DeveloperProfile
        fields = ['id', 'user', 'bio', 'skills', 'skill_ids', 'projects']

    def create(self, validated_data):
        skill_ids = validated_data.pop('skill_ids', [])
        profile = DeveloperProfile.objects.create(**validated_data)
        profile.skills.set(skill_ids)
        return profile

    def update(self, instance, validated_data):
        skill_ids = validated_data.pop('skill_ids', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if skill_ids is not None:
            instance.skills.set(skill_ids)
        return instance
