from rest_framework import serializers
from newsletter.models import Subscription

class NewsletterSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'email_field', 'name_field', 'subscribed', 'subscribe_date', 'unsubscribe_date']
        read_only_fields = ['id', 'subscribe_date', 'unsubscribe_date']
