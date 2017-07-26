from SZGLsys.urls import url
from app import views
# urlpatterns = [
#         url(r'^home/$',views.home,name= 'home'),
urlpatterns= [
    url(r'^home/$', views.home, name= 'cliente_home'),
    url(r'^login/$',views.login,name='login'),
    url(r'^apply1/$',views.apply1,name='apply1'),
    url(r'^index/$',views.index,name='index'),
    url(r'^archive/$',views.archive,name='archive'),
    url(r'^detail/$',views.detail,name='detail'),
    url(r'^comment/$',views.comment,name='comment'),
    # url(r'^uploads/(?P<path>.*)$',views.static.serve,),

# ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
]