from . import models
from rest_framework import serializers

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SkillsItem
        fields = ['id', 'skills']

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PortfolioItem
        fields = ['id', 'title', 'image', 'alt', 'href', 'types']

