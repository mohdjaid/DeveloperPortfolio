from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, DeveloperProfileViewSet, ProjectViewSet, SkillViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'profile', DeveloperProfileViewSet, basename='profile')
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'skills', SkillViewSet, basename='skills')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
