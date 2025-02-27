from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    deadline = models.DateTimeField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=True)

    # Metode untuk memberikan pesan warning
    def is_deadline_approaching(self):
        if self.deadline and not self.completed:
            return timezone.now() >= self.deadline - timedelta(days=1) and timezone.now() < self.deadline
        return False

    # Metode untuk cek waktu deadline
    def is_overdue(self):
        if self.deadline and not self.completed:
            return timezone.now() > self.deadline
        return False

    # Metode untuk menampilkan tasks 
    def __str__(self):
        return (f"Title: {self.title}, Description: {self.description}")

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return self.user.username