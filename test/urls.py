"""
ملف التوجيه الرئيسي
هنا نربط كل تطبيق بمساره على الموقع
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),                    # لوحة الإدارة
    path('accounts/', include('accounts.urls')),         # مسارات المستخدمين
    path('shop/', include('shop.urls')),                 # مسارات المنتجات
    path('delivery/', include('delivery.urls')),         # مسارات التوصيل
    path('', include('shop.urls')),                     # الصفحة الرئيسية → المنتجات
]
