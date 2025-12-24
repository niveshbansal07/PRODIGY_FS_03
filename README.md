# 🛒 SamanBuddy – E-Commerce Website for Local Store

SamanBuddy is a **full-stack e-commerce web application** developed using **Flask, MySQL, and modern frontend technologies**.
This project allows customers to **browse products, add them to cart, and place orders online**, making it ideal for a **local store going digital**.

The application demonstrates **real-world backend development**, database relationships, secure authentication using **JWT**, and clean responsive UI design.

---

## 📸 Project Preview

![Preview](https://github.com/niveshbansal07/PRODIGY_FS_03/blob/main/Document%20-%20Brave%2012_24_2025%206_42_14%20PM.png)
![Preview](https://github.com/niveshbansal07/PRODIGY_FS_03/blob/main/Document%20-%20Brave%2012_24_2025%206_42_39%20PM.png)

*(Replace screenshots with your actual images)*

---

## 🚀 Features

### ✅ Core Features

* User Signup & Login system
* Secure authentication using **JWT (JSON Web Tokens)**
* Password hashing with **bcrypt**
* Product listing with image, price & description
* Add to Cart & Remove from Cart functionality
* Cart data stored in MySQL
* Protected routes for authenticated users
* Responsive & clean UI design

### ⭐ Optional / Advanced Features

* Order placement system
* Order confirmation page
* Product stock management
* Modular backend architecture
* SEO-friendly frontend structure
* Ready for future features like:

  * Order tracking
  * User reviews
  * Product filters & sorting
  * Customer support module

---

## 🛠 Tech Stack

### **Frontend**

* HTML5
* CSS3 (Responsive & clean UI)
* JavaScript (Fetch API)

### **Backend**

* Python (Flask)
* JWT Authentication
* bcrypt (Password hashing)
* REST APIs

### **Database**

* MySQL

### **Other Tools**

* Flask-CORS
* python-dotenv
* mysql-connector-python

---

## 📁 Project Structure

```
SamanBuddy/
│
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── main.js
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── cart.html
│   ├── order.html
│   └── success.html
│
├── config.py
├── models.py
├── app.py
├── requirements.txt
└── venv/
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```env
SAMANSUPERKEY=your_flask_secret_key
NIVESHSAMANBUDDY=your_jwt_secret_key
```

⚠️ **Important:**
Add `.env` to `.gitignore` to protect sensitive data.

---

## 🗄 Database Structure (MySQL)

```sql
-- Users Table
CREATE TABLE user_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255)
);

-- Products Table
CREATE TABLE products_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    price DECIMAL(10,2),
    image VARCHAR(255),
    stock INT
);

-- Cart Table
CREATE TABLE cart_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    product_id INT,
    quantity INT
);
```

---

## ⚙ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Database

Update **MySQL credentials** in `config.py`.

### ▶ Run the Application

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

## 🧠 What I Learned

* Building a full-stack e-commerce system
* Flask project architecture
* JWT-based authentication
* Secure password hashing with bcrypt
* MySQL relational database design
* API integration with frontend (Fetch API)
* Protecting routes using decorators
* Writing clean, scalable backend code
* Responsive UI development

---

## 📌 Project Purpose

This project was built to:

* Digitize a **local store**
* Practice **real-world full-stack development**
* Demonstrate backend & database skills
* Create a scalable base for a production-ready e-commerce platform

---

## 📬 Contact

**Nivesh Bansal**
Aspiring Full Stack Developer

📧 Email: **[niveshbansal52@gmail.com](mailto:niveshbansal52@gmail.com)**
🌐 Portfolio: [https://nivesh-bansal.vercel.app](https://nivesh-bansal.vercel.app)
🔗 GitHub: [https://github.com/niveshbansal07](https://github.com/niveshbansal07)

---
