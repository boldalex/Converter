from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.show),
    url(r'^redirector/$', views.convert_redirector, name="redirector"),
    url(r'^(?P<from_code>[A-Z]{3})/'
        r'to/(?P<to_code>[A-Z]{3})/'
        r'in/(?P<method>(text|json|html))/$', views.convert, name="convert")
    ]