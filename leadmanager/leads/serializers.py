from rest_framework import serializers
from .models import Lead  # same folder's model hence . is required

# Lead Serializer


# it will turning our lead model into a serializer
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        #fields = ['name', 'email', 'message']
        fields = '__all__'
