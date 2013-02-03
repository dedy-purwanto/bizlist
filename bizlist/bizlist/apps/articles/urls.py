from django.conf.urls.defaults import patterns, url

from .views import ArticleListView, ArticleDetailView

urlpatterns = patterns('articles.views',
    url(r'^all/$', ArticleListView.as_view(), name='list'),
    url(r'^read/(?P<pk>\d+)/(?P<slug>[-\w]+)/$', ArticleDetailView.as_view(), name='detail'),

)
