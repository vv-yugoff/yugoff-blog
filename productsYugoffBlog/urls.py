from django.urls import path, re_path
from .views import (
    SkillsListCreateView, 
    SkillsRetrieveUpdateDestroyView,
    PortfolioListCreateView, 
    PortfolioRetrieveUpdateDestroyView,
)
from channels.routing import URLRouter

urlpatterns = [
    path('api/skills/', SkillsListCreateView.as_view(), name='skills-list-create'),
    path('api/skills/<int:pk>/', SkillsRetrieveUpdateDestroyView.as_view(), name='skills-detail'),
    path('api/portfolio/', PortfolioListCreateView.as_view(), name='portfolio-list-create'),
    path('api/portfolio/<int:pk>/', PortfolioRetrieveUpdateDestroyView.as_view(), name='portfolio-detail'),
]
