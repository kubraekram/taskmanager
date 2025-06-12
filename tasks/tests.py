from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Task

class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.task = Task.objects.create(
            title="Sample Task",
            description="Description",
            status="pending",
            category="Work"
        )

    def test_create_task(self):
        data = {"title": "New Task", "description": "Test Desc", "status": "pending", "category": "Personal"}
        response = self.client.post("/api/tasks/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_task(self):
        response = self.client.get(f"/api/tasks/{self.task.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_task(self):
        data = {"title": "Updated", "description": "Updated", "status": "completed", "category": "Work"}
        response = self.client.put(f"/api/tasks/{self.task.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        response = self.client.delete(f"/api/tasks/{self.task.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
