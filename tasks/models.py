from django.db import models
from django.utils import timezone
from datetime import timedelta

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    deadline = models.DateTimeField(blank=True, null=True)

    def is_deadline_approaching(self):
        if self.deadline and not self.completed:
            return timezone.now() >= self.deadline - timedelta(days=1) and timezone.now() < self.deadline
        return False

    def is_overdue(self):
        if self.deadline and not self.completed:
            return timezone.now() > self.deadline
        return False

    def __str__(self):
        return self.title
