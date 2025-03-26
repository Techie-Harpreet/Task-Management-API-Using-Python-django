from django.conf import settings  # Use AUTH_USER_MODEL for flexibility
from django.db import models
from django.contrib.auth.models import AbstractUser

class Task(models.Model):
    """
    Model representing a task with status tracking, assignment, and timestamps.
    """

    # Define choices for task status
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]
    
    name = models.CharField(max_length=255)  # Task title
    description = models.TextField()  # Task details
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when task is created
    task_type = models.CharField(max_length=100, blank=True, null=True)  # Optional field for task categorization
    completed_at = models.DateTimeField(blank=True, null=True)  # Timestamp when task is completed
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")  # Task status (default: Pending)
    
    # Many-to-Many relationship with users to allow multiple assignees per task
    assigned_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="tasks")

    def __str__(self):
        """Return task name as string representation."""
        return self.name

class CustomUser(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    Adds a unique mobile number field.
    """

    mobile = models.CharField(max_length=15, unique=True, null=True, blank=True)  # Optional mobile field
