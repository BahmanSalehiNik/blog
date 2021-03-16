
from django.urls import path
from .views import post_model_list_view, post_model_detail_view,\
    post_model_create_view, post_model_update_view, post_model_delete_view,\
    temp_test

urlpatterns = [

    path('', post_model_list_view, name='list'),
    path('<int:id>', post_model_detail_view, name='detail'),
    path('create/', post_model_create_view, name='create'),
    path('<int:id>/edit/', post_model_update_view, name='update'),
    path('<int:id>/delete/', post_model_delete_view, name='delete'),
    path('test/', temp_test, name='temp_test')

]
