"""
ملف النماذج (Models) لتطبيق delivery
هنا نصمم جدول بيانات التوصيل في قاعدة البيانات
"""
from django.db import models


class Delivery(models.Model):
    """
    نموذج التوصيل - يحتوي بيانات كل عملية توصيل
    """
    # خيارات حالة التوصيل
    STATUS_CHOICES = [
        ('pending', 'قيد الانتظار'),
        ('in_progress', 'جاري التوصيل'),
        ('delivered', 'تم التوصيل'),
        ('cancelled', 'ملغي'),
    ]

    delivery_person = models.CharField(max_length=100, verbose_name='اسم المندوب')  # اسم المندوب
    phone = models.CharField(max_length=20, verbose_name='رقم الهاتف')              # رقم الهاتف
    order_id = models.IntegerField(verbose_name='رقم الطلب')                        # رقم الطلب
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,      # يستخدم الخيارات أعلاه
        default='pending',           # الحالة الافتراضية: قيد الانتظار
        verbose_name='الحالة'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')

    def __str__(self):
        # كيف يظهر اسم التوصيلة في الإدارة
        return f"طلب #{self.order_id} - {self.delivery_person}"

    class Meta:
        verbose_name = 'توصيلة'
        verbose_name_plural = 'التوصيلات'
        ordering = ['-created_at']
