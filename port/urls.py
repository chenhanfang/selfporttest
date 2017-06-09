from django.conf.urls import url
from . import views,views2


urlpatterns = [
    url(r'index/$',views.index),
    url(r'code/$',views.code),
    url(r'search_name/$',views.search_name),
    url(r'editcode/(?P<code_id>[0-9]+)/$',views.editcode),
    url(r'codedetail/(?P<code_id>[0-9]+)/$',views.codedetail),
    url(r'editaction$',views.editaction),
    url(r'porttest/$',views2.porttest),
    url('codedelete/(?P<code_id>[0-9]+)/$',views.codedelete),

]