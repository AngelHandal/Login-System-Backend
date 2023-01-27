from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_login),
    path('check_login', views.check_login, name='check_login'),
    path('mypage', views.mypage, name='mypage'),
    path('mypage_logout', views.mypage_logout, name='mypage_logout')

    
]
