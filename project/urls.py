from project import views
from django.urls import path

urlpatterns = [
    path('search/', views.ProjectListView.as_view(), name='project-list'),
    path('<int:id>/', views.ProjectDetailView.as_view(), name='project-detail')
]