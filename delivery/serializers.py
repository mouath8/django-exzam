"""
ملف الـ Serializers لتطبيق delivery
الـ Serializer = يحوّل بيانات قاعدة البيانات إلى JSON
مثل: بيانات التوصيل → { "id": 1, "delivery_person": "أحمد", ... }
"""
from rest_framework import serializers  # مكتبة DRF
from .models import Delivery             # نموذج التوصيل


class DeliverySerializer(serializers.ModelSerializer):
    """
    Serializer للتوصيل
    ModelSerializer = يأخذ الحقول تلقائياً من الـ Model
    """
    class Meta:
        model = Delivery        # النموذج المرتبط
        fields = '__all__'      # عرض جميع الحقول
