from django.apps import AppConfig

class ProjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project'

    # Register signal to the app to ensure associated code is executed
    def ready(self):
        import project.signals