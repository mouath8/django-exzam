"""
ملف النماذج (Forms) لتطبيق accounts
هنا نصمم نموذج تسجيل المستخدم الجديد
"""
from django import forms
from django.contrib.auth.models import User          # نموذج المستخدم الجاهز من Django
from django.contrib.auth.forms import UserCreationForm  # نموذج إنشاء مستخدم جاهز

class RegisterForm(UserCreationForm):
    """
    نموذج التسجيل - يرث من UserCreationForm الجاهز
    أضفنا حقل البريد الإلكتروني فقط
    """
    email = forms.EmailField(
        required=True,         # حقل مطلوب
        label='البريد الإلكتروني'
    )

    class Meta:
        model = User           # النموذج المرتبط: المستخدم
        fields = ['username', 'email', 'password1', 'password2']  # الحقول المطلوبة
        labels = {
            'username': 'اسم المستخدم',
        }
