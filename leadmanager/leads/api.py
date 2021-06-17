from rest_framework import viewsets, permissions
from .models import Lead  # same folder's model hence . is required
from .serializers import LeadSerializer

#Lead Viewset
class LeadViewset(viewsets.ModelViewSet):
    queryset = Lead.objects.all(); # grab all the leads from leads table
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer