from django.apps import AppConfig


class BlogPodcastConfig(AppConfig):
    name = "sellekt.blog_podcast"
    verbose_name = "Blog and Podcast"

    def ready(self):
        try:
            import sellekt.blog_podcast.signals  # noqa F401
        except ImportError:
            pass
