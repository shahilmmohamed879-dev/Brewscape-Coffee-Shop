# ☕ BrewScape - Premium Coffee Shop Ordering Website

A modern full-stack coffee shop ordering website where customers can browse premium coffee products, add items to their cart, and place orders. Every order is securely stored in MongoDB, making it a complete end-to-end web application.

---

## 📌 Project Overview

BrewScape is a responsive coffee shop website designed with a premium UI/UX inspired by modern café brands. The project demonstrates frontend development, backend integration, database connectivity, and version control using Git and GitHub.

---

## ✨ Features

- ☕ Modern premium coffee-themed UI
- 🛍️ Browse coffee menu
- ➕ Add products to cart
- ➖ Update item quantity
- 💰 Automatic total price calculation
- 🧾 Checkout page
- ✅ Order confirmation page
- 📱 Fully responsive design
- 🍃 MongoDB database integration
- 🚀 Fast and user-friendly interface

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### Database
- MongoDB Atlas

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

```
BrewScape/
│
├── index.html
├── shop.html
├── cart.html
├── checkout.html
├── placeorder.html
│
├── css/
│   ├── style.css
│
├── js/
│   ├── script.js
│
├── images/
│
├── backend/
│   ├── app.py
│   ├── database.py
│   ├── routes.py
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ How It Works

1. User visits the homepage.
2. Browses available coffee products.
3. Adds products to the shopping cart.
4. Reviews the cart.
5. Proceeds to checkout.
6. Places the order.
7. Flask receives the order request.
8. Order details are stored in MongoDB Atlas.
9. Customer receives an order confirmation.

---

## 🗄️ Database

### MongoDB Collections

### Products

```json
{
    "_id": "...",
    "name": "Cappuccino",
    "price": 180,
    "category": "Hot Coffee",
    "image": "cappuccino.jpg"
}
```

### Orders

```json
{
    "_id": "...",
    "customerName": "John",
    "phone": "9876543210",
    "address": "Chennai",
    "items": [],
    "total": 650,
    "status": "Placed",
    "date": "2026-06-27"
}
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/BrewScape.git
```

Move into the project folder

```bash
cd BrewScape
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Flask

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

## 📸 Screenshots

### Home Page

(Add Screenshot)

### Coffee Menu

(Add Screenshot)

### Shopping Cart

(Add Screenshot)

### Checkout

(Add Screenshot)

### Order Confirmation

(Add Screenshot)

---

## 🎯 Future Improvements

- User Login & Registration
- Admin Dashboard
- Payment Gateway Integration
- Order Tracking
- Email Confirmation
- Search & Filter
- Wishlist
- Coupon System
- Customer Reviews
- Dark Mode

---

## 📚 Learning Outcomes

Through this project, I gained experience in:

- Responsive Web Design
- Frontend Development
- Backend API Development
- MongoDB Database Integration
- Flask Framework
- CRUD Operations
- Git & GitHub Workflow
- Full Stack Application Development

---

## 👨‍💻 Author

**Mohamed Shakeel**

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub!

---

## 📄 License

This project is created for educational and portfolio purposes.
