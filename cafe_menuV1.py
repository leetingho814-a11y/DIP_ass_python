# created by JEFF LEE

# This the program for school cafe system

# They can creat acc, login, order food and drink,customise their order, view their order, and save invoice
# (it will save thier time to line up and order unline.)

# Credits: 
# https://lingojam.com/FancyTextGenerator (for the special text)
# https://docs.python.org/3/library/random.html (for random number)



#importing libraries
import math
import tkinter as tk
from tkinter import messagebox
import random

# list
accounts = {}
orders = []
current_custom = {}


# start_page
root = tk.Tk()          
root.title("Cafe Menu")
root.geometry("3000x2000")
root.configure(bg="#faedcd")

# Add a Title
label = tk.Label(root, text="𝓦𝓮𝓵𝓸𝓬𝓶 𝓽𝓸 𝓽𝓱𝓮 𝓒𝓪𝓯𝓮!", font=("Arial", 80),bg="#faedcd")
label.pack(pady=20)


# login page function
def login_page(old_window):
    old_window.withdraw()       # hide the old window that user was in
    login_p = tk.Toplevel()     # create window
    login_p.title("Login Page")
    login_p.geometry("3000x2000")
    login_p.configure(bg="#faedcd")

    tk.Label(login_p, text="𝓛𝓸𝓰𝓲𝓷 𝓹𝓪𝓰𝓮", font=("Arial", 40), bg="#faedcd")\
        .grid(row=0, column=0, columnspan=2, pady=20)

    tk.Label(login_p, text="Username:", font=("Arial", 30), bg="#faedcd")\
        .grid(row=1, column=0, padx=50, pady=10, sticky="e")
    username_entry = tk.Entry(login_p, font=("Arial", 30), bg="#d4a373")
    username_entry.grid(row=1, column=1, padx=20)

    tk.Label(login_p, text="Password:", font=("Arial", 30), bg="#faedcd")\
        .grid(row=2, column=0, padx=50, pady=10, sticky="e")
    password_entry = tk.Entry(login_p, font=("Arial", 30), show="*", bg="#d4a373")
    password_entry.grid(row=2, column=1, padx=20)

    #login system
    def login():
        user = username_entry.get()     # get the username inputed
        pwd = password_entry.get()      # get the password inputed

        # Check saved accounts
        if user in accounts and accounts[user] == pwd:
            messagebox.showinfo("Login Success", f"Welcome, {user}!")
            menu_page(login_p)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    
    login_btn = tk.Button(login_p, text="𝓛𝓸𝓰𝓲𝓷", command=login,font=(30), bg="#d4a373",)
    login_btn.grid(row=3, column=1, pady=10)
    back_btn = tk.Button(login_p, text="𝘽𝙖𝙘𝙠", command=lambda: main_page(login_p),font=(30), bg="#d4a373")
    back_btn.grid(row=4, column=1, pady=10)

login_p_enter = tk.Button(root, text="𝓛𝓸𝓰𝓲𝓷 𝓹𝓪𝓰𝓮", command=lambda: login_page(root),width=70, height=2, font=(30), fg="white", bg="#d4a373")
login_p_enter.pack(pady=70)


# Sign up page function
def signup_page(old_window):
    old_window.withdraw()       # hide the old window that user was in
    signup_p = tk.Toplevel()    # create window
    signup_p.title("Sign Up Page")
    signup_p.geometry("3000x2000")
    signup_p.configure(bg="#faedcd")

    tk.Label(signup_p, text="𝓢𝓲𝓰𝓷𝓾𝓹 𝓹𝓪𝓰𝓮", font=("Arial", 40), bg="#faedcd")\
        .grid(row=0, column=0, columnspan=2, pady=20)

    tk.Label(signup_p, text="Username:", font=("Arial", 30), bg="#faedcd")\
        .grid(row=1, column=0, padx=50, pady=10, sticky="e")
    username_entry = tk.Entry(signup_p, font=("Arial", 30), bg="#d4a373")
    username_entry.grid(row=1, column=1, padx=20)

    tk.Label(signup_p, text="Password:", font=("Arial", 30), bg="#faedcd")\
        .grid(row=2, column=0, padx=50, pady=10, sticky="e")
    password_entry = tk.Entry(signup_p, font=("Arial", 30), show="*", bg="#d4a373")
    password_entry.grid(row=2, column=1, padx=20)

    # signup system
    def signup():
        user = username_entry.get()
        pwd = password_entry.get()

        # Check username already in account or not
        if user in accounts:
            messagebox.showerror("Sign Up Failed", "Username already exists")
            return

        # Save new account
        accounts[user] = pwd
        messagebox.showinfo("Success", "Account created successfully!")
        

    signup_btn = tk.Button(signup_p, text="𝓢𝓲𝓰𝓷𝓾𝓹", command=signup,font=(30), bg="#d4a373")
    signup_btn.grid(row=3, column=1, pady=10)
    back_btn = tk.Button(signup_p, text="𝘽𝙖𝙘𝙠", command=lambda: main_page(signup_p),font=(30), bg="#d4a373")
    back_btn.grid(row=4, column=1, pady=10)

