from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.collect_user_data_view, name='collect_user_data_view'),
    path('home/<int:user_data_id>/', views.test_list, name='home'),
    path('test/<int:test_id>/<int:user_data_id>/', views.test_detail, name='test_detail'),
]
urlpatterns += staticfiles_urlpatterns()
