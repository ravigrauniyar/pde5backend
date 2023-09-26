from project.views import project_views, source_views, event_views
from django.urls import path

urlpatterns = [
    path('events/', event_views.EventListView.as_view(), name='event-list'),
    path('events/<int:id>/', event_views.EventDetailView.as_view(), name='event-detail'),
    path('events/<str:key>/', event_views.EventCreateView.as_view(), name='event-create'),
    path('<int:project_id>/', project_views.ProjectDetailView.as_view(), name='project-detail'),
    path('<int:project_id>/sources/', source_views.SourceListView.as_view(), name='source-list'),
    path('<int:project_id>/sources/<int:source_id>/', source_views.SourceDetailView.as_view(), name='source-detail'),
    path('search/', project_views.ProjectListView.as_view(), name='project-list'),
]