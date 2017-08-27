from django.conf.urls import include, url
from myapp.api.views import User1View,User1DetailView,User1LoginView

app_name ='myapp'

urlpatterns=[


    url(r'^$',User1View.as_view(),name='user'),
#     url(r'^upload/',views.upload,name='upload'),
     url(r'^login/',User1LoginView.as_view(), name='login'),
#     url(r'^logout/$',views.logout1, name='logout'),
#     url(r'^registeration/', core_views.signup, name='registeration'),
    # url(r'^(?P<job>.+)$',User1DetailView.as_view(), name='download'),
]

