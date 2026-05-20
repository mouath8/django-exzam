# from django.contrib import admin
# from .models import Product

# # تسجيل نموذج المنتج في لوحة الإدارة
# admin.site.register(Product)

from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # عرض الحقول الأساسية في جدول المنتجات
    list_display = ('name', 'price', 'created_at')
    
    # # إضافة فلاتر جانبية لتصفية المنتجات حسب تاريخ الإضافة
    # list_filter = ('created_at',)
    
    # تفعيل البحث باسم المنتج أو حتى تفاصيل الوصف الخاص به
    search_fields = ('name', 'description')
    
    # # جعل حقل السعر قابلاً للتعديل مباشرة من جدول العرض دون الحاجة لدخول صفحة المنتج
    # list_editable = ('price',)