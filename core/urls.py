from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
    path('ecg/', TemplateView.as_view(template_name="ecg.html"), name='ecg'),
    path('rf/', TemplateView.as_view(template_name="rf.html"), name='rf'),
    path('emotion/', TemplateView.as_view(template_name="emotion.html"), name='emotion'),
    path('resetguard/', TemplateView.as_view(template_name="resetguard.html"), name='resetguard'),
    path('robotics/', TemplateView.as_view(template_name="robotics.html"), name='robotics'),

]

# Add these lines at the very bottom
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
