# 🚀 Form Handling in Back-End (FastAPI)
---

## 🌍 English Documentation

---

## 📌 What is Form in Back-End?

In Back-End development, a **Form** is a mechanism used to send structured data from the client (browser) to the server through an HTTP request.

Forms are usually created using HTML `<form>` elements and submitted via:

- `GET` → Data sent in URL (Query Parameters)
- `POST` → Data sent in Request Body

---

## 🧠 How Form Works (Full Flow)

```
User fills HTML Form
        ↓
Browser builds HTTP Request
        ↓
Data encoded (x-www-form-urlencoded / multipart)
        ↓
Server parses request body
        ↓
Validation & Processing
        ↓
Response returned (JSON / HTML / Redirect)
```

---

## 🔎 Types of Form Encoding

### 1️⃣ application/x-www-form-urlencoded

Default form encoding (no file upload)

Example Body:
```
username=ali&password=1234
```

---

### 2️⃣ multipart/form-data

Used when uploading files.

Each field is separated by boundaries.

---

### 3️⃣ text/plain

Rarely used.

---

## 📬 GET vs POST

| Feature | GET | POST |
|----------|------|------|
| Data Location | URL | Body |
| Visibility | Visible | Hidden |
| Security | Low | Higher |
| Usage | Search | Login / Register |

⚠ Never send passwords using GET.

---

## 🧪 FastAPI Implementation

### Basic Form Example

```python
from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/login")
def login(
    username: str = Form(...),
    password: str = Form(...)
):
    return {
        "username": username,
        "password": password
    }
```

---

### Validation Example

```python
from fastapi import HTTPException

@app.post("/books")
def create_book(
    title: str = Form(..., min_length=3),
    price: float = Form(...)
):
    if price < 0:
        raise HTTPException(status_code=400, detail="Price cannot be negative")

    return {"message": "Book created"}
```

---

### File Upload Example

```python
from fastapi import File, UploadFile

@app.post("/upload")
def upload_file(
    username: str = Form(...),
    file: UploadFile = File(...)
):
    return {"filename": file.filename}
```

---

## 🔐 Security Best Practices

- Always use POST for sensitive data
- Use HTTPS
- Validate input strictly
- Implement CSRF protection (for production apps)
- Sanitize user input
- Limit file upload size

---

## 🧩 Form vs JSON

| Form | JSON |
|------|------|
| Flat Structure | Nested Structure |
| Traditional Web Apps | REST APIs |
| Limited | Flexible |
| Browser-native | JS-driven |

Example JSON:

```json
{
  "user": {
    "name": "Ali",
    "age": 22
  }
}
```

---

## 🎯 When Should You Use Form?

✔ Admin panels  
✔ Server-rendered pages  
✔ Simple authentication forms  
✔ File uploads  

Use JSON for modern SPA applications (React, Vue, etc).



# 🏁 Final Summary

Form in Back-End is not just a string like:

```
username=ali&password=1234
```

It is a complete HTTP mechanism including:

- Encoding
- Method
- Parsing
- Validation
- Security considerations

Mastering Form handling is fundamental for becoming a professional Full-Stack Developer.

---


# 🇮🇷 مدیریت فرم (Form Handling) در بک‌اند (FastAPI)

---

<div dir="rtl">

## 📌 فرم در بک‌اند چیست؟

در توسعه بک‌اند، **Form** مکانیزمی برای ارسال داده‌های ساختاریافته از سمت کاربر (مرورگر) به سرور از طریق یک درخواست HTTP است.

فرم‌ها معمولاً با استفاده از عنصر `<form>` در HTML ساخته می‌شوند و از طریق روش‌های زیر ارسال می‌شوند:

- GET → داده‌ها در URL ارسال می‌شوند (پارامترهای Query)  
- POST → داده‌ها در بدنه درخواست (Request Body) ارسال می‌شوند

---

## 🧠 فرم چگونه کار می‌کند؟ (روند کامل)

