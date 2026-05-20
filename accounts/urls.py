"""
ملف المسارات (URLs) لتطبيق accounts
"""
from django.urls import path
from . import views  # استيراد الدوال من views.py

app_name = 'accounts'  # اسم التطبيق (للـ namespace)

urlpatterns = [
    path('login/', views.login_view, name='login'),        # /accounts/login/
    path('logout/', views.logout_view, name='logout'),     # /accounts/logout/
    path('register/', views.register_view, name='register'), # /accounts/register/
]
