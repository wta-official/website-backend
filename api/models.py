from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Category(models.Model):
  title = models.CharField(max_length=255)

  def __str__(self):
    return self.title
  
class Partner(models.Model):
  name = models.CharField(max_length=255)
  image= models.ImageField(upload_to='partners/')

  def __str__(self):
    return self.name
  

class Work(models.Model):
  title = models.CharField(max_length=255)
  category = models.ManyToManyField(Category, related_name="works")
  partners = models.ManyToManyField(Partner, related_name="works")
  image = models.ImageField(upload_to='works/')

  def __str__(self):
    return self.title
  
class Talent(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    works = models.ManyToManyField(Work, related_name="talents")
    image = models.ImageField(upload_to='talents/')
    instagram = models.CharField(max_length=255, blank=True, null=True)
    x = models.CharField(max_length=255, blank=True, null=True)  # For X (Twitter)
    linkedIn = models.CharField(max_length=255, blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    eye_color = models.CharField(max_length=100, blank=True, null=True)
    hair = models.CharField(max_length=100, blank=True, null=True)
    dietary_requirements = models.TextField(blank=True, null=True)
    roles = ArrayField(models.CharField(max_length=255), blank=True, default=list)
    partners = models.ManyToManyField(Partner, related_name="talents")

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title
        

