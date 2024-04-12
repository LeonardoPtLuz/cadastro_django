from django.urls import path
from . import views


urlpatterns = [
    path('', views.users_list, name='list_users'),
    path('user/add/', views.user_add, name='add_user'),
    path('user/<int:user_id>/', views.user_detail, name='detail_user'),
    path('user/<int:user_id>/edit/', views.user_edit, name='edit_user'),
    path('user/<int:user_id>/delete/', views.user_delete, name='delete_user')
]
