﻿# Shopping System Management 📊

![Project Preview](https://github.com/rj9884/shopping-mall-billing-system/blob/main/assets/Ui.png)

A comprehensive **Shopping Mall Billing System** application written in **Python** with **MySQL integration**, designed for seamless management of products, customers, and purchases. This project enables efficient data handling, provides easy-to-use menus, and generates detailed invoices.

## ✨ Features
- **Product Management**:
  - Create product tables and manage the database.
  - Add, remove, or modify products.
  - View available stocks with details like price, quantity, and discounts.
- **Customer Management**:
  - Register new customers and generate unique customer IDs.
  - View customer information efficiently.
- **Purchase Management**:
  - Place orders, generate invoices, and apply discounts dynamically.
  - Automatically update product stock after purchases.
- **Editor Menu**:
  - Modify product details, including name, price, and quantity.
- **Invoice Generation**:
  - Generate detailed bills with customer and purchase details.

## 🚀 Technologies Used
- **Python**: Provides the core functionality of the project.
- **MySQL**: Handles database management for storing and manipulating records.

## 📂 Project Structure
```
project/
├── main.py          # Core Python script
├── README.md        # Documentation
├── assets           # images/media
```

## 🛠️ Setup Instructions
1. **Install Python**: Ensure Python is installed on your system.
2. **Install MySQL**: Set up MySQL and create a database named **Shopping**.
3. **Update Credentials**: Configure connection details in the `main.py` file (e.g., `host`, `user`, `password`).
4. **Run the Script**: Execute the Python script using `python main.py` to interact with the menu-driven interface.

## 📸 Demo
![Project Demo](https://github.com/rj9884/shopping-mall-billing-system/blob/main/assets/demo.png)

## 🎨 Key Functionalities
- **Database Initialization**: Creates tables (`Product`, `Customer`) automatically if they don't exist.
- **Customer Registration**: Generates unique customer IDs and stores customer data.
- **Product Purchases**: Tracks purchases, applies discounts, and updates stock dynamically.
- **Invoice Generation**: Provides formatted invoices with complete details of the purchase.
- **Error Handling**: Displays error messages for invalid inputs or database issues.
