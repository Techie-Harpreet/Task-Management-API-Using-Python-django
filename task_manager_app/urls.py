from django.urls import path
from .views import CreateTaskView, AssignTaskView, UserTasksView, UserListView
from rest_framework.authtoken.views import obtain_auth_token

# Define URL patterns for task-related API endpoints
urlpatterns = [
    # Endpoint for creating a new task
    path("tasks/create/", CreateTaskView.as_view(), name="create-task"),

    # Endpoint for assigning a task to one or more users (requires task ID)
    path("tasks/<int:pk>/assign/", AssignTaskView.as_view(), name="assign-task"),

    # Endpoint to fetch a list of all tasks
    path("tasks/", UserTasksView.as_view(), name="task-list"),

    # Endpoint to fetch tasks assigned to a specific user (requires user ID)
    path("tasks/user/<int:user_id>/", UserTasksView.as_view(), name="user-tasks"),

    # Endpoint to obtain an authentication token
    path('token/', obtain_auth_token, name='api_token_auth'),

    # Endpoint to retrieve a list of all registered users
    path("users/", UserListView.as_view(), name="user-list"),
]
