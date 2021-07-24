from django.conf.urls import url ,include 
from users.views import LoginView
from users.views import RegisterView
from users import views
urlpatterns = [ 
    url(r'^api/users$',views.users_list),
    url(r'^api/login$', LoginView.as_view()),
    url(r'^api/register$',RegisterView.as_view()) 
]