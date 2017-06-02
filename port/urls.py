from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'index/$',views.index),
    url(r'porttest/$',views.porttest),
    url(r'code/$',views.code),
    url(r'search_name/$',views.search_name),
    url(r'editcode/(?P<code_id>[0-9]+)/$',views.editcode),
    url(r'codedetail/(?P<code_id>[0-9]+)/$',views.codedetail),
]