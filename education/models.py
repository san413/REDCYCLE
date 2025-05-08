from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='articles/')
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_url = models.URLField()
    thumbnail = models.ImageField(upload_to='videos/')
    published = models.BooleanField(default=True)  

class Article(models.Model):
    CATEGORY_CHOICES = [
        ('hygiene', 'Menstrual Hygiene'),
        ('myths', 'Period Myths'),
        ('nutrition', 'Nutrition & Health'),
        ('first_period', 'First Period Guide'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    published = models.BooleanField(default=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='hygiene')      

    def __str__(self):
        return self.title
    
    