signup_p_enter = tk.Button(root, text="𝓢𝓲𝓰𝓷𝓾𝓹 𝓹𝓪𝓰𝓮", command=lambda: signup_page(root),width=70, height=2, font=(30), fg="white", bg="#d4a373")
signup_p_enter.pack(pady=70)


# View my order page 
def view_order_page(old_window):
    old_window.withdraw()       # hide the old window that user was in
    order_window = tk.Toplevel()        # create window
    order_window.title("View My Order")
    order_window.geometry("3000x2000")
    order_window.configure(bg="#faedcd")

    tk.Label(order_window, text="𝓥𝓲𝓮𝔀 𝓨𝓸𝓾𝓻 𝓞𝓻𝓭𝓮r", font=("Arial", 40), bg="#faedcd").pack(pady=20)

    canvas = tk.Canvas(order_window, width=1200, height=700, bg="#ffffff", highlightthickness=0)
    canvas.pack()

    canvas.create_rectangle(50, 50, 1150, 650, fill="#faedcd", outline="#d4a373", width=5)
    y = 100         # first item position of y
    for item in orders:             # put the current order in window

        # Order number
        canvas.create_text(100, y, text=f"Order #{item['Order Number']}", anchor="w",font=("Arial", 28, "bold"), fill="black")
        y += 40
        canvas.create_text(100, y, text="-----------------------------", anchor="w",font=("Arial", 20), fill="black")
        y += 30

        # Item name
        if "item" in item:
            canvas.create_text(100, y, text=item["item"], anchor="w",font=("Arial", 24), fill="black")
            y += 35

        # Customizations
        if "Cold" in item:
            canvas.create_text(120, y, text=f"Cold: {item['Cold']}", anchor="w", font=("Arial", 20))
            y += 30

        if "Hot" in item:
            canvas.create_text(120, y, text=f"Hot: {item['Hot']}", anchor="w", font=("Arial", 20))
            y += 30

        if "Ice" in item:
            canvas.create_text(120, y, text=f"Ice: {item['Ice']}", anchor="w", font=("Arial", 20))
            y += 30

        if "Extra Shot" in item:
            canvas.create_text(120, y, text=f"Extra Shot: {item['Extra Shot']}", anchor="w", font=("Arial", 20))
            y += 30

        if "Toasted" in item:
            canvas.create_text(120, y, text=f"Toasted: {item['Toasted']}", anchor="w", font=("Arial", 20))
            y += 30

        if "Cheese" in item:
            canvas.create_text(120, y, text=f"Cheese: {item['Cheese']}", anchor="w", font=("Arial", 20))
            y += 30

        if "Sauce" in item:
            canvas.create_text(120, y, text=f"Sauce: {item['Sauce']}", anchor="w", font=("Arial", 20))
            y += 30

        canvas.create_text(100, y, text="-----------------------------", anchor="w",font=("Arial", 20), fill="black")
        y += 50    # gap between orders

    tk.Button(order_window, text="𝙂𝙤 𝙋𝙖𝙮", command=lambda: payment_page(order_window),font=(30), bg="#d4a373").pack(pady=1)
    tk.Button(order_window, text="𝘽𝙖𝙘𝙠", command=lambda: menu_page(order_window),font=(30), bg="#d4a373").pack(padx=20)

