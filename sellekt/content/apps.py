from django.apps import AppConfig


class ContentConfig(AppConfig):
    name = "sellekt.content"
    verbose_name = "Content"

    def ready(self):
        try:
            import sellekt.content.signals  # noqa F401
        except ImportError:
            pass
