from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)


class Films(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    release_date = models.DateField()
    actors = models.TextField()
    show_date = models.DateField()