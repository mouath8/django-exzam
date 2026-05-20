"""
ملف النماذج (Forms) لتطبيق shop
ModelForm = نموذج مبني تلقائياً من الـ Model
"""
from django import forms
from .models import Product  # استيراد نموذج المنتج


class ProductForm(forms.ModelForm):
    """
    نموذج المنتج - يأخذ حقوله من Model مباشرة
    """
    class Meta:
        model = Product                                    # النموذج المرتبط
        fields = ['name', 'price', 'description']         # الحقول المطلوبة
        labels = {
            'name': 'اسم المنتج',
            'price': 'السعر',
            'description': 'الوصف',
        }
        widgets = {
            # تخصيص مظهر حقل الوصف
            'description': forms.Textarea(attrs={'rows': 3}),
        }
