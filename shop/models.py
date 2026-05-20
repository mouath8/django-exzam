"""
ملف النماذج (Models) لتطبيق shop
هنا نصمم جدول المنتجات في قاعدة البيانات
"""
from django.db import models


class Product(models.Model):
    """
    نموذج المنتج - كل سطر هو عمود في قاعدة البيانات
    """
    name = models.CharField(max_length=200, verbose_name='اسم المنتج')    # اسم المنتج
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='السعر')  # السعر
    description = models.TextField(blank=True, verbose_name='الوصف')       # وصف اختياري
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإضافة')  # تاريخ تلقائي

    def __str__(self):
        # هذا يحدد كيف يظهر اسم المنتج في الإدارة
        return self.name

    class Meta:
        verbose_name = 'منتج'
        verbose_name_plural = 'المنتجات'
        ordering = ['-created_at']  # ترتيب من الأحدث للأقدم
