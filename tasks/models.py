from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    deadline = models.DateTimeField(blank=True, null=True)

    def is_deadline_approaching(self):
        if self.deadline:
            return timezone.now() >= self.deadline - timezone.timedelta(days=1)  # 1 hari sebelum deadline
        return False

    def __str__(self):
        return self.title
