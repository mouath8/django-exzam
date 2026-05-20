#!/usr/bin/env python
"""
ملف manage.py - يُستخدم لتشغيل الأوامر مثل:
  python manage.py runserver   → لتشغيل الخادم
  python manage.py migrate     → لإنشاء قاعدة البيانات
  python manage.py createsuperuser → لإنشاء مدير
"""
import os
import sys

def main():
    # تحديد ملف الإعدادات الرئيسي
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("تأكد من تثبيت Django أولاً") from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
