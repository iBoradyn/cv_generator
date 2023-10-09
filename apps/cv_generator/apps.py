"""CV generator apps."""
# Django
from django.apps import AppConfig


class CvGeneratorConfig(AppConfig):  # noqa: D101
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.cv_generator'
