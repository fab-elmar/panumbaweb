from django.shortcuts import render

# Create your views here.
class InterFaceView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "InterFace"
        return context
    