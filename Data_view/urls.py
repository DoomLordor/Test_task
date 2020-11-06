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

    path('TypeInstitutions/', views.TypeInstitutionsRest.as_view({'get': 'list', 'post': 'create'})),

    path('TypeInstitutions/<int:pk>/', views.TypeInstitutionsRest.as_view({'get': 'retrieve',
                                                                           'put': 'update',
                                                                           'patch': 'partial_update',
                                                                           'delete': 'destroy'})),

    path('TypeOrganizations/', views.TypeOrganizationsRest.as_view({'get': 'list', 'post': 'create'})),

    path('TypeOrganizations/<int:pk>/', views.TypeOrganizationsRest.as_view({'get': 'retrieve',
                                                                             'put': 'update',
                                                                             'patch': 'partial_update',
                                                                             'delete': 'destroy'})),

    path('StatusEGRUL/', views.StatusEGRULRest.as_view({'get': 'list', 'post': 'create'})),

    path('StatusEGRUL/<int:pk>/', views.StatusEGRULRest.as_view({'get': 'retrieve',
                                                                 'put': 'update',
                                                                 'patch': 'partial_update',
                                                                 'delete': 'destroy'})),

    path('StatusRYBPNYBP/', views.StatusRYBPNYBPRest.as_view({'get': 'list', 'post': 'create'})),

    path('StatusRYBPNYBP/<int:pk>/', views.StatusRYBPNYBPRest.as_view({'get': 'retrieve',
                                                                       'put': 'update',
                                                                       'patch': 'partial_update',
                                                                       'delete': 'destroy'})),

    path('IndustrySpecificTyping/', views.IndustrySpecificTypingRest.as_view({'get': 'list', 'post': 'create'})),

    path('IndustrySpecificTyping/<int:pk>/', views.IndustrySpecificTypingRest.as_view({'get': 'retrieve',
                                                                                       'put': 'update',
                                                                                       'patch': 'partial_update',
                                                                                       'delete': 'destroy'})),

]
