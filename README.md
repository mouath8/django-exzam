# 📋 خطوات تشغيل المشروع

## 1️⃣ تثبيت المكتبات
```
pip install -r requirements.txt
```

## 2️⃣ إنشاء قاعدة البيانات
```
python manage.py makemigrations
python manage.py migrate
```

## 3️⃣ إنشاء حساب المدير (اختياري)
```
python manage.py createsuperuser
```

## 4️⃣ تشغيل الخادم
```
python manage.py runserver
```

---

## 🔗 الروابط

| الصفحة | الرابط |
|--------|--------|
| المنتجات | http://127.0.0.1:8000/shop/ |
| تسجيل دخول | http://127.0.0.1:8000/accounts/login/ |
| إنشاء حساب | http://127.0.0.1:8000/accounts/register/ |
| التوصيل | http://127.0.0.1:8000/delivery/ |
| API (JSON) | http://127.0.0.1:8000/delivery/api/ |
| لوحة الإدارة | http://127.0.0.1:8000/admin/ |
