from django.conf.urls import url 

from ForeignInvestorsOption import views
urlpatterns = [
    url(r'^api/getForeignInvestorsOption$',views.ForeignInvestorsOption_get),
    url(r'^api/getForeignInvestorsOptionData$',views.GetForeignOptionData),

]