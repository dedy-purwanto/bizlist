from django.conf.urls.defaults import patterns, url

from .views import CompanyListView

urlpatterns = patterns('home.views',
    url(r'^myanmar-burma-companies/(?P<state>[-\w]+)/(?P<category>[-\w]+)/(?P<sub_category>[-\w]+)/$', CompanyListView.as_view(), name='company_list'),

)
