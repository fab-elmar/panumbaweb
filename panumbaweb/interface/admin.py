from django.contrib import admin, messages

# Register your models here.
from .models import AIcontact, SendToCCC



@admin.register(AIcontact)
class AIcontactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "question", "answer", "context")
    list_filter = ("id", "name", "question", "answer", "context")
    search_fields = ("id", "name", "question", "answer", "context")
    ordering = ("id", "name", "question", "answer", "context")
    
    class Meta:
        model = AIcontact
        
        
        
@admin.register(SendToCCC)
class SendToCCCDisplayAdmin(admin.ModelAdmin):
    list_display = ( "ip", "red", "green", "blue", "token")
    list_filter = ( "ip",  "red", "green", "blue", "token")
   
    def add_view(self, request, form_url='', extra_context=None):
        url = f'http://<ip>/number?n=<number>&r=<red>&g=<green>&b=<blue>&token=<token>'
        messages.info(request, 'The URL will be: ' + url)
        return super().add_view(request, form_url, extra_context)
    class Meta:
        model = SendToCCC