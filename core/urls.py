from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    # The main homepage
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
    
    # Your project pages
    path('ecg/', TemplateView.as_view(template_name="ecg.html"), name='ecg'),
    path('rf/', TemplateView.as_view(template_name="rf.html"), name='rf'),
    path('portfolio/', TemplateView.as_view(template_name="portfolio.html"), name='portfolio'),
    
    # Don't forget to map the rest of your project pages too!
    path('circuit-solver/', TemplateView.as_view(template_name="circuit-solver.html"), name='circuit-solver'),
    path('tracker/', TemplateView.as_view(template_name="tracker.html"), name='tracker'),
    path('planner/', TemplateView.as_view(template_name="planner.html"), name='planner'),
    path('debug/', TemplateView.as_view(template_name="debug.html"), name='debug'),
]