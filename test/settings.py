"""
ملف الإعدادات الرئيسي للمشروع (نسخة الإنتاج والتطوير المحدثة - بدون مكتبات خارجية للـ CORS)
"""
import os
from pathlib import Path

# المسار الرئيسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# المفتاح السري
SECRET_KEY = 'django-insecure-key-for-learning-only'

# وضع التطوير
DEBUG = True

# السماح بالوصول من أي جهاز
ALLOWED_HOSTS = [
    'mouath.pythonanywhere.com', 
    '127.0.0.1', 
    'localhost', 
    '10.0.0.2',  
]

# ===========================
# التطبيقات المثبتة في المشروع
# ===========================
INSTALLED_APPS = [
    'django.contrib.admin',           
    'django.contrib.auth',            
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',                 
    'accounts',                       
    'shop',                           
    'delivery',                       
]

# ===========================
# تم استبدال الكورس الخارجي بالـ Middleware المخصصة الذاتية
# ===========================
MIDDLEWARE = [
    'test.middleware.CorsMiddleware',  # ← هذا هو السطر الصحيح البديل
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
        'DIRS': [BASE_DIR / 'templates'],  
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
# قاعدة البيانات 
# ===========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  
        'NAME': BASE_DIR / 'db.sqlite3',          
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
LANGUAGE_CODE = 'ar'           
TIME_ZONE = 'Asia/Riyadh'      
USE_I18N = True                
USE_TZ = True                  

# ===========================
# إعدادات الملفات الثابتة والميديا 
# ===========================
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'         

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ===========================
# إعادة التوجيه بعد تسجيل الدخول والخروج
# ===========================
LOGIN_URL = '/accounts/login/'          
LOGIN_REDIRECT_URL = '/shop/'           
LOGOUT_REDIRECT_URL = '/shop/'