from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
    path('ecg/', TemplateView.as_view(template_name="ecg.html"), name='ecg'),
    path('rf/', TemplateView.as_view(template_name="rf.html"), name='rf'),
    path('portfolio/', TemplateView.as_view(template_name="portfolio.html"), name='portfolio'),
    path('circuit-solver/', TemplateView.as_view(template_name="circuit-solver.html"), name='circuit-solver'),
    path('tracker/', TemplateView.as_view(template_name="tracker.html"), name='tracker'),
    path('planner/', TemplateView.as_view(template_name="planner.html"), name='planner'),
    path('debug/', TemplateView.as_view(template_name="debug.html"), name='debug'),
]

# Add these lines at the very bottom
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
