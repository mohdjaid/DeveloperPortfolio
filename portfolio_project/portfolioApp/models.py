from django.db import models
from django.contrib.auth.models import User

# Skill Model
class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Developer Profile Model
class DeveloperProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField()
    skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return self.user.username

# Project Model
class Project(models.Model):
    profile = models.ForeignKey(DeveloperProfile, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=100)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    github_link = models.URLField(blank=True, null=True)
    demo_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.profile.user.username})"
