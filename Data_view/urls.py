from django.urls import path

from . import views

urlpatterns = [
    path('Data/', views.DataRest.as_view({'get': 'list', 'post': 'create'})),

    path('Data/<int:pk>/', views.DataRest.as_view({'get': 'retrieve',
                                                   'put': 'update',
                                                   'patch': 'partial_update',
                                                   'delete': 'destroy'})),

    path('HeadByBK/', views.HeadByBKRest.as_view({'get': 'list', 'post': 'create'})),

    path('HeadByBK/<int:pk>/', views.HeadByBKRest.as_view({'get': 'retrieve',
                                                           'put': 'update',
                                                           'patch': 'partial_update',
                                                           'delete': 'destroy'})),
]