# Payment page 
def payment_page(old_window):
    old_window.withdraw()       # hide the old window that user was in
    payment_p = tk.Toplevel()      # create window
    payment_p.title("Payment Page")
    payment_p.geometry("3000x2000")
    payment_p.configure(bg="#faedcd")

    tk.Label(payment_p, text="𝓟𝓪𝔂𝓶𝓮𝓷𝓽 𝓟𝓪𝓰𝓮", font=("Arial", 40), bg="#faedcd")\
        .grid(row=0, column=0, columnspan=2, pady=50, padx=200)
    
    credit = tk.Button(payment_p, text="𝘾𝙧𝙚𝙙𝙞𝙩", font=(30), fg="black", bg="#d4a373",width=40, height=4)
    credit.place(x=100, y=200)
    cash = tk.Button(payment_p, text="𝘾𝙖𝙨𝙝", font=(30), fg="black", bg="#d4a373",width=40, height=4)
    cash.place(x=600, y=200)
    sc = tk.Button(payment_p, text="𝙎𝙩𝙪𝙙𝙚𝙣𝙩 𝘾𝙖𝙧𝙙", font=(30), fg="black", bg="#d4a373",width=85, height=4)
    sc.place(x=100, y=400)
    tk.Label(payment_p, text="𝙎𝙩𝙪𝙙𝙚𝙣𝙩 𝘾𝙖𝙧𝙙 𝙉𝙪𝙢𝙗𝙚𝙧", font=("Arial", 20), bg="#faedcd").place(x=100, y=550)
    username_entry = tk.Entry(payment_p, font=("Arial", 30), bg="#d4a373")
    username_entry.place(x=100, y=600)

    finish_btn = tk.Button(payment_p, text="𝙁𝙞𝙣𝙞𝙨𝙝", command=lambda: finish_page(payment_p),font=(30), bg="#d4a373")   
    finish_btn.place(x=650, y=800)
    back_btn = tk.Button(payment_p, text="𝘽𝙖𝙘𝙠", command=lambda: menu_page(payment_p),font=(30), bg="#d4a373")
    back_btn.place(x=750, y=800)

# Finish page
def finish_page(old_window):
    old_window.withdraw()
    fin_p = tk.Toplevel()
    fin_p.title("Finish Page")
    fin_p.geometry("3000x2000")
    fin_p.configure(bg="#faedcd")
    label = tk.Label(fin_p, text="𝙏𝙝𝙖𝙣𝙠 𝙮𝙤𝙪 𝙛𝙤𝙧 𝙤𝙧𝙙𝙚𝙧, 𝙨𝙚𝙚 𝙮𝙤𝙪 𝙨𝙤𝙤𝙣!", font=("Arial", 50),bg="#faedcd")
    label.pack(pady=20)

    finish_btn = tk.Button(fin_p, text="𝙁𝙞𝙣𝙞𝙨𝙝", command=fin_p.destroy,font=(30), bg="#d4a373")       # destroy page
    finish_btn.place(x=650, y=800)
    backtomain_btn = tk.Button(fin_p, text="𝘽𝙖𝙘𝙠 𝙏𝙤 𝙈𝙖𝙞𝙣", command=lambda: main_page(fin_p),font=(30), bg="#d4a373")
    backtomain_btn.place(x=750, y=800)

