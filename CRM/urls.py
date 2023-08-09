from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    # path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path('register/', views.register_user, name="register"),
    path('addRecord/', views.CreateRecord, name='add-record'),
    path('record/<str:pk>/', views.costumer_record, name="c_record"),
    path('edit-record/<str:pk>/', views.edit_record, name="edit-record"),
    path('delete-record/<str:pk>/', views.delete_record, name="delete-record"),

]


