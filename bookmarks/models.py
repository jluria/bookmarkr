from django.db import models

class Link(models.Model):
    name = models.CharField(max_length=50)
    address = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    tags = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class List(models.Model):
    name = models.CharField(max_length=50, help_text="Name Your List:")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    links = models.ManyToManyField(Link, help_text="Help")

    def __str__(self):
        return self.name

# Create your models here.
