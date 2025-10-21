# استخدم صورة Python الرسمية
FROM python:3.10-slim

# تعيين مجلد العمل
WORKDIR /app

# نسخ ملف المتطلبات وتثبيت المكتبات
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# نسخ باقي ملفات المشروع
COPY . .

# فتح بورت التطبيق
EXPOSE 5000

# تشغيل التطبيق
CMD ["python", "app.py"]

