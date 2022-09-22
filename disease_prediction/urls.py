from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<uuid:id>/', views.user, name='user'),
    path('signup/', views.signup, name='signup'),
]
