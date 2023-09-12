import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from project.models import Project
from project.services import ProjectService
from project.seriailzers import (
    ProjectListSerializer,
    ProjectDetailSerializer,
    ProjectUpdateSerializer,
)

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def sample_project():
    return Project.objects.create(title="Test Project")

@pytest.mark.django_db
def test_project_list(api_client, sample_project):
    url = reverse("project-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == ProjectListSerializer([sample_project], many=True).data

@pytest.mark.django_db
def test_create_project(api_client):
    url = reverse("project-list")
    data = {"title": "New Project"}
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Project.objects.filter(title="New Project").exists()

@pytest.mark.django_db
def test_project_detail(api_client, sample_project):
    url = reverse("project-detail", args=[sample_project.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == ProjectDetailSerializer(sample_project).data

@pytest.mark.django_db
def test_update_project(api_client, sample_project):
    url = reverse("project-detail", args=[sample_project.id])
    data = {"title": "Updated Project"}
    response = api_client.put(url, data)
    assert response.status_code == status.HTTP_200_OK
    sample_project.refresh_from_db()
    assert sample_project.title == "Updated Project"

@pytest.mark.django_db
def test_invalid_update(api_client, sample_project):
    url = reverse("project-detail", args=[sample_project.id])
    data = {"nonexistent_field": "Updated Project"}  # Invalid field
    response = api_client.put(url, data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
