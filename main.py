booking_no = 1


def welcome():
    print("\n🎬 Welcome to Movie Ticket Booking 🎬")


# ---------------- LOGIN ----------------

def login_user():
    db = ["saumya@gmail.com", "123"]
    print("\n🔐 Please login if you want to order tickets")

    email = input("📧 Enter your email: ")
    password = input("🔑 Enter your password: ")

    if email == "" and password == "":
        print("⚠️ Please enter email and password")
        return False

    elif email == "":
        print("⚠️ Please enter email")
        return False

    elif password == "":
        print("⚠️ Please enter password")
        return False

    elif email != db[0] and password != db[1]:
        print("❌ Invalid email and password")
        return False

    elif email != db[0]:
        print("❌ Invalid email")
        return False

    elif password != db[1]:
        print("❌ Invalid password")
        return False

    else:
        print("✅ Welcome")
        return True


# ---------------- MOVIES ----------------

def movies():
    print("\n🎬 Available Movies")
    print("1. Avatar 3 - ₹200")
    print("2. Spider-Man - ₹250")
    print("3. Jurassic World - ₹300")
    print("4. The Conjuring - ₹180")
    print("5. Avengers - ₹350")


def get_movie(choice):

    if choice == 1:
        return "Avatar 3", 200

    elif choice == 2:
        return "Spider-Man", 250

    elif choice == 3:
        return "Jurassic World", 300

    elif choice == 4:
        return "The Conjuring", 180

    elif choice == 5:
        return "Avengers", 350

    else:
        return None, 0


# ---------------- TICKET TYPE ----------------

def ticket_types():

    print("\n🎫 Ticket Types")
    print("1. Standard - ₹200")
    print("2. Premium  - ₹500")
    print("3. VIP      - ₹1000")


def get_ticket(choice):

    if choice == 1:
        return "Standard", 200

    elif choice == 2:
        return "Premium", 500

    elif choice == 3:
        return "VIP", 1000

    else:
        return None, 0


# ---------------- CUSTOMER ----------------

def customer():

    name = input("\n👤 Enter Customer Name: ")
    phone = input("📱 Enter Phone Number: ")

    return name, phone


# ---------------- PRICE ----------------

def calculate_price(ticket_price, quantity, movie_price):

    one_ticket_price = ticket_price + movie_price

    total = one_ticket_price * quantity

    return total


# ---------------- DISCOUNT ----------------

def discount(total):

    if total >= 1500:
        percent = 40

    elif total >= 1000:
        percent = 20

    elif total >= 500:
        percent = 10

    else:
        percent = 0

    discount_amount = total * percent / 100

    final_price = total - discount_amount

    return percent, discount_amount, final_price


# ---------------- PAYMENT ----------------

def payment():

    print("\n💳 Payment Method")
    print("1. UPI")
    print("2. Card")
    print("3. Cash")

    choice = int(input("Choose Payment Method: "))

    if choice == 1:
        return "UPI"

    elif choice == 2:
        return "Card"

    elif choice == 3:
        return "Cash"

    else:
        return "Unknown"


# ---------------- BOOKING ID ----------------

def booking_id():

    global booking_no

    booking_no = booking_no + 1

    return "BK" + str(booking_no)


# ---------------- RECEIPT ----------------

def show_receipt(name, phone, movie, movie_price,
                 ticket, ticket_price, quantity,
                 total, percent, discount_amount,
                 final_price, payment_method, book_id):

    print("\n")
    print("=" * 50)
    print("🧾 BOOKING RECEIPT")
    print("=" * 50)

    print("🆔 Booking ID       :", book_id)
    print("👤 Customer Name    :", name)
    print("📱 Phone Number     :", phone)

    print("-" * 50)

    print("🎬 Movie            :", movie)
    print("🎬 Movie Price      : ₹", movie_price)

    print("🎫 Ticket Type      :", ticket)
    print("🎫 Ticket Price     : ₹", ticket_price)

    print("🔢 Number of Tickets:", quantity)

    print("-" * 50)

    print("💰 Total Price      : ₹", total)
    print("🏷️ Discount         :", percent, "%")
    print("💸 Discount Amount  : ₹", discount_amount)

    print("-" * 50)

    print("💵 Final Price      : ₹", final_price)
    print("💳 Payment Method   :", payment_method)

    print("=" * 50)
    print("          ✅ BOOKING CONFIRMED!")
    print("=" * 50)


# ---------------- CANCEL ----------------

def cancel_ticket(final_price):

    choice = input("\n❓ Do you want to cancel? (yes/no): ")

    if choice == "yes":

        charge = final_price * 20 / 100

        refund = final_price - charge

        print("\n❌ Ticket Cancelled")
        print("📉 Cancellation Charge : ₹", charge)
        print("💰 Refund Amount       : ₹", refund)

    elif choice == "no":

        print("\n🎫 Ticket is still booked.")

    else:

        print("\n⚠️ Invalid choice.")


# ---------------- MAIN ----------------

def main():

    welcome()

    # Login
    login = login_user()

    if login == False:
        return

    # Movie
    movies()

    movie_choice = int(input("\n🎬 Select Movie (1-5): "))

    movie, movie_price = get_movie(movie_choice)

    if movie == None:
        print("❌ Invalid Movie")
        return

    # Ticket
    ticket_types()

    ticket_choice = int(input("\n🎫 Select Ticket (1-3): "))

    ticket, ticket_price = get_ticket(ticket_choice)

    if ticket == None:
        print("❌ Invalid Ticket")
        return

    # Customer
    name, phone = customer()

    # Quantity
    quantity = int(input("🔢 Enter Number of Tickets: "))

    # Calculate total
    total = calculate_price(
        ticket_price,
        quantity,
        movie_price
    )

    # Discount
    percent, discount_amount, final_price = discount(total)

    # Payment
    payment_method = payment()

    # Booking ID
    book_id = booking_id()

    # Final Receipt
    show_receipt(
        name,
        phone,
        movie,
        movie_price,
        ticket,
        ticket_price,
        quantity,
        total,
        percent,
        discount_amount,
        final_price,
        payment_method,
        book_id
    )

    # Cancellation
    cancel_ticket(final_price)


# Run program
main()