# Customize page 
def customize_d_page(old_window, drink_name="item"):
    old_window.withdraw()       # hide the old window that user was in
    custd_p = tk.Toplevel()      # create window
    custd_p.title("Customize Page")
    custd_p.geometry("3000x2000")
    custd_p.configure(bg="#faedcd")

    tk.Label(custd_p, text="𝓒𝓾𝓼𝓽𝓸𝓶𝓲𝔃𝓮 𝓟𝓪𝓰𝓮", font=("Arial", 40), bg="#faedcd")\
        .grid(row=0, column=0, columnspan=2, pady=50, padx=200)
    
    # reset the customisation for each item
    global c_custom
    c_custom = {"item": drink_name}
    
    cold = tk.Button(custd_p, text="𝘾𝙤𝙡𝙙", font=(30), fg="black", bg="#d4a373",command=lambda: c_custom.update({"Cold": "Yes"}),width=40, height=4)
    cold.place(x=100, y=200)
    hot = tk.Button(custd_p, text="𝙃𝙤𝙩", font=(30), fg="black", bg="#d4a373",command=lambda: c_custom.update({"Hot": "Yes"}),width=40, height=4)
    hot.place(x=600, y=200)

    n_ice = tk.Button(custd_p, text="𝙉𝙤 𝙄𝘾𝙀", font=(30), fg="black", bg="#d4a373",command=lambda: c_custom.update({"Ice": "No"}),width=30, height=4)
    n_ice.place(x=100, y=370)
    normal_ice = tk.Button(custd_p, text="𝙉𝙤𝙧𝙢𝙖𝙡 𝙄𝘾𝙀", font=(30), fg="black", bg="#d4a373",command=lambda: c_custom.update({"Ice": "Normal"}),width=30, height=4)
    normal_ice.place(x=500, y=370)
    extra_ice = tk.Button(custd_p, text="𝙀𝙭𝙩𝙧𝙖 𝙄𝘾𝙀", font=(30), fg="black", bg="#d4a373",command=lambda: c_custom.update({"Ice": "Extra"}),width=30, height=4)
    extra_ice.place(x=900, y=370)

    n_hot = tk.Button(custd_p, text="𝙉𝙤 𝙃𝙊𝙏", font=(30), fg="black", bg="#d4a373",command=lambda: c_custom.update({"Hot": "No"}),width=30, height=4)
    n_hot.place(x=100, y=550)
    normal_hot = tk.Button(custd_p, text="𝙉𝙤𝙧𝙢𝙖𝙡 𝙃𝙊𝙏", font=(30), fg="black", bg="#d4a373",command=lambda: c_custom.update({"Hot": "Normal"}),width=30, height=4)
    normal_hot.place(x=500, y=550)
    extra_hot = tk.Button(custd_p, text="𝙀𝙭𝙩𝙧𝙖 𝙃𝙊𝙏", font=(30), fg="black", bg="#d4a373",command=lambda: c_custom.update({"Hot": "Extra"}),width=30, height=4)
    extra_hot.place(x=900, y=550)

    add_btn = tk.Button(custd_p, text="𝙀𝙭𝙩𝙧𝙖 𝙨𝙝𝙤𝙩 (+$1.00)", command=lambda: c_custom.update({"Extra Shot": "Yes"}),font=(15), bg="#d4a373")
    add_btn.place(x=660, y=700)
    
    # save item system
    def save_item():
        # make random number in 100 to 999
        order_num = random.randint(100, 999)

        c_custom["Order Number"] = order_num        # add order number

        orders.append(c_custom.copy())      # add custom to order list

        messagebox.showinfo("Saved", f"Item added! Order #{order_num}")
        menu_page(custd_p)

    add_btn = tk.Button(custd_p, text="𝘼𝙙𝙙 𝙄𝙩𝙚𝙢", command=save_item,font=(30), bg="#d4a373")
    add_btn.place(x=700, y=800)

