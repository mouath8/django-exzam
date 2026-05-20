"""
ملف الـ Views لتطبيق delivery
يحتوي على:
  - صفحة HTML لعرض التوصيلات
  - صفحة HTML لإضافة / تعديل / حذف توصيلة
  - API View لإرجاع البيانات بصيغة JSON
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework.generics import ListCreateAPIView  # من مكتبة DRF
from .models import Delivery
from .serializers import DeliverySerializer


# ============================================
# صفحة HTML - عرض قائمة التوصيلات
# ============================================
@login_required  # يمنع غير المسجلين
def delivery_list(request):
    # جلب جميع التوصيلات من قاعدة البيانات
    deliveries = Delivery.objects.all()
    return render(request, 'delivery/delivery_list.html', {'deliveries': deliveries})


# ============================================
# صفحة HTML - إضافة توصيلة جديدة
# ============================================
@login_required
def delivery_create(request):
    if request.method == 'POST':  # عند إرسال النموذج
        # أخذ البيانات من النموذج
        delivery_person = request.POST.get('delivery_person')
        phone = request.POST.get('phone')
        order_id = request.POST.get('order_id')
        status = request.POST.get('status')

        # حفظ التوصيلة الجديدة
        Delivery.objects.create(
            delivery_person=delivery_person,
            phone=phone,
            order_id=order_id,
            status=status,
        )
        return redirect('delivery:delivery_list')  # روح للقائمة

    # عرض النموذج الفارغ
    return render(request, 'delivery/delivery_form.html')


# ============================================
# صفحة HTML - تعديل توصيلة موجودة
# ============================================
@login_required
def delivery_update(request, pk):
    delivery = get_object_or_404(Delivery, pk=pk)  # جيب التوصيلة أو أظهر خطأ 404

    if request.method == 'POST':  # عند إرسال النموذج
        # تحديث البيانات من النموذج
        delivery.delivery_person = request.POST.get('delivery_person')
        delivery.phone = request.POST.get('phone')
        delivery.order_id = request.POST.get('order_id')
        delivery.status = request.POST.get('status')
        delivery.save()  # احفظ التعديلات
        return redirect('delivery:delivery_list')

    # اعرض النموذج مع البيانات الحالية (للتعديل)
    return render(request, 'delivery/delivery_form.html', {'delivery': delivery})


# ============================================
# صفحة HTML - حذف توصيلة
# ============================================
@login_required
def delivery_delete(request, pk):
    delivery = get_object_or_404(Delivery, pk=pk)  # جيب التوصيلة أو أظهر خطأ 404

    if request.method == 'POST':  # تأكيد الحذف
        delivery.delete()          # احذف من قاعدة البيانات
        return redirect('delivery:delivery_list')

    # اعرض صفحة تأكيد الحذف
    return render(request, 'delivery/delivery_confirm_delete.html', {'delivery': delivery})


# ============================================
# API View - إرجاع البيانات بصيغة JSON
# الرابط: /delivery/api/
# ============================================
class DeliveryAPIView(ListCreateAPIView):
    """
    هذا الـ View يعمل شيئين:
      GET  → يعرض جميع التوصيلات بصيغة JSON
      POST → يضيف توصيلة جديدة عبر JSON
    """
    queryset = Delivery.objects.all()      # البيانات المطلوبة
    serializer_class = DeliverySerializer  # كيف نحوّلها إلى JSON
