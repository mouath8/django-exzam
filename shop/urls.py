"""
ملف المسارات (URLs) لتطبيق shop
"""
from django.urls import path
from .views import (
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = 'shop'  # اسم التطبيق (للـ namespace)

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),           # /shop/
    path('create/', ProductCreateView.as_view(), name='product_create'), # /shop/create/
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'), # /shop/1/update/
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'), # /shop/1/delete/
]


# ============================================
# ❌ الطريقة القديمة (Function-Based Views)
#    متروكة ككومنت - لا تُستخدم
# ============================================

# from django.urls import path
# from .views import (
# product_list, product_create, product_update, product_delete
# )

# app_name = 'shop'  # اسم التطبيق (للـ namespace)

# urlpatterns = [
#     path('', product_list, name='product_list'),           # /shop/
#     path('create/', product_create, name='product_create'), # /shop/create/
#     path('<int:pk>/update/', product_update, name='product_update'), # /shop/1/update/
#     path('<int:pk>/delete/', product_delete, name='product_delete'), # /shop/1/delete/
# ]