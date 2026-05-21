"""
ملف الإعدادات الرئيسي للمشروع (نسخة الإنتاج والتطوير المحدثة)
هنا نضع كل إعدادات Django مثل: التطبيقات، قاعدة البيانات، اللغة...
"""
import os
from pathlib import Path

# المسار الرئيسي للمشروع (يعطي مساراً مطلقاً)
BASE_DIR = Path(__file__).resolve().parent.parent

# المفتاح السري (لا تشاركه مع أحد في مشاريع حقيقية)
SECRET_KEY = 'django-insecure-key-for-learning-only'

# وضع التطوير: True تظهر رسائل الأخطاء (اقلبه إلى False عند انتهاء مشروع التخرج والرفع الفعلي)
DEBUG = True

# السماح بالوصول من أي جهاز ونطاق السيرفر الخاص بك
ALLOWED_HOSTS = [
    'mouath.pythonanywhere.com', 
    '127.0.0.1', 
    'localhost', 
    '10.0.0.2',  # مهم جداً لمحاكي أندرويد الافتراضي (Android Emulator)
]

# ===========================
# التطبيقات المثبتة في المشروع
# ===========================
INSTALLED_APPS = [
    'django.contrib.admin',           # لوحة الإدارة
    'django.contrib.auth',            # نظام المصادقة (تسجيل دخول)
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',                 # مكتبة الـ API (DRF)
    'corsheaders',                    # مكتبة الـ CORS للسماح باتصال تطبيق Flutter
    'accounts',                       # تطبيق المستخدمين
    'shop',                           # تطبيق المنتجات
    'delivery',                       # تطبيق التوصيل
]

# ===========================
# الترتيب الصحيح والموصى به للـ Middleware
# ===========================
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',                  # يجب أن يكون في الأعلى لـ Flutter
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',   # يجب أن يسبق الـ CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ملف التوجيه الرئيسي
ROOT_URLCONF = 'test.urls'

# إعدادات القوالب (HTML)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # مجلد القوالب المشترك
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'test.wsgi.application'

# ===========================
# قاعدة البيانات (باستخدام المسار المطلق BASE_DIR)
# ===========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # نوع قاعدة البيانات
        'NAME': BASE_DIR / 'db.sqlite3',          # مسار الملف المطلق لمنع خطأ الـ OperationalError
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ===========================
# إعدادات اللغة والوقت
# ===========================
LANGUAGE_CODE = 'ar'           # اللغة العربية
TIME_ZONE = 'Asia/Riyadh'      # المنطقة الزمنية
USE_I18N = True                # تفعيل الترجمة
USE_TZ = True                  # استخدام المناطق الزمنية

# ===========================
# إعدادات الملفات الثابتة والميديا (مهمة جداً للسيرفر)
# ===========================
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # المجلد الذي سيجمع فيه السيرفر ملفات الـ CSS والـ Admin

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'         # المجلد الخاص بالصور المرفوعة للمنتجات

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ===========================
# إعادة التوجيه بعد تسجيل الدخول والخروج
# ===========================
LOGIN_URL = '/accounts/login/'          # رابط صفحة تسجيل الدخول
LOGIN_REDIRECT_URL = '/shop/'           # بعد تسجيل الدخول اذهب للمنتجات
LOGOUT_REDIRECT_URL = '/shop/'          # بعد الخروج اذهب لصفحة المنتجات

# ============================================
# إعدادات الـ CORS لتطبيق Flutter
# ============================================

# السماح لجميع الأجهزة والتطبيقات الخارجية بالاتصال بالـ API بدون حظر
CORS_ALLOW_ALL_ORIGINS = True

# السماح بطلب الـ Cookies أو جلسات تسجيل الدخول عبر الـ API
CORS_ALLOW_CREDENTIALS = True