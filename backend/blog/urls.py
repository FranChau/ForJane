from django.urls import path
from blog import views
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'article'

urlpatterns = [
    url('list/', views.article_list, name='list'),
    url('(?P<pk>[0-9]+)/$', views.article_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)