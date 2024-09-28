from django.db import models

class Watch(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField()  # URL to the watch image
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Price(models.Model):
    watch = models.ForeignKey(Watch, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    platform = models.CharField(max_length=255)
    url = models.URLField()  # URL of the platform listing
    timestamp = models.DateTimeField(auto_now_add=True)
