from django.contrib import admin

# Register your models here.
from .models import AIcontact



@admin.register(AIcontact)
class AIcontactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "question", "answer", "context")
    list_filter = ("id", "name", "question", "answer", "context")
    search_fields = ("id", "name", "question", "answer", "context")
    ordering = ("id", "name", "question", "answer", "context")
    
    class Meta:
        model = AIcontact