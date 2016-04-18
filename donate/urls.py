from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

#from django.contrib import admin

from .views import DonateView, SuccessView

urlpatterns = [
    #url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    #url(r"^admin/", include(admin.site.urls)),
    url(r"^$", DonateView.as_view(template_name="donate.html"), name='home'),

    url(r'^donate/$', DonateView.as_view(template_name="donate.html"), name='donate'),
    url(r'^thank_you/$', SuccessView.as_view(), name='thank_you'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
