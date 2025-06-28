from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User

from .models import DeveloperProfile, Project, Skill
from .serializers import (
    UserSerializer,
    DeveloperProfileSerializer,
    ProjectSerializer,
    SkillSerializer
)

# Register View
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully"}, status=201)
        return Response(serializer.errors, status=400)

# Skill ViewSet
class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Project ViewSet
class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(profile__user=self.request.user)

    def perform_create(self, serializer):
        profile = DeveloperProfile.objects.get(user=self.request.user)
        serializer.save(profile=profile)

# Developer Profile ViewSet
class DeveloperProfileViewSet(viewsets.ModelViewSet):
    serializer_class = DeveloperProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return DeveloperProfile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
