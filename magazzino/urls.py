from django.conf.urls import patterns, url

from magazzino import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^classi/$', views.classedimateriale_index, name='classedimateriale_index'),
    url(r'^classi/(?P<cdm_sigla>[A-Z]+)', views.classedimateriale_detail, name='classedimateriale_detail'),
    url(r'^cerca/$', views.classedimateriale_search, name='classedimateriale_search'),
    url(r'^materiale-in-cassa/(?P<pk>\d+)/$', views.MaterialeInCassaDetailView.as_view(), name='materialeincassa-detail'),
    url(r'^materiale-in-cassa/(?P<pk>\d+)/edit$', views.MaterialeInCassaUpdate.as_view(), name='materialeincassa_update'),
)
