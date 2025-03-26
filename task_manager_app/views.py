from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import Task
from .serializers import TaskSerializer

# Get the user model dynamically
User = get_user_model()

class UserListView(APIView):
    """
    API endpoint to retrieve all registered users.
    Only authenticated users can access this list.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        user_data = [
            {
                "id": user.id,
                "name": user.username,
                "email": user.email,
            }
            for user in users
        ]
        return Response(user_data, status=status.HTTP_200_OK)
    
class CreateTaskView(APIView):
    """
    API endpoint to create a new task.
    Only authenticated users can create a task.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new task in the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssignTaskView(APIView):
    """
    API endpoint to assign users to a task.
    Accepts a list of user IDs and assigns them to a specific task.
    """
    def post(self, request, pk, *args, **kwargs):  # `pk` represents the task ID
        task = get_object_or_404(Task, id=pk)  # Fetch the task, return 404 if not found

        assigned_users = request.data.get("assigned_users", [])
        if not assigned_users:
            return Response({"error": "assigned_users field is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve users based on the provided IDs
        users = User.objects.filter(id__in=assigned_users)
        if not users.exists():
            return Response({"error": "Some users do not exist."}, status=status.HTTP_400_BAD_REQUEST)

        # Assign users to the task
        task.assigned_users.set(users)
        task.save()

        return Response({"message": "Task assigned successfully."}, status=status.HTTP_200_OK)

class TaskListView(APIView):
    """
    API endpoint to retrieve a list of all tasks.
    Only authenticated users can access this list.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)  # Serialize multiple tasks
        return Response(serializer.data)

class UserTasksView(APIView):
    """
    API endpoint to retrieve tasks assigned to a specific user.
    - If `user_id` is provided, it returns tasks assigned to that user.
    - If `user_id` is not provided, it returns all tasks.
    """
    def get(self, request, user_id=None, *args, **kwargs):
        if user_id:  
            # If `user_id` is provided, fetch tasks assigned to that user
            user = get_object_or_404(User, id=user_id)
            tasks = Task.objects.filter(assigned_users=user)
        else:
            # If no `user_id` is provided, return all tasks
            tasks = Task.objects.all()

        # Format the tasks into a structured JSON response
        task_data = [
            {
                "id": task.id,
                "name": task.name,
                "description": task.description,
                "status": task.status,
                "assigned_users": [user.id for user in task.assigned_users.all()],
            }
            for task in tasks
        ]

        return Response(task_data, status=status.HTTP_200_OK)
