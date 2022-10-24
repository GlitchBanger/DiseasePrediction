from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<uuid:id>/', views.user, name='user'),
    path('signup/', views.signup, name='signup'),
    path('test/<uuid:id>/', views.test, name='test'),
    path('result/<uuid:id>/', views.result, name='result'),
    path('records/<uuid:id>/', views.records, name='records'),
]
