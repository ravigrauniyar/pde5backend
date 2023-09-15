from project.views import project_views, source_views
from django.urls import path

urlpatterns = [
    path('<int:id>/', project_views.ProjectDetailView.as_view(), name='project-detail'),
    path('search/', project_views.ProjectListView.as_view(), name='project-list'),
    path('sources/', source_views.SourceListView.as_view(), name='source-list'),
    path('sources/<int:id>/', source_views.SourceDetailView.as_view(), name='source-detail'),
]