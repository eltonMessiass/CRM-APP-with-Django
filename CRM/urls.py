from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    # path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path('register/', views.register_user, name="register"),\
    path('addRecord/', views.CreateRecord, name='add-record')

]


