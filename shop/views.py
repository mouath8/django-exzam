"""
ملف الـ Views لتطبيق shop
يحتوي على طريقتين:
  ❌ الطريقة القديمة (FBV) - متروكة كـ Comment
  ✅ الطريقة الجديدة (CBV) - المستخدمة فعلياً
"""
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin  # للتأمين
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm


# ============================================
# ❌ الطريقة القديمة (Function-Based Views)
#    متروكة ككومنت - لا تُستخدم
# ============================================
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

def product_list(request):
    # جلب جميع المنتجات من قاعدة البيانات
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

@login_required
def product_create(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop:product_list')
    return render(request, 'shop/product_form.html', {'form': form})

@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('shop:product_list')
    return render(request, 'shop/product_form.html', {'form': form})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('shop:product_list')
    return render(request, 'shop/product_confirm_delete.html', {'product': product})
"""


# ============================================
# ✅ الطريقة الجديدة (Class-Based Views) - المستخدمة
# ============================================

class ProductListView(ListView):
    """
    عرض قائمة جميع المنتجات
    لا يحتاج login (يمكن للجميع رؤية المنتجات)
    """
    model = Product                           # من أي جدول نجيب البيانات
    template_name = 'shop/product_list.html'  # أي قالب نعرض
    context_object_name = 'products'          # اسم المتغير في القالب


class ProductCreateView(LoginRequiredMixin, CreateView):
    """
    إضافة منتج جديد
    LoginRequiredMixin = يمنع غير المسجلين من الوصول
    """
    model = Product
    form_class = ProductForm                  # النموذج المستخدم
    template_name = 'shop/product_form.html'
    success_url = reverse_lazy('shop:product_list')  # بعد الحفظ روح للقائمة
    login_url = '/accounts/login/'            # إذا مو مسجل روح هنا


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """
    تعديل منتج موجود
    """
    model = Product
    form_class = ProductForm
    template_name = 'shop/product_form.html'
    success_url = reverse_lazy('shop:product_list')
    login_url = '/accounts/login/'


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """
    حذف منتج
    """
    model = Product
    template_name = 'shop/product_confirm_delete.html'
    success_url = reverse_lazy('shop:product_list')
    login_url = '/accounts/login/'
