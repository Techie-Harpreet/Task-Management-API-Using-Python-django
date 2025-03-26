from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin panel URL
    path('admin/', admin.site.urls),

    # Include API routes from the 'task_manager_app' application
    path('api/', include('task_manager_app.urls')),  
]
