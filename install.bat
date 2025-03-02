@echo off
echo 🔧 Đang thiết lập môi trường Django...

REM 1. Tạo Virtual Environment
python -m venv env
call env\Scripts\activate

REM 2. Cài đặt thư viện
pip install --upgrade pip
pip install -r requirements.txt

REM 3. Thiết lập database
cd blogapp
python manage.py migrate

REM 4. Khởi động server
echo 🚀 Khởi động Django server...
python manage.py runserver
pause
