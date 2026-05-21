"""
ملف الإعدادات الرئيسي للمشروع
هنا نضع كل إعدادات Django مثل: التطبيقات، قاعدة البيانات، اللغة...
"""
from pathlib import Path

# المسار الرئيسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# المفتاح السري (لا تشاركه مع أحد في مشاريع حقيقية)
SECRET_KEY = 'django-insecure-key-for-learning-only'

# وضع التطوير: True = تظهر رسائل الأخطاء
# DEBUG = False
DEBUG = True
# السماح بالوصول من أي جهاز
# ALLOWED_HOSTS = ['mouath.pythonanywhere.com', '127.0.0.1']
ALLOWED_HOSTS = [
    'mouath.pythonanywhere.com', 
    '127.0.0.1', 
    'localhost', 
    '10.0.0.2',  # ← مهم جداً لمحاكي أندرويد الافتراضي (Android Emulator)
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
    'rest_framework',  
    'corsheaders',               # مكتبة API (DRF)
    'accounts',                       # تطبيق المستخدمين
    'shop',                           # تطبيق المنتجات
    'delivery',                       # تطبيق التوصيل
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
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
# قاعدة البيانات (SQLite مناسبة للتعلم)
# ===========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # نوع قاعدة البيانات
        'NAME': BASE_DIR / 'db.sqlite3',          # اسم الملف
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

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ===========================
# إعادة التوجيه بعد تسجيل الدخول والخروج
# ===========================
LOGIN_URL = '/accounts/login/'          # رابط صفحة تسجيل الدخول
LOGIN_REDIRECT_URL = '/shop/'           # بعد تسجيل الدخول روح للمنتجات
LOGOUT_REDIRECT_URL = '/shop/'           # بعد الخروج روح لصفحة المنتجات

# ============================================
# إعدادات الـ CORS لتطبيق Flutter
# ============================================

# أثناء التطوير والتجربة، اسمح لجميع النطاقات بالاتصال بالـ API
CORS_ALLOW_ALL_ORIGINS = True

# إذا كنت تريد السماح بطلب الـ Cookies أو جلسات تسجيل الدخول (Sessions) عبر الـ API
CORS_ALLOW_CREDENTIALS = True