from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=10, default="xxx")
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.code}  {self.city}"
    

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination} ({self.duration} minutes)"
    
    def is_valid_flight(self):
        return self.origin != self.destination and self.duration >= 0