# movieticket_booking_system
```
🎬 A beginner-friendly Python Movie Ticket Booking System that allows users to login, select movies and ticket types,
 enter customer details, calculate prices and discounts, choose payment methods, generate booking IDs, view receipts,
 and cancel tickets with refund calculation.
```
## 🎫 1. Project Title
```
 Movie Ticket Booking System 🎬🎟️
```
## 📖 2. Introduction

The Movie Ticket Booking System is a Python-based mini project designed to simulate a real-world movie ticket booking application.

The system allows users to securely log in, view available movies, select a ticket category, enter customer details, choose the number of tickets, calculate the total price, apply discounts, select a payment method, generate a booking ID, and view a complete booking receipt.

The project also provides a ticket cancellation and refund facility.

This project is developed using basic and intermediate Python concepts such as variables, data types, lists, dictionaries, conditional statements, loops, functions, arguments, return values, and calculations.

## 🎯 3. Objectives

The main objectives of this project are:
```
- 🐍 To understand Python programming concepts.
- 🧩 To practice creating and calling functions.
- 🔐 To implement basic user login validation.
- 🎬 To display available movies.
- 🎫 To provide different ticket categories.
- 👤 To collect customer information.
- 🔢 To validate ticket quantity.
- 💰 To calculate ticket prices.
- 🏷️ To apply discounts based on booking amount.
- 💳 To provide multiple payment options.
- 🆔 To generate a unique booking ID.
- 🧾 To generate a booking receipt.
- ❌ To provide ticket cancellation.
- 💵 To calculate refund amount.
- 🔄 To understand the flow of a real-world booking system.
```
## ⚙️ 4. System Features

The improved system includes:
```
- 🔐 User Login
- 🎬 Display Available Movies
- 🎫 Display Ticket Categories
- ⭐ Standard, Premium and VIP tickets
- 👤 Customer Details
- 🔢 Ticket Quantity Validation
- 💰 Automatic Price Calculation
- 🏷️ Automatic Discount Calculation
- 💳 Multiple Payment Methods
- 🆔 Booking ID Generation
- 🧾 Detailed Booking Receipt
- ✅ Booking Confirmation
- ❌ Ticket Cancellation
- 💵 Refund Calculation
- 📋 Final Booking Summary
- ⚠️ Input Validation
- 🔄 Menu-based booking flow
- 🛠️ 5. Tools Used
- Tool	Purpose
- 🐍 Python	Programming
- 💻 VS Code	Code Editor
- 🤖 AI Tools	Learning and debugging
- 🖥️ Terminal	Program execution
```
## 🔄 6. Project Flow
                🚀 START
                   ↓
          🎬 Welcome Screen
                   ↓
             🔐 User Login
                   ↓
          Login Validation
             ↙         ↘
          Failed       Success
            ↓             ↓
           END      🎬 Show Movies
                         ↓
                  🎥 Select Movie
                         ↓
                 🎫 Show Ticket Types
                         ↓
                  Select Ticket Type
                         ↓
                  👤 Customer Details
                         ↓
                   🔢 Ticket Quantity
                         ↓
                  💰 Calculate Price
                         ↓
                   🏷️ Apply Discount
                         ↓
                    💳 Payment
                         ↓
                  🆔 Booking ID
                         ↓
                   🧾 Receipt
                         ↓
                  ✅ Booking Confirmed
                         ↓
                  ❓ Cancel Ticket?
                    ↙           ↘
                  YES           NO
                   ↓             ↓
             💵 Calculate       🎫 Keep
                Refund          Booking
                   ↓             ↓
                 🧾 Refund      🏁 END
## 🧩 7. Function Design

The project is divided into small functions so that every function performs one specific task.
```
main()
│
├── welcome_message()
├── login_user()
│
├── display_movies()
├── get_movie_details()
│
├── display_ticket_types()
├── get_ticket_details()
│
├── get_customer_details()
├── get_quantity()
│
├── calculate_total()
├── calculate_discount()
│
├── select_payment_method()
├── generate_booking_id()
│
├── display_booking_receipt()
│
├── cancel_ticket()
└── calculate_refund()

```

## 🎬 8. Available Movies

The system provides five movies:
```
1. 🎬 Avatar 3
2. 🦸 Avengers: Secret Wars
3. 🕷️ Spider-Man
4. 🦖 Jurassic World
5. 👻 The Conjuring
```
Each movie has its own movie price.

## 🎫 9. Ticket Categories
```
1. 🎟️ Standard - ₹200
2. ⭐ Premium  - ₹500
3. 👑 VIP      - ₹1000
```
The user can select any one category while booking.

## 🏷️ 10. Discount System

The system automatically calculates discounts based on the total booking amount.
```
- Total Amount	Discount
- Below ₹500	0%
- ₹500 – ₹999	10%
- ₹1000 – ₹1499	20%
- ₹1500 or above	40%
```
This makes the booking system more realistic.

## 💳 11. Payment Methods

The user can select:

1. 💳 Credit/Debit Card
2. 📱 UPI
3. 💵 Cash
🆔
## 🆔 12. Booking ID

After successful booking, the system generates a booking ID.

- Example:

- 🎫 Booking ID: BK1001

- This booking ID can be displayed on the final receipt.

## 🧾 13. Booking Receipt

The receipt displays:
```
1. Booking ID
2. Customer Name
3. Movie Name
4. Ticket Type
5. Number of Tickets
6.Ticket Price
7. Movie Price
8. Original Amount
9. Discount
10. Discount Amount
11. Final Amount
12. Payment Method
13. Booking Status
```
## ❌ 14. Cancellation & Refund

The user can cancel the booking after confirmation.

The system deducts 20% cancellation charges and returns 80% of the paid amount as a refund.

Example:

- Paid Amount       = ₹1000
- Cancellation Fee  = ₹200
- Refund Amount     = ₹800
