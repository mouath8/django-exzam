"""
ملف الـ Views لتطبيق accounts
هنا نكتب دوال تسجيل الدخول والخروج وإنشاء الحساب
كل الدوال هنا FBV (Function-Based Views)
"""
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate  # دوال جاهزة من Django
from django.contrib.auth.forms import AuthenticationForm      # نموذج تسجيل الدخول الجاهز
from .forms import RegisterForm                               # نموذج التسجيل اللي صممناه


# ============================================
# دالة تسجيل الدخول
# ============================================
def login_view(request):
    # إذا كان المستخدم مسجل أصلاً → روح للمنتجات مباشرة
    if request.user.is_authenticated:
        return redirect('shop:product_list')

    form = AuthenticationForm()  # النموذج الجاهز من Django

    if request.method == 'POST':  # عند الضغط على زر "تسجيل دخول"
        form = AuthenticationForm(data=request.POST)  # خذ البيانات من النموذج
        if form.is_valid():  # إذا البيانات صحيحة
            user = form.get_user()   # جيب المستخدم
            login(request, user)     # سجل دخوله
            return redirect('shop:product_list')  # روح لصفحة المنتجات

    # اعرض صفحة تسجيل الدخول
    return render(request, 'accounts/login.html', {'form': form})


# ============================================
# دالة إنشاء حساب جديد
# ============================================
def register_view(request):
    form = RegisterForm()  # نموذج التسجيل اللي صممناه

    if request.method == 'POST':  # عند الضغط على زر "إنشاء حساب"
        form = RegisterForm(request.POST)  # خذ البيانات من النموذج
        if form.is_valid():               # إذا البيانات صحيحة
            user = form.save()            # احفظ المستخدم في قاعدة البيانات
            login(request, user)          # سجل دخوله تلقائياً
            return redirect('shop:product_list')  # روح لصفحة المنتجات

    # اعرض صفحة إنشاء الحساب
    return render(request, 'accounts/register.html', {'form': form})


# ============================================
# دالة تسجيل الخروج
# ============================================
def logout_view(request):
    if request.method == 'POST':  # فقط عبر POST (أمان)
        logout(request)           # سجل الخروج
    return redirect('shop:product_list')  # روح لصفحة المنتجات