def customize_f_page(old_window, food_name="item"):
    old_window.withdraw()       # hide the old window that user was in
    custF_p = tk.Toplevel()      # create window    
    custF_p.title("Customize Page")
    custF_p.geometry("3000x2000")
    custF_p.configure(bg="#faedcd")

    tk.Label(custF_p, text="𝓒𝓾𝓼𝓽𝓸𝓶𝓲𝔃𝓮 𝓟𝓪𝓰𝓮", font=("Arial", 40), bg="#faedcd")\
        .grid(row=0, column=0, columnspan=2, pady=50, padx=200)
    
    #reset the customisation for each item
    global c_custom
    c_custom = {"item": food_name}
    
    toasted = tk.Button(custF_p, text="𝙏𝙤𝙖𝙨𝙩𝙚𝙙", font=(30), fg="black", bg="#d4a373",command=lambda: c_custom.update({"Toasted": "Yes"}),width=40, height=4)
    toasted.place(x=100, y=200)
    Ntoasted = tk.Button(custF_p, text="𝙉𝙤 𝙏𝙤𝙖𝙨𝙩𝙚𝙙", font=(30), fg="black", bg="#d4a373",command=lambda: c_custom.update({"Toasted": "No"}),width=40, height=4)
    Ntoasted.place(x=600, y=200)

    cheese = tk.Button(custF_p, text="𝘾𝙝𝙚𝙚𝙨𝙚", font=(30), fg="black", bg="#d4a373",command=lambda: c_custom.update({"Cheese": "Yes"}),width=40, height=4)
    cheese.place(x=100, y=370)
    Ncheese = tk.Button(custF_p, text="𝙉𝙤 𝘾𝙝𝙚𝙚𝙨𝙚", font=(30), fg="black", bg="#d4a373",command=lambda: c_custom.update({"Cheese": "No"}),width=40, height=4)
    Ncheese.place(x=600, y=370)

    Nsauce = tk.Button(custF_p, text="𝙉𝙤 𝙎𝙖𝙪𝙘𝙚", font=(25), fg="black", bg="#d4a373",command=lambda: c_custom.update({"Sauce": "No"}),width=20, height=4)
    Nsauce.place(x=100, y=550)
    sauce_b= tk.Button(custF_p, text="𝘽𝘽𝙌 𝙎𝙖𝙪𝙘𝙚", font=(25), fg="black", bg="#d4a373",command=lambda: c_custom.update({"Sauce": "BBQ"}),width=20, height=4)
    sauce_b.place(x=350, y=550)
    sauce_t= tk.Button(custF_p, text="𝙏𝙤𝙢𝙖𝙩𝙤 𝙎𝙖𝙪𝙘𝙚", font=(25), fg="black", bg="#d4a373",command=lambda: c_custom.update({"Sauce": "Tomato"}),width=20, height=4)
    sauce_t.place(x=600, y=550)
    sauce_w= tk.Button(custF_p, text="𝙒𝙝𝙞𝙩𝙚 𝙎𝙖𝙪𝙘𝙚", font=(25), fg="black", bg="#d4a373",command=lambda: c_custom.update({"Sauce": "White"}),width=20, height=4)
    sauce_w.place(x=850, y=550)
    sauce_m= tk.Button(custF_p, text="𝙈𝙖𝙮𝙤 𝙎𝙖𝙪𝙘𝙚", font=(25), fg="black", bg="#d4a373",command=lambda: c_custom.update({"Sauce": "Mayo"}),width=20, height=4)
    sauce_m.place(x=1100, y=550)

    # save item system
    def save_item():
        # make random number in 100 to 999
        order_num = random.randint(100, 999)

        c_custom["Order Number"] = order_num        # add order number to customisation

        orders.append(c_custom.copy())      # add customisation to the order list
        messagebox.showinfo("Saved", "Item added to your order!")
        menu_page(custF_p)

    add_btn = tk.Button(custF_p, text="𝘼𝙙𝙙 𝙄𝙩𝙚𝙢", command=save_item,font=(30), bg="#d4a373")
    add_btn.place(x=700, y=800)

