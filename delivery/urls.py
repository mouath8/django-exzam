"""
ملف المسارات (URLs) لتطبيق delivery
"""
from django.urls import path
from .views import delivery_list, delivery_create, delivery_update, delivery_delete, DeliveryAPIView

app_name = 'delivery'  # اسم التطبيق

urlpatterns = [
    path('', delivery_list, name='delivery_list'),                      # /delivery/
    path('create/', delivery_create, name='delivery_create'),           # /delivery/create/
    path('<int:pk>/update/', delivery_update, name='delivery_update'),  # /delivery/1/update/
    path('<int:pk>/delete/', delivery_delete, name='delivery_delete'),  # /delivery/1/delete/
    path('api/', DeliveryAPIView.as_view(), name='delivery_api'),       # /delivery/api/ → JSON
]
