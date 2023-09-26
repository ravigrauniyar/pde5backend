import pytest
from django.http import Http404
from project.models.project import Project
from project.services.project_service import ProjectService
from .project_test_data import ProjectFactory

@pytest.fixture
def sample_project_data():
    return ProjectFactory()

@pytest.mark.django_db
def test_list_projects_empty_db():
    # Ensure that calling list() on an empty database raises Http404
    with pytest.raises(Http404):
        ProjectService.list()

@pytest.mark.django_db
def test_list_projects_with_data(db, sample_project_data):
    # Call the list() method and ensure that at least one project is returned
    projects = ProjectService.list()
    assert len(projects) == 1

@pytest.mark.django_db
def test_create_project():
    # Create a sample project data dictionary
    project_data = {
        "title": "New Project",
        "description": "A new project",
        "is_active": True,
    }

    # Call the create() method to create a new project
    created_project = ProjectService.create(project_data)

    # Ensure that the project was created and exists in the database
    assert Project.objects.filter(id=created_project.id).exists()

@pytest.mark.django_db
def test_retrieve_existing_project(db, sample_project_data):
    # Call the retrieve() method with the ID of the created project
    retrieved_project = ProjectService.retrieve(sample_project_data.id)

    # Ensure that the retrieved project matches the created project
    assert retrieved_project == sample_project_data

@pytest.mark.django_db
def test_retrieve_nonexistent_project():
    # Call the retrieve() method with a non-existent ID
    with pytest.raises(Http404):
        ProjectService.retrieve(999)

@pytest.mark.django_db
def test_update_project(db, sample_project_data):
    # Define updated data
    updated_data = {
        "title": "Updated Project Title",
        "description": "Updated project description",
        "is_active": False,
    }

    # Call the update() method to update the project
    updated_project = ProjectService.update(sample_project_data, updated_data)

    # Reload the project from the database to get the latest data
    sample_project_data.refresh_from_db()

    # Ensure that the project has been updated with the new data
    assert updated_project == sample_project_data
    assert updated_project.title == updated_data["title"]
    assert updated_project.description == updated_data["description"]
    assert updated_project.is_active == updated_data["is_active"]
