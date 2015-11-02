from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    ## ex: /newapp/5/
    url(r'^(?P<n>[0-9]+)/$', views.detail, name='detail'),
    ## ex: /newapp/5/results/
##    url(r'^(?P<n>[0-9]+)/results/$', views.results, name='results'),
##    ## ex: /newapp/5/vote/
##    url(r'^(?P<n>[0-9]+)/vote/$', views.vote, name='vote'),
]
