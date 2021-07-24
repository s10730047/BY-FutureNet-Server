from django.conf.urls import url 

from eps import views
urlpatterns = [ 
    url(r'^api/getEps$',views.eps_get),
]
# from Futures import views
# urlpatterns = [
#     url(r'^api/getFutures$',views.FutureData_get),
# ]