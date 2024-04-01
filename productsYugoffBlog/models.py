from django.db import models

# Create your models here.

class SkillsItem(models.Model):
    skills = models.CharField(max_length=200)

    def __str__(self):
        return f'Навыки: {self.skills}'

class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    alt = models.CharField(max_length=200)
    href = models.URLField()
    types = models.CharField(max_length=200)

    def __str__(self):
        return f'Портфолио: {self.title}'