import pytest
from django.http import Http404
from project.models.source import Source
from project.services.source_service import SourceService
from tests.test_source.source_test_data import SourceFactory
from tests.test_project.project_test_data import ProjectFactory

@pytest.fixture
def sample_source_data():
    return SourceFactory()

@pytest.mark.django_db
def test_list_sources_empty_db():
    # Ensure that calling list() on an empty database raises Http404
    with pytest.raises(Http404):
        SourceService.list()

@pytest.mark.django_db
def test_list_sources_with_data(db, sample_source_data):
    # Call the list() method and ensure that at least one project is returned
    sources = SourceService.list()
    assert len(sources) == 2 # While calling the source factory project factory is called which create a new source

@pytest.mark.django_db
def test_source_created_after_project_is_created(db):
    ProjectFactory()
    source = SourceService.list()
    assert len(source) == 1

@pytest.mark.django_db
def test_create_source():
    project = ProjectFactory()
    # Create a sample project data dictionary
    source_data = {
        "name": "New Source",
        "description": "A new source",
        "tag": "random-tag",
        "project_id": project.id
    }

    # Call the create() method to create a new project
    created_source = SourceService.create(source_data)

    # Ensure that the project was created and exists in the database
    assert Source.objects.filter(id=created_source.id).exists()

@pytest.mark.django_db
def test_retrieve_existing_source(db, sample_source_data):
    # Call the retrieve() method with the ID of the created project
    retrieved_source = SourceService.retrieve(sample_source_data.id)

    # Ensure that the retrieved project matches the created project
    assert retrieved_source == sample_source_data

@pytest.mark.django_db
def test_retrieve_nonexistent_source():
    # Call the retrieve() method with a non-existent ID
    with pytest.raises(Http404):
        SourceService.retrieve(999)
