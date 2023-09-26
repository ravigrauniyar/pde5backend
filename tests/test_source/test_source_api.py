import pytest
from django.urls import reverse
from rest_framework import status
from project.models.source import Source
from project.models.project import Project
from account.models import UserAccount
from project.serializers.source_serializer import (
    SourceDetailSerializer,
    SourceListSerializer
)
from tests.test_source.source_test_data import SourceFactory

@pytest.fixture
@pytest.mark.django_db
def sample_source():
    return SourceFactory()

@pytest.mark.django_db
def test_source_list_api(authenticated_client, sample_source):
    url = reverse("source-list")
    response = authenticated_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) >= 1

@pytest.mark.django_db
def test_source_create_api(authenticated_client, sample_source):
    url = reverse("source-list")
    data = {
        "name": "New Source",
        "description": "This is description",
        "tag": "random-tag",
        "project_id": sample_source.project.id,
        "token": "random-token"
    }
    response = authenticated_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Source.objects.filter(name="New Source").exists()

@pytest.mark.django_db
def test_source_detail_api(authenticated_client, sample_source):
    url = reverse("source-detail", args=[sample_source.id])
    response = authenticated_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == SourceDetailSerializer(sample_source).data