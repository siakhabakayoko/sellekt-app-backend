from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from sellekt.users.api.views import UserViewSet
from newsletter_api.views import NewsletterSubscriptionViewSet
from crm_api.views import (
    CustomerViewSet,
    ContactViewSet,
    OpportunityViewSet,
    TaskViewSet,
    NoteViewSet
)

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("newsletter", NewsletterSubscriptionViewSet, basename="newsletter")
router.register("crm/customers", CustomerViewSet)
router.register("crm/contacts", ContactViewSet)
router.register("crm/opportunities", OpportunityViewSet)
router.register("crm/tasks", TaskViewSet)
router.register("crm/notes", NoteViewSet)

app_name = "api"
urlpatterns = router.urls
