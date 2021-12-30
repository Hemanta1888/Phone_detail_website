from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home_view.as_view(),name = 'home'),
    path('temp',views.template_view.as_view(),name="template"),
    path('phone',views.default_list_view.as_view(),name="phone"),
    path('phonelist',views.custom_listView.as_view(),name='phonelist'),
    path('phonedetail/<int:pk>',views.details_view.as_view(),name="details")
]