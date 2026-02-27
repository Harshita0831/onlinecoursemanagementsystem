from django.db import models
from accounts.models import User

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Course(models.Model):

    LEVEL_CHOICES = [
        ('BEGINNER', 'Beginner'),
        ('INTERMEDIATE', 'Intermediate'),
        ('ADVANCED', 'Advanced')
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Module(models.Model):

    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    order = models.IntegerField()

    class Meta:
        unique_together = ('course','order')

    def __str__(self):
        return self.title
    
class Lecture(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    video_url = models.URLField()
    notes = models.TextField(blank=True)
    order = models.IntegerField()
    duration = models.IntegerField(help_text="Duration in seconds")

    class Meta:
        unique_together = ('module','order')

    def __str__(self):
        return self.title
