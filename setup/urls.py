
from django.conf.urls import url
from . import views as appviews

app_name = 'setup'

urlpatterns = [
    
    url(r'^$', appviews.IndexListView.as_view(), name='home'),
    url(r'^setup/$', appviews.CreateView.as_view(), name='create'),
    url(r'^setup/(?P<pk>[0-9]+)/$', appviews.EditView.as_view(), name='detail'),
]