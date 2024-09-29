from django.db import models

class Watch(models.Model):
    name = models.CharField(max_length=255)
    amazon_link = models.CharField(max_length=255)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def latest_price(self):
        return self.price_set.latest("timestamp")

class Price(models.Model):
    watch = models.ForeignKey(Watch, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
