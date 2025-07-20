from django.urls import path
from . import views
from .views import edit_profile, delete_profile

urlpatterns = [
    path('', views.home, name='home'),
    path('profiles/', views.profile_list, name='profile_list'),
    path('api/profiles/', views.api_profile_list, name='api_profile_list'),  # New API endpoint
    path('edit/<int:pk>/', edit_profile, name='edit_profile'),
    path('delete/<int:pk>/', delete_profile, name='delete_profile'),
    path('api/', views.api_overview),
    path('api/profiles/', views.profile_list_api),
    path('api/profiles/<int:id>/', views.profile_detail_api),
    path('api/profiles/create/', views.profile_create_api),
    path('api/profiles/update/<int:id>/', views.profile_update_api),
    path('api/profiles/delete/<int:id>/', views.profile_delete_api),
]
