from django.urls import path
from .views import (
    TaskListCreateAPIView,
    TaskRetrieveUpdateDestroyAPIView,
    APIRootView,
    home
)

urlpatterns = [
    path('', APIRootView.as_view(), name='api-root'),  # this handles /api/
    path('tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-detail'),
    path('home/', home, name='home'),  # optional: loads your index.html template
]
