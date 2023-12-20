from rest_framework import serializers
from panumbaweb.interface.models import AIcontact  

class AIcontactSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIcontact
        fields = ['answer', 'context', 'id', 'question']
