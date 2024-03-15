from django.db import models

# Create your models here.

class SkillsItem(models.Model):
    skills = models.CharField(max_length=200)

class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/')
    alt = models.CharField(max_length=200)
    href = models.URLField()
    types = models.CharField(max_length=200)

    def __str__(self):
        return self.title