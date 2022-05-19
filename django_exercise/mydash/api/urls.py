from django.urls import path
from .views import msg_list
from rest_framework.authtoken import views     # to use obtain_auth_token view 


urlpatterns = [
    path('', msg_list, name="list"),
    path('api-token-auth/', views.obtain_auth_token)  #for generating tokens
]