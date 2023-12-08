from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.
from .models import AIcontact



class AIcontactListView(ListView):
    model = AIcontact
    template_name = "interface/panumba_list.html"
    context_object_name = "AIcontacts"
    ordering = ["id"]
    paginate_by = 10
    paginate_orphans = 5
    allow_empty_first_page = True
    queryset = AIcontact.objects.all()


