from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Customer, Contact, Opportunity, Task, Note, Lead
from .serializers import (
    CustomerSerializer,
    ContactSerializer,
    OpportunitySerializer,
    TaskSerializer,
    NoteSerializer,
    LeadSerializer
)
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing customers.

    list:
    Return a list of all customers.

    create:
    Create a new customer.

    retrieve:
    Return the details of a specific customer.

    update:
    Update all fields of a specific customer.

    partial_update:
    Update one or more fields of a specific customer.

    destroy:
    Delete a specific customer.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing contacts.

    list:
    Return a list of all contacts.

    create:
    Create a new contact.

    retrieve:
    Return the details of a specific contact.

    update:
    Update all fields of a specific contact.

    partial_update:
    Update one or more fields of a specific contact.

    destroy:
    Delete a specific contact.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]

class OpportunityViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing opportunities.

    list:
    Return a list of all opportunities.

    create:
    Create a new opportunity.

    retrieve:
    Return the details of a specific opportunity.

    update:
    Update all fields of a specific opportunity.

    partial_update:
    Update one or more fields of a specific opportunity.

    destroy:
    Delete a specific opportunity.
    """
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer
    permission_classes = [permissions.IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing tasks.

    list:
    Return a list of all tasks.

    create:
    Create a new task.

    retrieve:
    Return the details of a specific task.

    update:
    Update all fields of a specific task.

    partial_update:
    Update one or more fields of a specific task.

    destroy:
    Delete a specific task.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

class NoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing notes.

    list:
    Return a list of all notes.

    create:
    Create a new note.

    retrieve:
    Return the details of a specific note.

    update:
    Update all fields of a specific note.

    partial_update:
    Update one or more fields of a specific note.

    destroy:
    Delete a specific note.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

class LeadViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing leads.

    list:
    Return a list of all leads.

    create:
    Create a new lead.

    retrieve:
    Return the details of a specific lead.

    update:
    Update all fields of a specific lead.

    partial_update:
    Update one or more fields of a specific lead.

    destroy:
    Delete a specific lead.
    """
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
