import pytest
from django.urls import reverse
from rest_framework import status
from project.models.project import Project
from account.models import UserAccount
from project.serializers.project_seriailzer import (
    ProjectListSerializer,
    ProjectDetailSerializer,
)

@pytest.fixture
@pytest.mark.django_db
def sample_project():
    return Project.objects.create(title="Test Project")

@pytest.mark.django_db
def test_project_list_api(authenticated_client, sample_project):
    url = reverse("project-list")
    response = authenticated_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == ProjectListSerializer([sample_project], many=True).data

@pytest.mark.django_db
def test_project_create_api(authenticated_client):
    url = reverse("project-list")
    data = {"title": "New Project", "description": "This is description"}
    response = authenticated_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Project.objects.filter(title="New Project").exists()

@pytest.mark.django_db
def test_project_detail_api(authenticated_client, sample_project):
    url = reverse("project-detail", args=[sample_project.id])
    response = authenticated_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == ProjectDetailSerializer(sample_project).data

@pytest.mark.django_db
def test_update_project_api(authenticated_client, sample_project):
    url = reverse("project-detail", args=[sample_project.id])
    data = {"title": "Updated Project"}
    response = authenticated_client.put(url, data)
    assert response.status_code == status.HTTP_200_OK
    sample_project.refresh_from_db()
    assert sample_project.title == "Updated Project"

@pytest.mark.django_db
def test_invalid_update(authenticated_client, sample_project, ):
    url = reverse("project-detail", args=[sample_project.id])
    data = {"nonexistent_field": "Updated Project"}  # Invalid field
    response = authenticated_client.put(url, data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST