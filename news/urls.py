from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template 


urlpatterns = patterns('news.views',
    (r'^(?P<id>\d+[a-z]*)/', 'article'),
)