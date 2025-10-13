from django.db import models


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"


class ContactMessage(models.Model):
    name = models.CharField("Name", max_length=100)
    email = models.EmailField("E-Mail")
    message = models.TextField("Nachricht")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"
