from rest_framework import serializers
from .models import Task
from django.contrib.auth import get_user_model  # Import user model dynamically

# Get the correct user model dynamically to ensure compatibility
User = get_user_model()

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model.
    Converts Task model instances to JSON format and validates input data.
    """

    # Use PrimaryKeyRelatedField to handle multiple assigned users
    assigned_users = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.all()
    )

    class Meta:
        model = Task  # Define the model associated with this serializer
        fields = ['id', 'name', 'description', 'created_at', 'completed_at', 'status', 'assigned_users']
        # Include all required fields of the Task model
