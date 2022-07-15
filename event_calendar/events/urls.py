from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('/sign-up', views.sign_up, name='signup'),
    path('/login', views.log_in, name='login'),
    path('/new', views.new_event, name='new'),
    path('/<int:id>/edit', views.edit, name='edit'),
    path('/<int:id>/delete', views.delete_event, name='delete'),
    path('/<int:id>', views.detail, name='detail'),
    path('/logout', views.log_out, name='logout'),
]