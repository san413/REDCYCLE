from django.db import models

class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    category = models.CharField(max_length=100)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.question
