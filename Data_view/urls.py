from django.urls import path

from . import views

LIST_VIEW_METHODS = {'get': 'list', 'post': 'create'}
object_OBJECT_VIEW_METHODS = {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}

urlpatterns = [
    path('Data/', views.CharacteristicsOrganizationRest.as_view(LIST_VIEW_METHODS)),
    path('Data/<int:pk>/', views.CharacteristicsOrganizationRest.as_view(object_OBJECT_VIEW_METHODS)),

    path('HeadByBK/', views.HeadByBKRest.as_view(LIST_VIEW_METHODS)),
    path('HeadByBK/<int:pk>/', views.HeadByBKRest.as_view(object_OBJECT_VIEW_METHODS)),

    path('TypeInstitutions/', views.TypeInstitutionRest.as_view(LIST_VIEW_METHODS)),
    path('TypeInstitutions/<int:pk>/', views.TypeInstitutionRest.as_view(object_OBJECT_VIEW_METHODS)),

    path('TypeOrganizations/', views.TypeOrganizationRest.as_view(LIST_VIEW_METHODS)),
    path('TypeOrganizations/<int:pk>/', views.TypeOrganizationRest.as_view(object_OBJECT_VIEW_METHODS)),

    path('StatusEGRUL/', views.StatusEGRULRest.as_view(LIST_VIEW_METHODS)),
    path('StatusEGRUL/<int:pk>/', views.StatusEGRULRest.as_view(object_OBJECT_VIEW_METHODS)),

    path('StatusRYBPNYBP/', views.StatusRYBPNYBPRest.as_view(LIST_VIEW_METHODS)),
    path('StatusRYBPNYBP/<int:pk>/', views.StatusRYBPNYBPRest.as_view(object_OBJECT_VIEW_METHODS)),

    path('IndustrySpecificTyping/', views.IndustrySpecificTypingRest.as_view(LIST_VIEW_METHODS)),
    path('IndustrySpecificTyping/<int:pk>/', views.IndustrySpecificTypingRest.as_view(object_OBJECT_VIEW_METHODS)),

]
