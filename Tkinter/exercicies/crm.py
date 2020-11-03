from tkinter import *
from PIL import ImageTk, Image
import sqlite3
import csv
from tkinter import ttk

root = Tk()
root.title("Client Relation Manager")
root.geometry("400x600")

# Create a database or connect to exisiting one
my_db = sqlite3.connect("codemy.db")

# Create a cursor and initialize it
my_cursor = my_db.cursor()

# #Drop table
# my_cursor.execute("""DROP TABLE customers""")

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

# Write to csv excel function
def write_to_csv(list_query):
    """
    Export to a csv called customers
    """
    with open("customers.csv", "a", newline="") as f:
        w = csv.writer(f, dialect="excel")
        for record in list_query:
            w.writerow(record)


# List customers
def list_customers():
    list_customers_query = Tk()
    list_customers_query.title("List All Customers")
    list_customers_query.geometry("800x600")

    to_csv_file = [("first_name", "last_name", "address1", "address2", "city", "state", "zipcode", "country", "phone", "email", "payment_method", "discount_code", "price_paid")]
    list_query = my_cursor.execute("SELECT * FROM customers")
    for index, customer in enumerate(list_query):
        num_column = 0
        to_csv_file.append(customer)
        for y in customer:
            lookup_label = Label(list_customers_query, text=y)
            lookup_label.grid(row=index, column=num_column)
            num_column += 1 

    # csv export
    csv_button = Button(list_customers_query, text="Save to Excel", command=lambda: write_to_csv(to_csv_file))
    csv_button.grid(row=index+1, column=0)


