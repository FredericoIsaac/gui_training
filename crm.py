from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Client Relation Manager")
root.geometry("400x600")

# Create a database or connect to exisiting one
my_db = sqlite3.connect("codemy.db")

# Create a cursor and initialize it
my_cursor = my_db.cursor()

# # Drop table
#my_cursor.execute("""DROP TABLE customers""")

# Create a Table
my_cursor.execute("""CREATE TABLE IF NOT EXISTS customers (
    first_name TEXT,
    last_name TEXT,
    zipcode INTEGER,
    price_paid REAL,
    email TEXT,
    address_1 TEXT,
    address_2 TEXT,
    city TEXT,
    state TEXT,
    country TEXT,
    phone TEXT,
    payment_method TEXT,
    discount_code TEXT
    )""")

# Clear text fields
def clear_fields():
    first_name_box.delete(0, END)
    last_name_box.delete(0, END)
    address1_box.delete(0, END)
    address2_box.delete(0, END)
    city_box.delete(0, END)
    state_box.delete(0, END)
    zipcode_box.delete(0, END)
    country_box.delete(0, END)
    phone_box.delete(0, END)
    email_box.delete(0, END)
    payment_method_box.delete(0, END)
    discount_code_box.delete(0, END)
    price_paid_box.delete(0, END)

# Submit Customer to Database
def add_customer():
    my_cursor.execute("INSERT INTO customers VALUES (:first_name, :last_name, :address1, :address2, :city, :state, :zipcode, :country, :phone, :email, :payment_method, :discount_code, :price_paid)",
    {
        "first_name": first_name_box.get(),
        "last_name": last_name_box.get(),
        "address1": address1_box.get(),
        "address2": address2_box.get(),
        "city": city_box.get(),
        "state": state_box.get(),
        "zipcode": zipcode_box.get(),
        "country": country_box.get(),
        "phone": phone_box.get(),
        "email": email_box.get(),
        "payment_method": payment_method_box.get(),
        "discount_code": discount_code_box.get(),
        "price_paid": price_paid_box.get()
    })
    # Commit changes to database
    my_db.commit()
    # Clear the fields
    clear_fields()

# Create a Label
title_label = Label(root, text="Codemy Customers Database", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=2, pady="10")

# Create main form to enter customer data
first_name_label = Label(root, text="First Name").grid(row=1, column=0, sticky=W, padx=10)
last_name_label = Label(root, text="Last Name").grid(row=2, column=0, sticky=W, padx=10)
address1_label = Label(root, text="Address 1").grid(row=3, column=0, sticky=W, padx=10)
address2_label = Label(root, text="Address 2").grid(row=4, column=0, sticky=W, padx=10)
city_label = Label(root, text="City").grid(row=5, column=0, sticky=W, padx=10)
state_label = Label(root, text="State").grid(row=6, column=0, sticky=W, padx=10)
zipcode_label = Label(root, text="Zipcode").grid(row=7, column=0, sticky=W, padx=10)
country_label = Label(root, text="Country").grid(row=8, column=0, sticky=W, padx=10)
phone_label = Label(root, text="Phone Number").grid(row=9, column=0, sticky=W, padx=10)
email_label = Label(root, text="Email Address").grid(row=10, column=0, sticky=W, padx=10)
payment_method_label = Label(root, text="Payment Method").grid(row=11, column=0, sticky=W, padx=10)
discount_code_label = Label(root, text="Discount Code").grid(row=12, column=0, sticky=W, padx=10)
price_paid_label = Label(root, text="Price Paid").grid(row=13, column=0, sticky=W, padx=10)

# Create Entry Boxes
first_name_box = Entry(root)
first_name_box.grid(row=1, column=1)

last_name_box = Entry(root)
last_name_box.grid(row=2, column=1, pady=5)

address1_box = Entry(root)
address1_box.grid(row=3, column=1, pady=5)

address2_box = Entry(root)
address2_box.grid(row=4, column=1, pady=5)

city_box = Entry(root)
city_box.grid(row=5, column=1, pady=5)

state_box = Entry(root)
state_box.grid(row=6, column=1, pady=5)

zipcode_box = Entry(root)
zipcode_box.grid(row=7, column=1, pady=5)

country_box = Entry(root)
country_box.grid(row=8, column=1, pady=5)

phone_box = Entry(root)
phone_box.grid(row=9, column=1, pady=5)

email_box = Entry(root)
email_box.grid(row=10, column=1, pady=5)

payment_method_box = Entry(root)
payment_method_box.grid(row=11, column=1, pady=5)

discount_code_box = Entry(root)
discount_code_box.grid(row=12, column=1, pady=5)

price_paid_box = Entry(root)
price_paid_box.grid(row=13, column=1, pady=5)

# Create Buttons
add_customer_button = Button(root, text="Add Customer To Database", command=add_customer)
add_customer_button.grid(row=14, column=0, padx=10, pady=10)

clear_fields_button = Button(root, text="Clear Fields", command=clear_fields)
clear_fields_button.grid(row=14, column=1)







my_db.commit()
mainloop()


my_db.close()