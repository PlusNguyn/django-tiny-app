@echo off
echo Establishing Django environment...

REM 1. Tạo Virtual Environment
echo Creating Virtual Environment...
python -m venv env
call env\Scripts\activate

REM 2. Cài đặt thư viện
echo Installing requirements...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt



REM 3. Thiết lập database
echo Setting up database...
cd blogapp
python manage.py makemigrations
python manage.py migrate

REM 5. Khởi động server
echo Starting server...
python manage.py runserver
pause

REM 6. Khởi động trình duyệt
start http://127.0.0.1:8000/
