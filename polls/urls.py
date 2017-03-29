
from django.conf.urls import include, url
from . import views
urlpatterns = [
   
    url(r'^$',views.home,name='home'),
     #url(r'^',social.apps.django_app.urls),
     url('^oauth/', include('social.apps.django_app.urls', namespace='social')),
      url(r'^signup/$',views.signup,name='signup'),
       url(r'^login/$',views.login,name='login'),
    #url(r'^create/$',views.create,name='create'),^address_edit/(\d+)/$
     #url(r'^edit/(\d+)/$',views.edit,name='edit'),

     
     #url(r'^delete/(\d+)/$',views.delete,name='delete'),
     #url(r'^update/$',views.update,name='update'),
]