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




# from django.urls import path
# from .views import (
#     DeliveryListView, 
#     DeliveryCreateView, 
#     DeliveryUpdateView, 
#     DeliveryDeleteView, 
#     DeliveryAPIView
# )

# app_name = 'delivery'  # اسم التطبيق (Namespace)

# urlpatterns = [
#     # صفحة عرض قائمة التوصيلات HTML
#     path('', DeliveryListView.as_view(), name='delivery_list'),                      # /delivery/
    
#     # صفحة إضافة توصيلة جديدة HTML
#     path('create/', DeliveryCreateView.as_view(), name='delivery_create'),            # /delivery/create/
    
#     # صفحة تعديل توصيلة موجودة HTML (تحتاج رقم التوصيلة pk)
#     path('<int:pk>/update/', DeliveryUpdateView.as_view(), name='delivery_update'),   # /delivery/1/update/
    
#     # صفحة تأكيد حذف توصيلة HTML (تحتاج رقم التوصيلة pk)
#     path('<int:pk>/delete/', DeliveryDeleteView.as_view(), name='delivery_delete'),   # /delivery/1/delete/
    
#     # واجهة الـ API لإرجاع وإضافة البيانات بصيغة JSON
#     path('api/', DeliveryAPIView.as_view(), name='delivery_api'),                    # /delivery/api/
# ]