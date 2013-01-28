from django.conf.urls.defaults import patterns, url

from .views import CompanyListView, CompanyDetailView

urlpatterns = patterns('companies.views',
    url(r'^myanmar-burma-companies/(?P<state>[-\w]+)/(?P<category>[-\w]+)/(?P<sub_category>[-\w]+)/$', CompanyListView.as_view(), name='company_list'),
    url(r'^(?P<company_slug>[-\w]+)/$', CompanyDetailView.as_view(), name='company_detail'),

)
