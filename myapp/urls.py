from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from myapp import views as core_views
from myapp import views



app_name ='myapp'

urlpatterns=[
    url(r'fts',views.fts,name='files'),
    url(r'^$',views.base,name='base'),
    url(r'^upload/',views.upload,name='upload'),
    url(r'^login/',views.login1, name='login'),
    url(r'^logout/$',views.logout1, name='logout'),
    url(r'^registeration/', core_views.signup, name='registeration'),
    url(r'^download/(?P<filename>.+)$',views.download, name='download'),
    url(r'^api/',include('myapp.api.urls',namespace='user1-api'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
