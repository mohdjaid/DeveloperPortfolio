from django.contrib import admin
from .models import Skill, DeveloperProfile, Project

# Inline admin for displaying projects inside the profile view
class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1

# Customize DeveloperProfile admin
@admin.register(DeveloperProfile)
class DeveloperProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio_summary', 'get_skills')
    inlines = [ProjectInline]

    def bio_summary(self, obj):
        return obj.bio[:50] + "..." if len(obj.bio) > 50 else obj.bio
    bio_summary.short_description = 'Bio'

    def get_skills(self, obj):
        return ", ".join([skill.name for skill in obj.skills.all()])
    get_skills.short_description = 'Skills'

# Skill admin
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Project admin (optional if you want to view independently)
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'profile', 'tech_stack')
    search_fields = ('title', 'tech_stack')