```
کاربر فرم HTML را پر می‌کند
        ↓
مرورگر یک درخواست HTTP می‌سازد
        ↓
داده‌ها encode می‌شوند (x-www-form-urlencoded / multipart)
        ↓
سرور بدنه درخواست را parse می‌کند
        ↓
اعتبارسنجی و پردازش انجام می‌شود
        ↓
پاسخ بازگردانده می‌شود (JSON / HTML / Redirect)
```

---

## 🔎 انواع Encoding در فرم

### 1️⃣ application/x-www-form-urlencoded

نوع پیش‌فرض encoding فرم (بدون آپلود فایل)

<div style="text-align:left">

```
username=ali&password=1234
```

</div>

---

### 2️⃣ multipart/form-data

زمانی استفاده می‌شود که فایل آپلود می‌کنیم.

<div style="text-align:left">

هر فیلد با boundary از بقیه جدا می‌شود.

</div>

---

### 3️⃣ text/plain

به‌ندرت استفاده می‌شود.

---

## 📬 تفاوت GET و POST

<div style="text-align:left">

| ویژگی | GET | POST |
|----------|------|------|
| محل داده | URL | بدنه |
| قابل مشاهده بودن | قابل مشاهده | مخفی |
| امنیت | پایین | بیشتر |
| کاربرد | جستجو | ورود / ثبت‌نام |

</div>

⚠ هرگز رمز عبور را با GET ارسال نکنید.

---

## 🧪 پیاده‌سازی در FastAPI

### مثال پایه فرم

<div style="text-align:left">

```python
from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/login")
def login(
    username: str = Form(...),
    password: str = Form(...)
):
    return {
        "username": username,
        "password": password
    }
```

</div>

---

### مثال اعتبارسنجی

<div style="text-align:left">

```python
from fastapi import HTTPException

@app.post("/books")
def create_book(
    title: str = Form(..., min_length=3),
    price: float = Form(...)
):
    if price < 0:
        raise HTTPException(status_code=400, detail="Price cannot be negative")

    return {"message": "Book created"}
```

</div>

---

### مثال آپلود فایل

<div style="text-align:left">

```python
from fastapi import File, UploadFile

@app.post("/upload")
def upload_file(
    username: str = Form(...),
    file: UploadFile = File(...)
):
    return {"filename": file.filename}
```

</div>

---

## 🔐 بهترین شیوه‌های امنیتی

- همیشه برای داده‌های حساس از POST استفاده کنید  
- از HTTPS استفاده کنید  
- ورودی‌ها را به‌صورت سخت‌گیرانه اعتبارسنجی کنید  
- در برنامه‌های Production از CSRF Protection استفاده کنید  
- ورودی‌های کاربر را پاک‌سازی (Sanitize) کنید  
- حجم فایل‌های آپلودی را محدود کنید

---

## 🧩 مقایسه Form و JSON

<div style="text-align:left">

| Form | JSON |
|------|------|
| ساختار تخت (Flat) | ساختار تو در تو (Nested) |
| مناسب برنامه‌های وب سنتی | مناسب REST API |
| محدودتر | انعطاف‌پذیر |
| وابسته به مرورگر | مبتنی بر JavaScript |

نمونه JSON:

```json
{
  "user": {
    "name": "Ali",
    "age": 22
  }
}
```

</div>

---

## 🎯 چه زمانی باید از Form استفاده کنید؟

✔ پنل‌های ادمین  
✔ صفحات Server-Rendered  
✔ فرم‌های ساده احراز هویت  
✔ آپلود فایل  

برای برنامه‌های مدرن SPA (مانند React و Vue) معمولاً از JSON استفاده می‌شود.

---

# 🏁 جمع‌بندی نهایی

Form در بک‌اند فقط یک رشته ساده مانند:

<div style="text-align:left">

```
username=ali&password=1234
```

</div>

نیست.

بلکه یک مکانیزم کامل HTTP است که شامل موارد زیر می‌شود:

- Encoding  
- Method  
- Parsing  
- Validation  
- ملاحظات امنیتی  

تسلط بر مدیریت فرم‌ها یکی از پایه‌های اصلی برای تبدیل شدن به یک توسعه‌دهنده حرفه‌ای فول‌استک است.

</div>