# Menu page 2(food)
def menu_page2(old_window):
    old_window.withdraw()       # hide the old window that user was in
    menu2_p = tk.Toplevel()     # create window
    menu2_p.title("Menu Page")
    menu2_p.geometry("3000x2000")
    menu2_p.configure(bg="#faedcd")

    tk.Label(menu2_p, text="𝓜𝓮𝓷𝓾 𝓟𝓪𝓰𝓮【２】\n𝓕𝓸𝓸𝓭", font=("Arial", 40), bg="#faedcd")\
        .grid(row=0, column=0, columnspan=2, pady=20)

    canvas = tk.Canvas(menu2_p, width=960, height=600, bg="#d4aa73")
    canvas.grid(row=1, column=1, pady=20, padx=270,)

    # item 1
    canvas.create_rectangle(50, 50, 450, 270, fill="#faedcd", outline="black")

    item = tk.Label(menu2_p, text="𝘽𝙪𝙧𝙜𝙚𝙧", font=("Arial", 20),bg="#faedcd")
    btn = tk.Button(menu2_p, text="𝘾𝙪𝙨𝙩𝙤𝙢𝙞𝙯𝙚", bg="#d4aa73", fg="white", font=("Arial", 20), command=lambda: customize_f_page(menu2_p,"𝘽𝙪𝙧𝙜𝙚𝙧"))

    canvas.create_window(250, 120, window=item) 
    canvas.create_window(250, 200, window=btn)

    # item 2
    canvas.create_rectangle(500, 50, 900, 270, fill="#faedcd", outline="black")

    item2 = tk.Label(menu2_p, text="𝙎𝙖𝙣𝙙𝙬𝙞𝙘𝙝", font=("Arial", 20), bg="#faedcd")
    btn2 = tk.Button(menu2_p, text="𝘾𝙪𝙨𝙩𝙤𝙢𝙞𝙯𝙚", bg="#d4aa73", fg="white", font=("Arial", 20), command=lambda: customize_f_page(menu2_p,"𝙎𝙖𝙣𝙙𝙬𝙞𝙘𝙝"))

    canvas.create_window(700, 120, window=item2)
    canvas.create_window(700, 200, window=btn2)

    # item 3
    canvas.create_rectangle(50, 300, 450, 530, fill="#faedcd", outline="black")

    item3 = tk.Label(menu2_p, text="𝙘𝙝𝙤𝙘𝙤𝙡𝙖𝙩𝙚 𝙘𝙖𝙠𝙚", font=("Arial", 20),bg="#faedcd")
    btn3 = tk.Button(menu2_p, text="𝘾𝙪𝙨𝙩𝙤𝙢𝙞𝙯𝙚", bg="#d4aa73", fg="white", font=("Arial", 20), command=lambda: customize_f_page(menu2_p,"𝙘𝙝𝙤𝙘𝙤𝙡𝙖𝙩𝙚 𝙘𝙖𝙠𝙚"))

    canvas.create_window(250, 370, window=item3) 
    canvas.create_window(250, 450, window=btn3)

    # item 4
    canvas.create_rectangle(500, 300, 900, 530, fill="#faedcd", outline="black")

    item4 = tk.Label(menu2_p, text="𝙈𝙪𝙛𝙛𝙞𝙣", font=("Arial", 20), bg="#faedcd")
    btn4 = tk.Button(menu2_p, text="𝘾𝙪𝙨𝙩𝙤𝙢𝙞𝙯𝙚", bg="#d4aa73", fg="white", font=("Arial", 20), command=lambda: customize_f_page(menu2_p,"𝙈𝙪𝙛𝙛𝙞𝙣"))

    canvas.create_window(700, 370, window=item4)
    canvas.create_window(700, 450, window=btn4)

    back_btn = tk.Button(menu2_p, text="<", command=lambda: menu_page(menu2_p),font=(40), bg="#d4a373")
    back_btn.place(x=100, y=400)
    vop_btn = tk.Button(menu2_p, text="𝙑𝙄𝙀𝙒 𝙊𝙍𝘿𝙀𝙍", command=lambda: view_order_page(menu2_p),font=(30), bg="#d4a373")
    vop_btn.place(x=670, y=825)

