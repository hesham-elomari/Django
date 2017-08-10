from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from Task1.myapp import views as core_views

app_name ='myapp'

urlpatterns=[
    url(r'^login/$', auth_views.login,{'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout,{'next_page': 'login.html'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
