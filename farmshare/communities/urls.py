from django.conf.urls import url 
from . import views

app_name = 'communities'

urlpatterns = [
    url(r'^$', views.ListCommunities.as_view(), name="all"), 
    url(r'^new/$', views.CreateCommunity.as_view(), name="create"), 
    url(r"^posts/in/(?P<slug>[-\w]+)/$", views.SingleCommunity.as_view(), name="single"),
    url(r'join/(?P<slug>[-\w]+)/$', views.JoinCommunity.as_view(), name = "join"), 
    url(r'leave/(?P<slug>[-\w]+)/$', views.LeaveCommunity.as_view(), name = "leave"),
] 