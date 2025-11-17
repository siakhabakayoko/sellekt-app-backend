from django.shortcuts import render
from rest_framework import viewsets, permissions
from newsletter.models import Subscription
from .serializers import NewsletterSubscriptionSerializer

# Create your views here.

class NewsletterSubscriptionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing newsletter subscriptions
    """
    queryset = Subscription.objects.all()
    serializer_class = NewsletterSubscriptionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
