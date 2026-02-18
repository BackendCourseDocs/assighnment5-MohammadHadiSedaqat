# 📚 Advanced Book Management API  
### 🚀 FastAPI + File Upload + Pagination + Validation

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-Modern_API-00C7B7?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Validation-Pydantic-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/File_Upload-Enabled-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Pagination-Supported-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Production_Ready-brightgreen?style=for-the-badge" />
</p>

---

# 🌍 Overview

**Advanced Book Management API** is a powerful RESTful backend built using **FastAPI**.

This project combines:

- 🔎 Book search
- ➕ Book creation
- 📸 Image upload support
- 📄 Pagination
- 🧠 Data validation
- 📦 Static file serving

It integrates with **OpenLibrary API** to preload books and allows dynamic addition of new books with optional cover images.

---

# 🏗 Architecture Flow

```
Application Startup
      │
      ▼
Fetch Books from OpenLibrary
      │
      ▼
Store in Local Memory (books list)
      │
      ├───────────────┐
      ▼               ▼
 GET /books        POST /books
 (Search)          (Add Book + Upload Image)
```

---

# 🔥 Core Features

✅ OpenLibrary Integration  
✅ In-Memory Book Storage  
✅ Smart Search Filtering  
✅ Pagination (skip & limit)  
✅ Add New Books  
✅ Image Upload Support  
✅ Static File Serving (/images)  
✅ Input Validation with Pydantic  
✅ Clean JSON Responses  
✅ Production-ready Structure  

---

# 📡 API Endpoints

---

## 🔎 GET `/books`

Search books with pagination support.

### Query Parameters

| Parameter | Type | Required | Description |
|------------|--------|----------|--------------|
| q | string | ✅ Yes | Search keyword |
| skip | int | ❌ Optional | Number of results to skip |
| limit | int | ❌ Optional | Number of results to return |

---

### 📥 Example Request

```bash
GET http://127.0.0.1:8000/books?q=python&skip=0&limit=5
```

---

### 📤 Example Response

```json
{
  "query": "python",
  "count": 5,
  "results": [
    {
      "title": "Learning Python",
      "author": "Mark Lutz",
      "publisher": "O'Reilly Media",
      "first_publish_year": 2013,
      "image_url": null
    }
  ],
  "skip": 0,
  "limit": 5
}
```

---

## ➕ POST `/books`

Add a new book with optional image upload.

### Form Fields

| Field | Type | Required |
|--------|--------|----------|
| title | string | ✅ Yes |
| author | string | ✅ Yes |
| publisher | string | ✅ Yes |
| first_publish_year | int | ✅ Yes |
| image | file | ❌ Optional |

---

### 📥 Example Request (cURL)

```bash
curl -X POST "http://127.0.0.1:8000/books" \
  -F "title=FastAPI Mastery" \
  -F "author=John Doe" \
  -F "publisher=Tech Press" \
  -F "first_publish_year=2024" \
  -F "image=@cover.jpg"
```

---

### 📤 Example Response

```json
{
  "title": "FastAPI Mastery",
  "author": "John Doe",
  "publisher": "Tech Press",
  "first_publish_year": 2024,
  "image_url": "http://127.0.0.1:8000/images/cover.jpg"
}
```

---

# 📂 Static Files

Uploaded images are stored inside:

```
/images
```

Accessible via:

```
http://127.0.0.1:8000/images/<filename>
```

---

# 🧠 Validation System

Validation is handled using **Pydantic**:

```python
title: str = Field(..., min_length=3, max_length=100)
first_publish_year: int = Field(..., ge=0)
```

Ensures:

- Minimum & maximum length validation
- Positive year constraint
- Strong data integrity

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/book-management-api.git
cd book-management-api
```

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

## 3️⃣ Install Dependencies

```bash
pip install fastapi uvicorn requests python-multipart
```

---

# ▶️ Run Application

```bash
uvicorn main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

---

# 📘 Auto API Documentation

Swagger:
```
/docs
```

ReDoc:
```
/redoc
```

---

# 📁 Project Structure

```
book-management-api/
│
├── main.py
├── images/
├── README.md
```

---

# 🚀 Future Enhancements

- 🗄 Database integration (PostgreSQL / SQLite)
- 🔐 Authentication (JWT)
- 🧪 Unit Testing
- 🐳 Docker Support
- ☁ Cloud Deployment
- 📊 Admin Dashboard
- 🔍 Advanced Filtering
- 🧠 Full CRUD Operations

---

# 🛠 Tech Stack

- FastAPI
- Python
- Pydantic
- Requests
- Uvicorn
- OpenLibrary API

---

# 📜 License

MIT License

---

---

<div dir="rtl">

# 📚 API مدیریت پیشرفته کتاب  
### 🚀 جستجو + افزودن کتاب + آپلود تصویر + صفحه‌بندی

---

# 🌟 معرفی پروژه

این پروژه یک API حرفه‌ای مدیریت کتاب است که با استفاده از **FastAPI** توسعه داده شده است.

ویژگی‌های این سیستم:

- دریافت لیست اولیه از OpenLibrary
- جستجوی پیشرفته
- افزودن کتاب جدید
- آپلود تصویر جلد
- صفحه‌بندی نتایج
- اعتبارسنجی داده‌ها
- سرو فایل‌های استاتیک

---

# 🏗 نحوه عملکرد

```
شروع برنامه
      │
      ▼
دریافت کتاب‌ها از OpenLibrary
      │
      ▼
ذخیره در حافظه برنامه
      │
      ├───────────────┐
      ▼               ▼
 GET /books        POST /books
```

---

# ✨ ویژگی‌ها

✅ جستجوی هوشمند  
✅ صفحه‌بندی (skip / limit)  
✅ افزودن کتاب جدید  
✅ آپلود تصویر  
✅ ذخیره فایل در پوشه images  
✅ اعتبارسنجی حرفه‌ای با Pydantic  
✅ مستندات خودکار  
✅ ساختار تمیز و توسعه‌پذیر  

---

# 📡 اندپوینت‌ها

## 🔎 GET /books

پارامترها:

| نام | توضیح |
|------|--------|
| q | عبارت جستجو |
| skip | تعداد نتایج رد شده |
| limit | تعداد نتایج نمایش داده شده |

---

## ➕ POST /books

دریافت اطلاعات از طریق Form Data  
امکان ارسال فایل تصویر وجود دارد.

---

# 📂 مسیر تصاویر

تصاویر داخل پوشه:

```
images/
```

و از طریق مسیر زیر قابل دسترسی هستند:

```
/images/filename.jpg
```

---

# ⚙️ نصب

```bash
pip install fastapi uvicorn requests python-multipart
```

---

# ▶️ اجرا

```bash
uvicorn main:app --reload
```

---

# 📘 مستندات

```
/docs
```

---

# 🚀 توسعه‌های آینده

- اتصال به دیتابیس
- افزودن احراز هویت
- عملیات کامل CRUD
- داکرایز کردن
- دیپلوی روی سرور ابری

---

# 🏆 تکنولوژی‌ها

- FastAPI
- Python
- Pydantic
- Requests
- Uvicorn

---

# 📜 لایسنس

MIT

</div>