# Menu page 1(drink)
def menu_page(old_window):
    old_window.withdraw()
    menu_p = tk.Toplevel()
    menu_p.title("Menu Page")
    menu_p.geometry("3000x2000")
    menu_p.configure(bg="#faedcd")

    tk.Label(menu_p, text="𝓜𝓮𝓷𝓾 𝓟𝓪𝓰𝓮【１】\n𝓓𝓻𝓲𝓷𝓴𝓼", font=("Arial", 40), bg="#faedcd")\
        .grid(row=0, column=0, columnspan=2, pady=20)

    canvas = tk.Canvas(menu_p, width=960, height=600, bg="#d4aa73")
    canvas.grid(row=1, column=1, pady=20, padx=270,)

    # item 1
    canvas.create_rectangle(50, 50, 450, 270, fill="#faedcd", outline="black")

    item = tk.Label(menu_p, text="𝙃𝙤𝙩 𝘾𝙝𝙤𝙘𝙤𝙡𝙖𝙩𝙚", font=("Arial", 20),bg="#faedcd")
    btn = tk.Button(menu_p, text="𝘾𝙪𝙨𝙩𝙤𝙢𝙞𝙯𝙚", bg="#d4aa73", fg="white", font=("Arial", 20), command=lambda: customize_d_page(menu_p, "𝙃𝙤𝙩 𝘾𝙝𝙤𝙘𝙤𝙡𝙖𝙩𝙚"))

    canvas.create_window(250, 120, window=item) 
    canvas.create_window(250, 200, window=btn)

    # item 2
    canvas.create_rectangle(500, 50, 900, 270, fill="#faedcd", outline="black")

    item2 = tk.Label(menu_p, text="𝘾𝙤𝙛𝙛𝙚𝙚", font=("Arial", 20), bg="#faedcd")
    btn2 = tk.Button(menu_p, text="𝘾𝙪𝙨𝙩𝙤𝙢𝙞𝙯𝙚", bg="#d4aa73", fg="white", font=("Arial", 20), command=lambda: customize_d_page(menu_p, "𝘾𝙤𝙛𝙛𝙚𝙚"))

    canvas.create_window(700, 120, window=item2)
    canvas.create_window(700, 200, window=btn2)

    # item 3
    canvas.create_rectangle(50, 300, 450, 530, fill="#faedcd", outline="black")

    item3 = tk.Label(menu_p, text="𝙈𝙖𝙘𝙝𝙖", font=("Arial", 20),bg="#faedcd")
    btn3 = tk.Button(menu_p, text="𝘾𝙪𝙨𝙩𝙤𝙢𝙞𝙯𝙚", bg="#d4aa73", fg="white", font=("Arial", 20), command=lambda: customize_d_page(menu_p, "𝙈𝙖𝙘𝙝𝙖"))

    canvas.create_window(250, 370, window=item3) 
    canvas.create_window(250, 450, window=btn3)

    # item 4
    canvas.create_rectangle(500, 300, 900, 530, fill="#faedcd", outline="black")

    item4 = tk.Label(menu_p, text="𝙏𝙚𝙖", font=("Arial", 20), bg="#faedcd")
    btn4 = tk.Button(menu_p, text="𝘾𝙪𝙨𝙩𝙤𝙢𝙞𝙯𝙚", bg="#d4aa73", fg="white", font=("Arial", 20), command=lambda: customize_d_page(menu_p, "𝙏𝙚𝙖"))

    canvas.create_window(700, 370, window=item4)
    canvas.create_window(700, 450, window=btn4)

    back_btn = tk.Button(menu_p, text="<", command=lambda: login_page(menu_p),font=(40), bg="#d4a373")
    back_btn.place(x=100, y=400)
    next_btn = tk.Button(menu_p, text=">", command=lambda: menu_page2(menu_p),font=(40), bg="#d4a373")
    next_btn.place(x=1350, y=400)
    vop_btn = tk.Button(menu_p, text="𝙑𝙄𝙀𝙒 𝙊𝙍𝘿𝙀𝙍", command=lambda: view_order_page(menu_p),font=(30), bg="#d4a373")
    vop_btn.place(x=670, y=825)

    
# Main page
def main_page(old_window):
    old_window.withdraw()
    main_p = tk.Toplevel()
    main_p.title("Cafe Menu")
    main_p.geometry("3000x2000")
    main_p.configure(bg="#faedcd")
    label = tk.Label(main_p, text="𝓦𝓮𝓵𝓸𝓬𝓶 𝓽𝓸 𝓽𝓱𝓮 𝓒𝓪𝓯𝓮!", font=("Arial", 80),bg="#faedcd")
    label.pack(pady=20)
    
    login_p_enter2 = tk.Button(main_p, text="𝓛𝓸𝓰𝓲𝓷 𝓹𝓪𝓰𝓮", command=lambda: login_page(main_p),width=70, height=2, font=(30), fg="white", bg="#d4a373")
    login_p_enter2.pack(pady=70)
    signup_p_enter2 = tk.Button(main_p, text="𝓢𝓲𝓰𝓷𝓾𝓹 𝓹𝓪𝓰𝓮", command=lambda: signup_page(main_p),width=70, height=2, font=(30), fg="white", bg="#d4a373")
    signup_p_enter2.pack(pady=70)

# Start the loop
if __name__ == "__main__":
    root.mainloop()
