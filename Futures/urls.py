from django.conf.urls import url 

from Futures import views
urlpatterns = [
    url(r'^api/getFutures$',views.FutureData_get),
    url(r'^api/getFuturesData',views.GetFutureData)
]