# Search Customers
def search_customers():
    search_customers = Tk()
    search_customers.title("Search Customers")
    search_customers.geometry("1100x800")
    
    def update():
        sql_command = """UPDATE customers SET first_name = ?, last_name = ?, zipcode = ?, price_paid = ?, email = ?, address_1 = ?, address_2 = ?, city = ?, state = ?, country = ?, phone = ?, payment_method = ?, discount_code = ? WHERE ROWID = ?"""
        first_name = first_name_box2.get()
        last_name = last_name_box2.get()
        zipcode = zipcode_box2.get()
        price_paid = price_paid_box2.get()
        email = email_box2.get()
        address_1 = address1_box2.get()
        address_2 = address2_box2.get()
        city = city_box2.get()
        state = state_box2.get()
        country = country_box2.get()
        phone = phone_box2.get()
        payment_method = payment_method_box2.get()
        discount_code = discount_code_box2.get()
        user_id = 1
        inputs = (first_name, last_name, zipcode, price_paid, email, address_1, address_2, city, state, country, phone, payment_method, discount_code, user_id)

        my_cursor.execute(sql_command, inputs)
        my_db.commit()

        search_customers.destroy()

    def edit_now(id, index):

        sql2 = "SELECT * FROM customers WHERE ROWID=?"   
        searched = search_box.get()
        name2 = (id,)
        result2 = my_cursor.execute(sql2, name2)
        result2 = my_cursor.fetchall()

        index += 1
        # Create main form to enter customer data
        first_name_label = Label(search_customers, text="First Name").grid(row=index + 1, column=0, sticky=W, padx=10)
        last_name_label = Label(search_customers, text="Last Name").grid(row=index + 2, column=0, sticky=W, padx=10)
        address1_label = Label(search_customers, text="Address 1").grid(row=index + 3, column=0, sticky=W, padx=10)
        address2_label = Label(search_customers, text="Address 2").grid(row=index + 4, column=0, sticky=W, padx=10)
        city_label = Label(search_customers, text="City").grid(row=index + 5, column=0, sticky=W, padx=10)
        state_label = Label(search_customers, text="State").grid(row=index + 6, column=0, sticky=W, padx=10)
        zipcode_label = Label(search_customers, text="Zipcode").grid(row=index + 7, column=0, sticky=W, padx=10)
        country_label = Label(search_customers, text="Country").grid(row=index + 8, column=0, sticky=W, padx=10)
        phone_label = Label(search_customers, text="Phone Number").grid(row=index + 9, column=0, sticky=W, padx=10)
        email_label = Label(search_customers, text="Email Address").grid(row=index + 10, column=0, sticky=W, padx=10)
        payment_method_label = Label(search_customers, text="Payment Method").grid(row=index + 11, column=0, sticky=W, padx=10)
        discount_code_label = Label(search_customers, text="Discount Code").grid(row=index + 12, column=0, sticky=W, padx=10)
        price_paid_label = Label(search_customers, text="Price Paid").grid(row=index + 13, column=0, sticky=W, padx=10)

        global first_name_box2
        # Create Entry Boxes
        first_name_box2 = Entry(search_customers)
        first_name_box2.grid(row=index + 1, column=1, pady=10)
        first_name_box2.insert(0, result2[0][0])
        global last_name_box2
        last_name_box2 = Entry(search_customers)
        last_name_box2.grid(row=index + 2, column=1, pady=5)
        last_name_box2.insert(0, result2[0][1])
        global address1_box2
        address1_box2 = Entry(search_customers)
        address1_box2.grid(row=index + 3, column=1, pady=5)
        address1_box2.insert(0, result2[0][2])
        global address2_box2
        address2_box2 = Entry(search_customers)
        address2_box2.grid(row=index + 4, column=1, pady=5)
        address2_box2.insert(0, result2[0][3])
        global city_box2
        city_box2 = Entry(search_customers)
        city_box2.grid(row=index + 5, column=1, pady=5)
        city_box2.insert(0, result2[0][4])
        global state_box2
        state_box2 = Entry(search_customers)
        state_box2.grid(row=index + 6, column=1, pady=5)
        state_box2.insert(0, result2[0][5])
        global zipcode_box2
        zipcode_box2 = Entry(search_customers)
        zipcode_box2.grid(row=index + 7, column=1, pady=5)
        zipcode_box2.insert(0, result2[0][6])
        global country_box2
        country_box2 = Entry(search_customers)
        country_box2.grid(row=index + 8, column=1, pady=5)
        country_box2.insert(0, result2[0][7])
        global phone_box2
        phone_box2 = Entry(search_customers)
        phone_box2.grid(row=index + 9, column=1, pady=5)
        phone_box2.insert(0, result2[0][8])
        global email_box2
        email_box2 = Entry(search_customers)
        email_box2.grid(row=index + 10, column=1, pady=5)
        email_box2.insert(0, result2[0][9])
        global payment_method_box2
        payment_method_box2 = Entry(search_customers)
        payment_method_box2.grid(row=index + 11, column=1, pady=5)
        payment_method_box2.insert(0, result2[0][10])
        global discount_code_box2
        discount_code_box2 = Entry(search_customers)
        discount_code_box2.grid(row=index + 12, column=1, pady=5)
        discount_code_box2.insert(0, result2[0][11])
        global price_paid_box2
        price_paid_box2 = Entry(search_customers)
        price_paid_box2.grid(row=index + 13, column=1, pady=5)
        price_paid_box2.insert(0, result2[0][12])
        
        save_record = Button(search_customers, text="Update Record", command=update)
        save_record.grid(row=index+15, column=0, padx=10)
    
    def search_now():
        selected = drop.get()
        if selected == "Search by...":
            test = Label(search_customers, text="Hey! You forgot to pick a search")
            test.grid(row=2, column=0)
        if selected == "Last Name":
            sql = "SELECT * FROM customers WHERE last_name=?"

        if selected == "Email Address":
            sql = "SELECT * FROM customers WHERE email=?"

        if selected == "Customer ID":
            sql = "SELECT * FROM customers WHERE ROWID=?"   
        
        searched = search_box.get()
        # sql = "SELECT * FROM customers WHERE last_name=?"
        name = (searched,)
        result = my_cursor.execute(sql, name)
        # Transform the query in to a list
        result = my_cursor.fetchall()

        if not result:
            result = "Record Not Found..."
            searched_label = Label(search_customers, text=result)
            searched_label.grid(row=2, column=0, padx=10, columnspan=2)
        else:
            for index, customer in enumerate(result):
                num_column = 0
                index += 2
                id_reference = 1
                edit_button = Button(search_customers, text="Edit", command=lambda: edit_now(id_reference, index))
                edit_button.grid(row=index, column=num_column)
                for y in customer:
                    lookup_label = Label(search_customers, text=y)
                    lookup_label.grid(row=index, column=num_column+1)
                    num_column += 1 

            
            csv_button = Button(search_customers, text="Save to Excel", command=lambda: write_to_csv(result))
            csv_button.grid(row=index+1, column=0)
        
        # searched_label = Label(search_customers, text=result)
        # searched_label.grid(row=3, column=0, padx=10, columnspan=2)
        

    # Entry box search for customer
    search_box = Entry(search_customers)
    search_box.grid(row=0, column=1, padx=10, pady=10)
    # Entry box label
    search_box_label = Label(search_customers, text="Search Customer")
    search_box_label.grid(row=0, column=0, padx=10, pady=10)
    # Entry box search Button for Customer
    search_button = Button(search_customers, text="Search Customers", command=search_now)
    search_button.grid(row=1, column=0, padx=10)

    # Drop Down Box
    drop = ttk.Combobox(search_customers, value=["Search by...", "Last Name", "Email Address", "Customer Id"])
    drop.current(0)
    drop.grid(row=0, column=2)

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

# List customers Button
list_customers_button = Button(root, text="List Customer", command=list_customers)
list_customers_button.grid(row=15, column=0, sticky=W, padx=10)

# Search Customers
search_customers_button = Button(root, text="Search/Edit Customers", command=search_customers)
search_customers_button.grid(row=15, column=1, sticky=W, padx=10)



my_db.commit()
mainloop()


my_db.close()
