from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^MerchandiseExports/([a-zA-Z0-9,]*)/$', views.showMerchandiseData),
    url(r'^MerchandiseExports/([a-zA-Z0-9,]+)/([a-zA-Z0-9,]+)$', views.showMerchandiseData),
    url(r'^Retail/([a-zA-Z0-9,]*)/$', views.showRetailData),
    url(r'^Retail/([a-zA-Z0-9,]+)/([a-zA-Z0-9,]+)$', views.showRetailData),
    # Add proper routing to the view
    # doc should be in Django website
]
