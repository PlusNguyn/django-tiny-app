# Django Tiny App

## Hướng dẫn chạy ứng dụng Django

### Yêu cầu hệ thống
- Python 3.x
- Django 3.x hoặc mới hơn
- pip (Python package installer)

### Cài đặt

1. **Clone repository**
    ```bash
    git clone git@github.com:PlusNguyn/django-tiny-app.git

    cd django-tiny-app
    ```

2. **Tạo virtual environment và kích hoạt**
    ```bash
    python -m venv env
    source env/bin/activate  # Trên Windows: .\env\Scripts\activate
    ```

3. **Cài đặt các gói phụ thuộc**
    ```bash
    pip install -r requirements.txt
    ```

4. **Chạy migrations**
    ```bash
    python manage.py migrate
    ```

5. **Chạy server**
    ```bash
    python manage.py runserver
    ```

6. **Truy cập ứng dụng**
    Mở trình duyệt và truy cập `http://127.0.0.1:8000/`


