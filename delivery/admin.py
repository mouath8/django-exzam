# from django.contrib import admin
# from .models import Delivery

# # تسجيل نموذج التوصيل في لوحة الإدارة
# admin.site.register(Delivery)
from django.contrib import admin
from .models import Delivery

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    # عرض الحقول كجدول منظم في لوحة الإدارة
    list_display = ('order_id', 'delivery_person', 'phone', 'status', 'created_at')
    
    # # إضافة شريط جانبي لتصفية الطلبات بناءً على الحالة أو التاريخ
    # list_filter = ('status', 'created_at')
    
    # إضافة صندوق بحث يسهل عليك البحث باسم المندوب، رقمه، أو رقم الطلب
    search_fields = ('delivery_person', 'phone', 'order_id')
    
    # # ترتيب ظهور الصفوف بحيث يظهر أحدث طلب فوق دائماً
    # ordering = ('-created_at',)