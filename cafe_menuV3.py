# created by JEFF LEE

# This the program for school cafe system

# They can creat acc, login, order food and drink,customise their order, view their order, and save invoice
# (it will save thier time to line up and order unline.)

# Credits: 
# https://lingojam.com/FancyTextGenerator (for the special text)
# https://docs.python.org/3/library/random.html (for random number)
# https://emojipedia.org/wastebasket (for rubblish bin emoji)
# https://www.w3schools.com/python/ref_string_isdigit.asp (for isdigit)
# https://carpedm20.github.io/emoji/ (for eye emoji)
# https://realpython.com/ref/keywords/global/ (for global)
# https://emojidb.org/python-emojis (for item emojis)
# https://www.geeksforgeeks.org/python/python-tkinter-scrollbar/ (for scrollbar in view order page)

#importing libraries
import tkinter as tk
from tkinter import messagebox
import datetime as dt

# list
accounts = {}
orders = []
current_custom = {}


# set value
total_price = 0
receipt_num = 1
payment_type = ""

# start_page
root = tk.Tk()          
root.title("Cafe Menu")
root.geometry("3000x2000")
root.configure(bg="#faedcd")
# Add a Title
label = tk.Label(root, text="𝓦𝓮𝓵𝓬𝓸𝓶𝓮 𝓽𝓸 𝓽𝓱𝓮 𝓒𝓪𝓯𝓮!", font=("Arial", 80),bg="#faedcd")
label.pack(pady=20)
# signup button in start page
signup_p_enter = tk.Button(root, text="𝓢𝓲𝓰𝓷𝓾𝓹 𝓹𝓪𝓰𝓮", command=lambda: signup_page(root),width=70, height=2, font=(30), fg="white", bg="#d4a373")
signup_p_enter.pack(pady=120)
# login button in start page
login_p_enter = tk.Button(root, text="𝓛𝓸𝓰𝓲𝓷 𝓹𝓪𝓰𝓮", command=lambda: login_page(root),width=70, height=2, font=(30), fg="white", bg="#d4a373")
login_p_enter.pack(pady=120)


# login page function
def login_page(old_window):
    old_window.withdraw()       # hide the old window that user was in
    login_p = tk.Toplevel()     # create window
    login_p.title("Login Page")
    login_p.geometry("3000x2000")
    login_p.configure(bg="#faedcd")

    tk.Label(login_p, text="𝓛𝓸𝓰𝓲𝓷 𝓹𝓪𝓰𝓮", font=("Arial", 40), bg="#faedcd").place(x=600, y=50)

    tk.Label(login_p, text="𝙐𝙨𝙚𝙧𝙣𝙖𝙢𝙚", font=("Arial", 30), bg="#faedcd").place(x=670, y=250)
    username_entry = tk.Entry(login_p, font=("Arial", 30), bg="#d4a373")
    username_entry.place(x=540, y=330)

    tk.Label(login_p, text="𝙋𝙖𝙨𝙨𝙬𝙤𝙧𝙙", font=("Arial", 30), bg="#faedcd").place(x=670, y=450)
    password_entry = tk.Entry(login_p, font=("Arial", 30), show="*", bg="#d4a373")
    password_entry.place(x=540, y=530)

    # Show Password system
    def show_ps():
        if password_entry.cget("show") == "":       # check is the password is showing or not
            password_entry.config(show="*")
        else:
            password_entry.config(show="")
    
    #login system
    def login():
        user = username_entry.get()     # get the username inputed
        pwd = password_entry.get()      # get the password inputed

        # Check saved accounts
        if user in accounts and accounts[user] == pwd:
            messagebox.showinfo("Login Success", f"Welcome, {user}!\nclick ok to menu page")
            menu_page(login_p)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password\nclick ok to try again")

    eye_btn = tk.Button(login_p, text="👁", command=lambda: show_ps(),font=(30), bg="#d4a373")
    eye_btn.place(x=990, y=533)
    login_btn = tk.Button(login_p, text="𝓛𝓸𝓰𝓲𝓷", command=login,font=(30), bg="#d4a373",)
    login_btn.place(x=700, y=650)
    back_btn = tk.Button(login_p, text="𝙓", command=lambda: main_page(login_p),font=(30), bg="#d4a373")
    back_btn.place(x=1400, y=65)


# Sign up page function
def signup_page(old_window):
    old_window.withdraw()       # hide the old window that user was in
    signup_p = tk.Toplevel()    # create window
    signup_p.title("Sign Up Page")
    signup_p.geometry("3000x2000")
    signup_p.configure(bg="#faedcd")

    tk.Label(signup_p, text="𝓢𝓲𝓰𝓷𝓾𝓹 𝓹𝓪𝓰𝓮", font=("Arial", 40), bg="#faedcd").place(x=600, y=50)

    tk.Label(signup_p, text="𝙐𝙨𝙚𝙧𝙣𝙖𝙢𝙚", font=("Arial", 30), bg="#faedcd").place(x=670, y=250)
    username_entry = tk.Entry(signup_p, font=("Arial", 30), bg="#d4a373")
    username_entry.place(x=540, y=330)

    tk.Label(signup_p, text="𝙋𝙖𝙨𝙨𝙬𝙤𝙧𝙙", font=("Arial", 30), bg="#faedcd").place(x=670, y=450)
    password_entry = tk.Entry(signup_p, font=("Arial", 30), show="*", bg="#d4a373")
    password_entry.place(x=540, y=530)

    # Show Password system
    def show_ps():
        if password_entry.cget("show") == "":       # check is the password is showing or not
            password_entry.config(show="*")
        else:
            password_entry.config(show="")
    
    # signup system
    def signup():
        user = username_entry.get()
        pwd = password_entry.get()

        # Check username already in account or not
        if user in accounts:
            messagebox.showerror("Sign Up Failed", "Username already exists\nclick ok to try again")
            return

        # Save new account
        accounts[user] = pwd
        messagebox.showinfo("Success", "Account created successfully! \nclick ok to hop in login page")
        login_page(signup_p)

    eye_btn = tk.Button(signup_p, text="👁", command=lambda: show_ps(),font=(30), bg="#d4a373")
    eye_btn.place(x=990, y=533)
    signup_btn = tk.Button(signup_p, text="𝓢𝓲𝓰𝓷𝓾𝓹", command=signup,font=(30), bg="#d4a373")
    signup_btn.place(x=700, y=650)
    back_btn = tk.Button(signup_p, text="𝙓", command=lambda: main_page(signup_p),font=(30), bg="#d4a373")
    back_btn.place(x=1400, y=65)


# View my order page 
def view_order_page(old_window):
    old_window.withdraw()       # hide the old window that user was in
    order_window = tk.Toplevel()        # create window
    order_window.title("View My Order")
    order_window.geometry("3000x2000")
    order_window.configure(bg="#faedcd")

    tk.Label(order_window, text="𝓥𝓲𝓮𝔀 𝓨𝓸𝓾𝓻 𝓞𝓻𝓭𝓮𝓻", font=("Arial", 40), bg="#faedcd").pack(pady=20)

    def delete_order(window):
        global receipt_num      # for reset receipt number after delete
        if orders:
            orders.pop()   # remove last item
            messagebox.showinfo("Deleted", "Item removed\nclick ok to next")
            receipt_num  = receipt_num-1     # receipt number -1, fix fixing the error
        else:
            messagebox.showerror("Error", "No items to delete\nclick ok to return")
        window.destroy()    # refresh the page to show the updated order list
        view_order_page(root)

    delete_btn = tk.Button(order_window, text="🗑️ 𝘿𝙚𝙡𝙚𝙩𝙚 𝙤𝙧𝙙𝙚𝙧",command=lambda: delete_order(order_window),font=(30), bg="#d4a373")
    delete_btn.place(x=1150, y=820)
    tk.Button(order_window, text="𝙂𝙤 𝙋𝙖𝙮", command=lambda: payment_m_page(order_window),font=(30), bg="#d4a373").place(x=720, y=820)
    tk.Button(order_window, text="𝙓", command=lambda: menu_page(order_window),font=(30), bg="#d4a373").place(x=1400, y=65)

    # Scrollable canvas
    canvas = tk.Canvas(order_window,width=1200,height=650,bg="#937659")
    scrollbar = tk.Scrollbar(order_window,orient="vertical",command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.place(x=150, y=150)
    scrollbar.pack(side="right", fill="y")

    # Mouse wheel scrolling
    def mouse_scroll(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    canvas.bind_all("<MouseWheel>", mouse_scroll)

    # Background box
    canvas.create_rectangle(50, 50, 1150, 3000,fill="#faedcd",outline="#d4a373",width=5)
    y = 100

    for item in orders:
        canvas.create_text(100, y,text=f"Order #{item['Order Number']}",anchor="w",font=("Arial", 28, "bold"))
        y += 40
        canvas.create_text(100, y,text="-----------------------------",anchor="w",font=("Arial", 20))
        y += 30
        if "item" in item:
            canvas.create_text(100, y,text=item["item"],anchor="w",font=("Arial", 24))
            y += 35
        qty = item.get("Quantity", 1)
        canvas.create_text(120, y,text=f"Quantity: {qty}",anchor="w",font=("Arial", 20))
        y += 35
        canvas.create_text(120, y,text=f"Total Price: ${item['Price']:.2f}",anchor="w",font=("Arial", 20))
        y += 35
        if "Ice" in item:
            canvas.create_text(120, y,text=f"Ice: {item['Ice']}",anchor="w",font=("Arial", 20))
            y += 30
        if "Extra Shot" in item:
            canvas.create_text(120, y,text=f"Extra Shot: {item['Extra Shot']}",anchor="w",font=("Arial", 20))
            y += 30
        if "Toasted" in item:
            canvas.create_text(120, y,text=f"Toasted: {item['Toasted']}",anchor="w",font=("Arial", 20))
            y += 30
        if "Cheese" in item:
            canvas.create_text(120, y,text=f"Cheese: {item['Cheese']}",anchor="w",font=("Arial", 20))
            y += 30
        if "Sauce" in item:
            canvas.create_text(120, y,text=f"Sauce: {item['Sauce']}",anchor="w",font=("Arial", 20))
            y += 30
        canvas.create_text(100, y,text="-----------------------------",anchor="w",font=("Arial", 20))
        y += 50
    # Set scrollable area
    canvas.config(scrollregion=(0, 0, 1200, y + 100))


# Payment main page 
def payment_m_page(old_window):
    try:
        if orders == []:       # check if the order is empty or not
            messagebox.showerror("Error", "Your order is empty, please order something before going to payment page\nclick ok for next")
            return
    except:
        pass
# if the order is not empty, then go to payment page
    old_window.withdraw()       # hide the old window that user was in
    payment_pm = tk.Toplevel()      # create window
    payment_pm.title("Payment Page")
    payment_pm.geometry("3000x2000")
    payment_pm.configure(bg="#faedcd")

    tk.Label(payment_pm, text="𝓟𝓪𝔂𝓶𝓮𝓷𝓽 𝓟𝓪𝓰𝓮", font=("Arial", 40), bg="#faedcd")\
        .grid(row=0, column=0, columnspan=2, pady=50, padx=200)
    
    credit = tk.Button(payment_pm, text="𝘾𝙧𝙚𝙙𝙞𝙩", font=(30), fg="black", bg="#d4a373",width=40, height=4,command=lambda: payment_page(payment_pm))
    credit.place(x=100, y=200)
    cash = tk.Button(payment_pm, text="𝘾𝙖𝙨𝙝", font=(30), fg="black", bg="#d4a373",width=40, height=4,command=lambda: payment_CH_page(payment_pm))
    cash.place(x=600, y=200)
    sc = tk.Button(payment_pm, text="𝙎𝙩𝙪𝙙𝙚𝙣𝙩 𝘾𝙖𝙧d", font=(30), fg="black", bg="#d4a373",width=85, height=4,command=lambda: payment_SC_page(payment_pm))
    sc.place(x=100, y=400)
    tk.Label(payment_pm, text="𝗦𝗲𝗹𝗲𝗰𝘁 𝘁𝗵𝗲 𝗽𝗮𝘆𝗺𝗲𝗻𝘁 𝘆𝗼𝘂 𝘄𝗼𝘂𝗹𝗱 𝗹𝗶𝗸𝗲 𝘁𝗼 𝘂𝘀𝗲", font=("Arial", 20), bg="#faedcd").place(x=100, y=550)

    finish_btn = tk.Button(payment_pm, text="𝙁𝙞𝙣𝙞𝙨𝙝", command=lambda: finish_page(payment_pm),font=(30), bg="#d4a373")   
    finish_btn.place(x=720, y=800)
    back_btn = tk.Button(payment_pm, text="𝙓", command=lambda: view_order_page(payment_pm),font=(30), bg="#d4a373")
    back_btn.place(x=1400, y=65)



# Payment page 
def payment_CH_page(old_window):
    old_window.withdraw()       # hide the old window that user was in
    payment_pch = tk.Toplevel()      # create window
    payment_pch.title("Payment Page")
    payment_pch.geometry("3000x2000")
    payment_pch.configure(bg="#faedcd")

    global payment_type     # global for payment type, so it can be used in other function
    payment_type = "cash"       # set the type as cash

    tk.Label(payment_pch, text="𝓟𝓪𝔂𝓶𝓮𝓷𝓽 𝓟𝓪𝓰𝓮", font=("Arial", 40), bg="#faedcd")\
        .grid(row=0, column=0, columnspan=2, pady=50, padx=200)
    
    credit = tk.Button(payment_pch, text="𝘾𝙧𝙚𝙙𝙞𝙩", font=(30), fg="black", bg="#d4a373",width=40, height=4,command=lambda: payment_page(payment_pch))
    credit.place(x=100, y=200)
    cash = tk.Button(payment_pch, text="𝘾𝙖𝙨𝙝", font=(30), fg="black", bg="#ffffff",width=40, height=4,command=lambda: payment_CH_page(payment_pch))
    cash.place(x=600, y=200)
    sc = tk.Button(payment_pch, text="𝙎𝙩𝙪𝙙𝙚𝙣𝙩 𝘾𝙖𝙧d", font=(30), fg="black", bg="#d4a373",width=85, height=4,command=lambda: payment_SC_page(payment_pch))
    sc.place(x=100, y=400)
    tk.Label(payment_pch, text="𝗖𝗮𝘀𝗵 𝘄𝗶𝗹𝗹 𝗯𝗲 𝗔𝗿𝗿𝗶𝘃𝗲 𝗣𝗮𝘆", font=("Arial", 20), bg="#faedcd").place(x=100, y=550)

    finish_btn = tk.Button(payment_pch, text="𝙁𝙞𝙣𝙞𝙨𝙝", command=lambda: finish_page(payment_pch),font=(30), bg="#d4a373")   
    finish_btn.place(x=720, y=800)
    back_btn = tk.Button(payment_pch, text="𝙓", command=lambda: view_order_page(payment_pch),font=(30), bg="#d4a373")
    back_btn.place(x=1400, y=65)


# Payment page 
def payment_SC_page(old_window):
    old_window.withdraw()       # hide the old window that user was in
    payment_psc = tk.Toplevel()      # create window
    payment_psc.title("Payment Page")
    payment_psc.geometry("3000x2000")
    payment_psc.configure(bg="#faedcd")

    global payment_type         # global payment for using in this function
    payment_type = "student card"     # set the payment type

    tk.Label(payment_psc, text="𝓟𝓪𝔂𝓶𝓮𝓷𝓽 𝓟𝓪𝓰𝓮", font=("Arial", 40), bg="#faedcd")\
        .grid(row=0, column=0, columnspan=2, pady=50, padx=200)
    
    credit = tk.Button(payment_psc, text="𝘾𝙧𝙚𝙙𝙞𝙩", font=(30), fg="black", bg="#d4a373",width=40, height=4,command=lambda: payment_page(payment_psc))
    credit.place(x=100, y=200)
    cash = tk.Button(payment_psc, text="𝘾𝙖𝙨𝙝", font=(30), fg="black", bg="#d4a373",width=40, height=4,command=lambda: payment_CH_page(payment_psc))
    cash.place(x=600, y=200)
    sc = tk.Button(payment_psc, text="𝙎𝙩𝙪𝙙𝙚𝙣𝙩 𝘾𝙖𝙧d", font=(30), fg="black", bg="#ffffff",width=85, height=4,command=lambda: payment_SC_page(payment_psc))
    sc.place(x=100, y=400)
    tk.Label(payment_psc, text="𝗦𝘁𝘂𝗱𝗲𝗻𝘁 𝗖𝗮𝗿𝗱 𝗡𝘂𝗺𝗯𝗲𝗿*", font=("Arial", 20), bg="#faedcd").place(x=100, y=550)
    global student_entry     # global for student card entry, so it can be used in other function
    student_entry = tk.Entry(payment_psc, font=("Arial", 30), bg="#d4a373")
    student_entry.place(x=100, y=600)

    finish_btn = tk.Button(payment_psc, text="𝙁𝙞𝙣𝙞𝙨𝙝", command=lambda: finish_page(payment_psc),font=(30), bg="#d4a373")   
    finish_btn.place(x=720, y=800)
    back_btn = tk.Button(payment_psc, text="𝙓", command=lambda: view_order_page(payment_psc),font=(30), bg="#d4a373")
    back_btn.place(x=1400, y=65)


# Payment page 
def payment_op_page(old_window):
    old_window.withdraw()       # hide the old window that user was in
    payment_po = tk.Toplevel()      # create window
    payment_po.title("Payment Page")
    payment_po.geometry("3000x2000")
    payment_po.configure(bg="#faedcd")

    global payment_type         # global payment for using in this function
    payment_type = "credit"     # set the payment type


    tk.Label(payment_po, text="𝓟𝓪𝔂𝓶𝓮𝓷𝓽 𝓟𝓪𝓰𝓮", font=("Arial", 40), bg="#faedcd")\
        .grid(row=0, column=0, columnspan=2, pady=50, padx=200)
    
    credit = tk.Button(payment_po, text="𝘾𝙧𝙚𝙙𝙞𝙩", font=(30), fg="black", bg="#ffffff",width=40, height=4,command=lambda: payment_op_page(payment_po))
    credit.place(x=100, y=200)
    cash = tk.Button(payment_po, text="𝘾𝙖𝙨𝙝", font=(30), fg="black", bg="#d4a373",width=40, height=4,command=lambda: payment_CH_page(payment_po))
    cash.place(x=600, y=200)
    sc = tk.Button(payment_po, text="𝙎𝙩𝙪𝙙𝙚𝙣𝙩 𝘾𝙖𝙧d", font=(30), fg="black", bg="#d4a373",width=85, height=4,command=lambda: payment_SC_page(payment_po))
    sc.place(x=100, y=400)
    arrive_pay_btn = tk.Button(payment_po, text="𝗔𝗿𝗿𝗶𝘃𝗲 𝗣𝗮𝘆", font=(15), fg="black", bg="#d4a373",width=20, height=2,command=lambda: payment_ap_page(payment_po))
    arrive_pay_btn.place(x=100, y=550)
    Online_pay_btn = tk.Button(payment_po, text="𝗣𝗮𝘆 𝗢𝗻𝗹𝗶𝗻𝗲", font=(15), fg="black", bg="#ffffff",width=20, height=2)
    Online_pay_btn.place(x=400, y=550)
    tk.Label(payment_po, text="𝗖𝗿𝗲𝗱𝗶𝘁 𝗖𝗮𝗿𝗱 𝗡𝘂𝗺𝗯𝗲𝗿*", font=("Arial", 20), bg="#faedcd").place(x=100, y=650)
    global credit_entry     # global for credit card entry, so it can be used in other function
    credit_entry = tk.Entry(payment_po, font=("Arial", 30), bg="#d4a373")
    credit_entry.place(x=100, y=700)
    finish_btn = tk.Button(payment_po, text="𝙁𝙞𝙣𝙞𝙨𝙝", command=lambda: finish_page(payment_po),font=(30), bg="#d4a373")   
    finish_btn.place(x=720, y=800)
    back_btn = tk.Button(payment_po, text="𝙓", command=lambda: view_order_page(payment_po),font=(30), bg="#d4a373")
    back_btn.place(x=1400, y=65)


# Payment page 
def payment_ap_page(old_window):
    old_window.withdraw()       # hide the old window that user was in
    payment_pa = tk.Toplevel()      # create window
    payment_pa.title("Payment Page")
    payment_pa.geometry("3000x2000")
    payment_pa.configure(bg="#faedcd")

    global payment_type         # global payment type for using in this function
    payment_type = "credit"     # set the payment type in credit

    tk.Label(payment_pa, text="𝓟𝓪𝔂𝓶𝓮𝓷𝓽 𝓟𝓪𝓰𝓮", font=("Arial", 40), bg="#faedcd")\
        .grid(row=0, column=0, columnspan=2, pady=50, padx=200)
    
    credit = tk.Button(payment_pa, text="𝘾𝙧𝙚𝙙𝙞𝙩", font=(30), fg="black", bg="#ffffff",width=40, height=4,command=lambda: payment_ap_page(payment_pa))
    credit.place(x=100, y=200)
    cash = tk.Button(payment_pa, text="𝘾𝙖𝙨𝙝", font=(30), fg="black", bg="#d4a373",width=40, height=4,command=lambda: payment_CH_page(payment_pa))
    cash.place(x=600, y=200)
    sc = tk.Button(payment_pa, text="𝙎𝙩𝙪𝙙𝙚𝙣𝙩 𝘾𝙖𝙧d", font=(30), fg="black", bg="#d4a373",width=85, height=4,command=lambda: payment_SC_page(payment_pa))
    sc.place(x=100, y=400)
    arrive_pay_btn = tk.Button(payment_pa, text="𝗔𝗿𝗿𝗶𝘃𝗲 𝗣𝗮𝘆", font=(15), fg="black", bg="#ffffff",width=20, height=2)
    arrive_pay_btn.place(x=100, y=550)
    Online_pay_btn = tk.Button(payment_pa, text="𝗣𝗮𝘆 𝗢𝗻𝗹𝗶𝗻𝗲", font=(15), fg="black", bg="#d4a373",width=20, height=2,command=lambda:payment_op_page(payment_pa))
    Online_pay_btn.place(x=400, y=550)
    tk.Label(payment_pa, text="𝗔𝗿𝗿𝗶𝘃𝗲 𝗣𝗮𝘆 𝘀𝗲𝗹𝗲𝗰𝘁𝗲𝗱, 𝗽𝗹𝗲𝗮𝘀𝗲 𝗴𝗼 𝘁𝗼 𝗰𝗮𝗳𝗲 𝗮𝗿𝗿𝗶𝘃𝗲 𝗽𝗮𝘆 𝗿𝗼𝘄 𝘄𝗵𝗲𝗻 𝘂 𝗮𝗿𝗿𝗶𝘃𝗲", font=("Arial", 20), bg="#faedcd").place(x=100, y=650)

    finish_btn = tk.Button(payment_pa, text="𝙁𝙞𝙣𝙞𝙨𝙝", command=lambda: finish_page(payment_pa),font=(30), bg="#d4a373")   
    finish_btn.place(x=720, y=800)
    back_btn = tk.Button(payment_pa, text="𝙓", command=lambda: view_order_page(payment_pa),font=(30), bg="#d4a373")
    back_btn.place(x=1400, y=65)


# Payment page 
def payment_page(old_window):
    old_window.withdraw()       # hide the old window that user was in
    payment_p = tk.Toplevel()      # create window
    payment_p.title("Payment Page")
    payment_p.geometry("3000x2000")
    payment_p.configure(bg="#faedcd")

    global payment_type         # global payment type for using in this function
    payment_type = "credit"     # set the payment type in credit

    tk.Label(payment_p, text="𝓟𝓪𝔂𝓶𝓮𝓷𝓽 𝓟𝓪𝓰𝓮", font=("Arial", 40), bg="#faedcd")\
        .grid(row=0, column=0, columnspan=2, pady=50, padx=200)
    
    credit = tk.Button(payment_p, text="𝘾𝙧𝙚𝙙𝙞𝙩", font=(30), fg="black", bg="#ffffff",width=40, height=4,command=lambda: payment_page(payment_p))
    credit.place(x=100, y=200)
    cash = tk.Button(payment_p, text="𝘾𝙖𝙨𝙝", font=(30), fg="black", bg="#d4a373",width=40, height=4,command=lambda: payment_CH_page(payment_p))
    cash.place(x=600, y=200)
    sc = tk.Button(payment_p, text="𝙎𝙩𝙪𝙙𝙚𝙣𝙩 𝘾𝙖𝙧d", font=(30), fg="black", bg="#d4a373",width=85, height=4,command=lambda: payment_SC_page(payment_p))
    sc.place(x=100, y=400)
    arrive_pay_btn = tk.Button(payment_p, text="𝗔𝗿𝗿𝗶𝘃𝗲 𝗣𝗮𝘆", font=(15), fg="black", bg="#d4a373",width=20, height=2,command=lambda: payment_ap_page(payment_p))
    arrive_pay_btn.place(x=100, y=550)
    Online_pay_btn = tk.Button(payment_p, text="𝗣𝗮𝘆 𝗢𝗻𝗹𝗶𝗻𝗲", font=(15), fg="black", bg="#d4a373",width=20, height=2,command=lambda: payment_op_page(payment_p))
    Online_pay_btn.place(x=400, y=550)

    finish_btn = tk.Button(payment_p, text="𝙁𝙞𝙣𝙞𝙨𝙝", command=lambda: finish_page(payment_p),font=(30), bg="#d4a373")   
    finish_btn.place(x=720, y=800)
    back_btn = tk.Button(payment_p, text="𝙓", command=lambda: view_order_page(payment_p),font=(30), bg="#d4a373")
    back_btn.place(x=1400, y=65)


# Finish page
def finish_page(old_window):
    global payment_type
    if payment_type == "student card":
        try:
            if student_entry.get() == "":       # check if student card entry is filled
                messagebox.showerror("Error", "Please enter your student card number\nclick ok to try again")
                return
        except:
            pass
    if payment_type == "credit":
        try:
            if credit_entry.get() == "":       # check if credit card entry is filled
                messagebox.showerror("Error", "Please enter your credit card number\nclick ok to try again")
                return
        except:
            pass
    if payment_type == "cash":
        pass

    # if the entry is filled or not exist, then go to finish page
    old_window.withdraw()
    fin_p = tk.Toplevel()
    fin_p.title("Finish Page")
    fin_p.geometry("3000x2000")
    fin_p.configure(bg="#faedcd")
    label = tk.Label(fin_p, text="𝙏𝙝𝙖𝙣𝙠 𝙮𝙤𝙪 𝙛𝙤𝙧 𝙤𝙧𝙙𝙚𝙧, 𝙨𝙚𝙚 𝙮𝙤𝙪 𝙨𝙤𝙤𝙣!", font=("Arial", 50),bg="#faedcd")
    label.place(x=300, y=300)
    
    finish_btn = tk.Button(fin_p, text="𝙁𝙞𝙣𝙞𝙨𝙝", command=fin_p.destroy,font=(30), bg="#d4a373")       # destroy page
    finish_btn.place(x=650, y=800)
    backtomain_btn = tk.Button(fin_p, text="𝘽𝙖𝙘𝙠 𝙏𝙤 𝙈𝙖𝙞𝙣", command=lambda: main_page(fin_p),font=(30), bg="#d4a373")
    backtomain_btn.place(x=750, y=800)


# Customize page for drink 
def customize_d_page(old_window, drink_name="item"):
    old_window.withdraw()       # hide the old window that user was in
    custd_p = tk.Toplevel()      # create window
    custd_p.title("Customize Page")
    custd_p.geometry("3000x2000")
    custd_p.configure(bg="#faedcd")

    global total_price      # global for total price, so it can be used in other function
    total_price = 0   # reset price for new item

    if drink_name == "𝙃𝙤𝙩 𝘾𝙝𝙤𝙘𝙤𝙡𝙖𝙩𝙚":
        total_price = 2.50
    elif drink_name == "𝘾𝙤𝙛𝙛𝙚𝙚":
        total_price = 2.50
    elif drink_name == "𝙈𝙖𝙘𝙝𝙖":
        total_price = 2.00
    elif drink_name == "𝙏𝙚𝙖":
        total_price = 1.50

    tk.Label(custd_p, text="𝓒𝓾𝓼𝓽𝓸𝓶𝓲𝔃𝓮 𝓟𝓪𝓰𝓮", font=("Arial", 40), bg="#faedcd")\
        .grid(row=0, column=0, columnspan=2, pady=50, padx=200)
    # reset the customisation for each item
    global c_custom     # global for customisation, so it can be used in other function
    c_custom = {"item": drink_name}
    
    cold = tk.Button(custd_p, text="❄️ 𝘾𝙤𝙡𝙙", font=(30), fg="black", bg="#d4a373",command=lambda: customize_d_cold_page(custd_p,drink_name),width=40, height=4)
    cold.place(x=100, y=200)
    hot = tk.Button(custd_p, text="🔥 𝙃𝙤𝙩", font=(30), fg="black", bg="#d4a373",command=lambda: customize_d_hot_page(custd_p,drink_name),width=40, height=4)
    hot.place(x=600, y=200)
    back_btn = tk.Button(custd_p, text="𝙓", command=lambda: menu_page(custd_p),font=(20), bg="#d4a373")
    back_btn.place(x=1400, y=65)
    

# Customize page for drink (hot)
def customize_d_hot_page(old_window, drink_name="item"):
    old_window.withdraw()       # hide the old window that user was in
    custd_p_h = tk.Toplevel()      # create window
    custd_p_h.title("Customize Page")
    custd_p_h.geometry("3000x2000")
    custd_p_h.configure(bg="#faedcd")

    global total_price      # global for total price, so it can be used in other function
    total_price = 0   # reset price for new item

    if drink_name == "𝙃𝙤𝙩 𝘾𝙝𝙤𝙘𝙤𝙡𝙖𝙩𝙚":
        total_price = 2.50
    elif drink_name == "𝘾𝙤𝙛𝙛𝙚𝙚":
        total_price = 2.50
    elif drink_name == "𝙈𝙖𝙘𝙝𝙖":
        total_price = 2.00
    elif drink_name == "𝙏𝙚𝙖":
        total_price = 1.50

    tk.Label(custd_p_h, text="𝓒𝓾𝓼𝓽𝓸𝓶𝓲𝔃𝓮 𝓟𝓪𝓰𝓮", font=("Arial", 40), bg="#faedcd")\
        .grid(row=0, column=0, columnspan=2, pady=50, padx=200)
    
    # reset the customisation for each item
    global c_custom     # global for customisation, so it can be used in other function
    c_custom = {"item": drink_name}

    cold = tk.Button(custd_p_h, text="❄️ 𝘾𝙤𝙡𝙙", font=(30), fg="black", bg="#d4a373",command=lambda: (customize_d_cold_page(custd_p_h, drink_name)),width=40, height=4)
    cold.place(x=100, y=200)
    hot = tk.Button(custd_p_h, text="🔥 𝙃𝙤𝙩", font=(30), fg="black", bg="#ffffff",command=lambda: (customize_d_hot_page(custd_p_h, drink_name)),width=40, height=4)
    hot.place(x=600, y=200)

    def n_hot_select():            # color changed
        n_hot.config(bg="#ffffff")
        normal_hot.config(bg="#d4a373")
        extra_hot.config(bg="#d4a373")
    def nor_hot_select():              # color changed
        n_hot.config(bg="#d4a373")
        normal_hot.config(bg="#ffffff")
        extra_hot.config(bg="#d4a373")
    def ext_hot_select():              # color changed
        n_hot.config(bg="#d4a373")
        normal_hot.config(bg="#d4a373")
        extra_hot.config(bg="#ffffff")

    n_hot = tk.Button(custd_p_h, text="𝙉𝙤 𝙃𝙊𝙏", font=(30), fg="black", bg="#d4a373",command=lambda: (c_custom.update({"Hot": "No"}), n_hot_select()),width=30, height=4)
    n_hot.place(x=100, y=425)
    normal_hot = tk.Button(custd_p_h, text="𝙉𝙤𝙧𝙢𝙖𝙡 𝙃𝙊𝙏", font=(30), fg="black", bg="#d4a373",command=lambda: (c_custom.update({"Hot": "Normal"}), nor_hot_select()),width=30, height=4)
    normal_hot.place(x=500, y=425)
    extra_hot = tk.Button(custd_p_h, text="𝙀𝙭𝙩𝙧𝙖 𝙃𝙊𝙏", font=(30), fg="black", bg="#d4a373",command=lambda: (c_custom.update({"Hot": "Extra"}), ext_hot_select()),width=30, height=4)
    extra_hot.place(x=900, y=425)

    def ext_shot_select():              # color changed
        global total_price
        total_price += 1.00
        ext_btn.config(bg="#ffffff")
    
    ext_btn = tk.Button(custd_p_h, text="➕ 𝙀𝙭𝙩𝙧𝙖 𝙨𝙝𝙤𝙩 (+$1.00)", command=lambda: (c_custom.update({"Extra Shot": "Yes"}), ext_shot_select()),font=(15), bg="#d4a373")
    ext_btn.place(x=660, y=700)

    def resetd_select():              # color changed
        # Reset all customizations to their default values
        c_custom.update({
            "cold": "No",
            "Hot": "No",
            "Ice": "No",
            "Extra Shot": "No",
        })
        cold.config(bg="#d4a373")
        hot.config(bg="#d4a373")
        n_hot.config(bg="#d4a373")
        normal_hot.config(bg="#d4a373")
        extra_hot.config(bg="#d4a373")
        ext_btn.config(bg="#d4a373")

    reset_btn = tk.Button(custd_p_h, text="🗑️𝙍𝙚𝙨𝙚𝙩", command=lambda: resetd_select(),font=(15), bg="#d4a373")
    reset_btn.place(x=960, y=700)
    back_btn = tk.Button(custd_p_h, text="𝙓", command=lambda: menu_page(custd_p_h),font=(20), bg="#d4a373")
    back_btn.place(x=1400, y=65)
    
    # save item system
    def save_item():
        global total_price      
        qty = qty_entry.get()
        add_btn.config(state="disabled")            # Make the button state to disable, for fixing double clicking

        if qty.isdigit():       # check is the input number or not
            qty = int(qty)

            if qty < 1:
                messagebox.showerror("Error", "Quantity must be more than 0\nclick ok to try again")
                add_btn.config(state="normal")       # make button state back to normal for qty error
                return
            elif qty > 100:
                messagebox.showerror("Error", "Quantity must be less than 100\nclick ok to try again")
                add_btn.config(state="normal")       # make button state back to normal for qty 
                return
            c_custom["Quantity"] = qty
            total_price = total_price * qty   # calculate the price
        else:
            messagebox.showerror("Error", "Please enter a number\nclick ok to try again")
            add_btn.config(state="normal")       # make button state back to normal for next item
            return
        
        # make order number in 1 more than the last order number, for each order
        global receipt_num     # global for receipt number, so it can be used in other function
        order_num = receipt_num
        receipt_num += 1
        c_custom["Order Number"] = order_num        # add order number
        c_custom["Price"] = total_price
        orders.append(c_custom.copy())      # add custom to order list

        messagebox.showinfo("Saved", f"Item added! Order #{order_num}\nclick ok to back menu")
        add_btn.config(state="normal")       # make button state back to normal for next item
        menu_page(custd_p_h)

    qty = tk.Label(custd_p_h, text="𝙌𝙪𝙖𝙣𝙩𝙞𝙩𝙮 : ", font=(30), bg="#faedcd")
    qty.place(x=100, y=700)
    qty_entry = tk.Entry(custd_p_h, font=(30), bg="#d4a373")
    qty_entry.place(x=220, y=700)
    add_btn = tk.Button(custd_p_h, text="𝘼𝙙𝙙 𝙄𝙩𝙚𝙢", command=save_item,font=(30), bg="#d4a373")
    add_btn.place(x=700, y=800)


# Customize page for drink (cold)
def customize_d_cold_page(old_window, drink_name="item"):
    old_window.withdraw()       # hide the old window that user was in
    custd_p_c = tk.Toplevel()      # create window
    custd_p_c.title("Customize Page")
    custd_p_c.geometry("3000x2000")
    custd_p_c.configure(bg="#faedcd")

    global total_price      # global for total price, so it can be used in other function
    total_price = 0   # reset price for new item

    if drink_name == "𝙃𝙤𝙩 𝘾𝙝𝙤𝙘𝙤𝙡𝙖𝙩𝙚":
        total_price = 2.50
    elif drink_name == "𝘾𝙤𝙛𝙛𝙚𝙚":
        total_price = 2.50
    elif drink_name == "𝙈𝙖𝙘𝙝𝙖":
        total_price = 2.00
    elif drink_name == "𝙏𝙚𝙖":
        total_price = 1.50

    tk.Label(custd_p_c, text="𝓒𝓾𝓼𝓽𝓸𝓶𝓲𝔃𝓮 𝓟𝓪𝓰𝓮", font=("Arial", 40), bg="#faedcd")\
        .grid(row=0, column=0, columnspan=2, pady=50, padx=200)
    
    # reset the customisation for each item
    global c_custom     # global for customisation, so it can be used in other function
    c_custom = {"item": drink_name}
    
    cold = tk.Button(custd_p_c, text="❄️ 𝘾𝙤𝙡𝙙", font=(30), fg="black", bg="#ffffff",command=lambda: customize_d_cold_page(custd_p_c, drink_name),width=40, height=4)
    cold.place(x=100, y=200)
    hot = tk.Button(custd_p_c, text="🔥 𝙃𝙤𝙩", font=(30), fg="black", bg="#d4a373",command=lambda: customize_d_hot_page(custd_p_c, drink_name),width=40, height=4)
    hot.place(x=600, y=200)

    def n_ice_select():            # color changed
        n_ice.config(bg="#ffffff")
        normal_ice.config(bg="#d4a373")
        extra_ice.config(bg="#d4a373")
    def nor_ice_select():              # color changed
        n_ice.config(bg="#d4a373")
        normal_ice.config(bg="#ffffff")
        extra_ice.config(bg="#d4a373")
    def ext_ice_select():              # color changed
        n_ice.config(bg="#d4a373")
        normal_ice.config(bg="#d4a373")
        extra_ice.config(bg="#ffffff")

    n_ice = tk.Button(custd_p_c, text="𝙉𝙤 𝙄𝘾𝙀", font=(30), fg="black", bg="#d4a373",command=lambda: (c_custom.update({"Ice": "No"}), n_ice_select()),width=30, height=4)
    n_ice.place(x=100, y=425)
    normal_ice = tk.Button(custd_p_c, text="𝙉𝙤𝙧𝙢𝙖𝙡 𝙄𝘾𝙀", font=(30), fg="black", bg="#d4a373",command=lambda: (c_custom.update({"Ice": "Normal"}), nor_ice_select()),width=30, height=4)
    normal_ice.place(x=500, y=425)
    extra_ice = tk.Button(custd_p_c, text="𝙀𝙭𝙩𝙧𝙖 𝙄𝘾𝙀", font=(30), fg="black", bg="#d4a373",command=lambda: (c_custom.update({"Ice": "Extra"}), ext_ice_select()),width=30, height=4)
    extra_ice.place(x=900, y=425)

    def ext_shot_select():              # color changed
        global total_price
        total_price += 1.00
        ext_btn.config(bg="#ffffff")
    
    ext_btn = tk.Button(custd_p_c, text="➕ 𝙀𝙭𝙩𝙧𝙖 𝙨𝙝𝙤𝙩 (+$1.00)", command=lambda: (c_custom.update({"Extra Shot": "Yes"}), ext_shot_select()),font=(15), bg="#d4a373")
    ext_btn.place(x=660, y=700)

    def resetd_select():              # color changed
        # Reset all customizations to their default values
        c_custom.update({
            "cold": "No",
            "Hot": "No",
            "Ice": "No",
            "Extra Shot": "No",
        })
        cold.config(bg="#d4a373")
        hot.config(bg="#d4a373")
        n_ice.config(bg="#d4a373")
        normal_ice.config(bg="#d4a373")
        extra_ice.config(bg="#d4a373")
        ext_btn.config(bg="#d4a373")

    reset_btn = tk.Button(custd_p_c, text="🗑️𝙍𝙚𝙨𝙚𝙩", command=lambda: resetd_select(),font=(15), bg="#d4a373")
    reset_btn.place(x=960, y=700)
    back_btn = tk.Button(custd_p_c, text="𝙓", command=lambda: menu_page(custd_p_c),font=(20), bg="#d4a373")
    back_btn.place(x=1400, y=65)
    
    # save item system
    def save_item():
        global total_price      
        qty = qty_entry.get()
        add_btn.config(state="disabled")            # Make the button state to disable, for fixing double clicking

        if qty.isdigit():       # check is the input number or not
            qty = int(qty)

            if qty < 1:
                messagebox.showerror("Error", "Quantity must be more than 0\nclick ok to try again")
                add_btn.config(state="normal")       # make button state back to normal for qty error
                return
            elif qty > 100:
                messagebox.showerror("Error", "Quantity must be less than 100\nclick ok to try again")
                add_btn.config(state="normal")       # make button state back to normal for qty 
                return
            c_custom["Quantity"] = qty
            total_price = total_price * qty   # calculate the price
        else:
            messagebox.showerror("Error", "Please enter a number\nclick ok to try again")
            add_btn.config(state="normal")       # make button state back to normal for next item
            return
        
        # make order number in 1 more than the last order number, for each order
        global receipt_num     # global for receipt number, so it can be used in other function
        order_num = receipt_num
        receipt_num += 1
        c_custom["Order Number"] = order_num        # add order number
        c_custom["Price"] = total_price
        orders.append(c_custom.copy())      # add custom to order list

        messagebox.showinfo("Saved", f"Item added! Order #{order_num}\nclick ok to back menu")
        add_btn.config(state="normal")       # make button state back to normal for next item
        menu_page(custd_p_c)

    qty = tk.Label(custd_p_c, text="𝙌𝙪𝙖𝙣𝙩𝙞𝙩𝙮 : ", font=(30), bg="#faedcd")
    qty.place(x=100, y=700)
    qty_entry = tk.Entry(custd_p_c, font=(30), bg="#d4a373")
    qty_entry.place(x=220, y=700)
    add_btn = tk.Button(custd_p_c, text="𝘼𝙙𝙙 𝙄𝙩𝙚𝙢", command=save_item,font=(30), bg="#d4a373")
    add_btn.place(x=700, y=800)


# Customize page for food
def customize_f_page(old_window, food_name="item"):
    old_window.withdraw()       # hide the old window that user was in
    custF_p = tk.Toplevel()      # create window    
    custF_p.title("Customize Page")
    custF_p.geometry("3000x2000")
    custF_p.configure(bg="#faedcd")

    global total_price      # global for total price, so it can be used in other function
    total_price = 0   # reset price for new item

    # set price for each item
    if food_name == "𝘽𝙪𝙧𝙜𝙚𝙧":
        total_price = 3.00
    elif food_name == "𝙎𝙖𝙣𝙙𝙬𝙞𝙘𝙝":
        total_price = 2.50
    elif food_name == "𝙘𝙝𝙤𝙘𝙤𝙡𝙖𝙩𝙚 𝙘𝙖𝙠𝙚":
        total_price = 2.00
    elif food_name == "𝙈𝙪𝙛𝙛𝙞𝙣":
        total_price = 1.50

    tk.Label(custF_p, text="𝓒𝓾𝓼𝓽𝓸𝓶𝓲𝔃𝓮 𝓟𝓪𝓰𝓮", font=("Arial", 40), bg="#faedcd")\
        .grid(row=0, column=0, columnspan=2, pady=50, padx=200)
    
    #reset the customisation for each item
    global c_custom     # global for customisation, so it can be used in other function
    c_custom = {"item": food_name}

    def toasted_select():            # color changed
        toasted.config(bg="#ffffff")
        Ntoasted.config(bg="#d4a373")
    def Ntoasted_select():              # color changed
        toasted.config(bg="#d4a373")
        Ntoasted.config(bg="#ffffff")
    
    toasted = tk.Button(custF_p, text="♨️ 𝙏𝙤𝙖𝙨𝙩𝙚𝙙", font=(30), fg="black", bg="#d4a373",command=lambda: (c_custom.update({"Toasted": "Yes"}),toasted_select()),width=40, height=4)
    toasted.place(x=100, y=200)
    Ntoasted = tk.Button(custF_p, text="𝙉𝙤 𝙏𝙤𝙖𝙨𝙩𝙚𝙙", font=(30), fg="black", bg="#d4a373",command=lambda: (c_custom.update({"Toasted": "No"}),Ntoasted_select()),width=40, height=4)
    Ntoasted.place(x=600, y=200)

    def cheese_select():            # color changed
        cheese.config(bg="#ffffff")
        Ncheese.config(bg="#d4a373")
    def Ncheese_select():              # color changed
        cheese.config(bg="#d4a373")
        Ncheese.config(bg="#ffffff")

    cheese = tk.Button(custF_p, text="🧀 𝘾𝙝𝙚𝙚𝙨𝙚", font=(30), fg="black", bg="#d4a373",command=lambda: (c_custom.update({"Cheese": "Yes"}),cheese_select()),width=40, height=4)
    cheese.place(x=100, y=370)
    Ncheese = tk.Button(custF_p, text="𝙉𝙤 𝘾𝙝𝙚𝙚𝙨𝙚", font=(30), fg="black", bg="#d4a373",command=lambda: (c_custom.update({"Cheese": "No"}),Ncheese_select()),width=40, height=4)
    Ncheese.place(x=600, y=370)

    def Nsauce_select():            # color changed
        Nsauce.config(bg="#ffffff")
        sauce_b.config(bg="#d4a373")
        sauce_t.config(bg="#d4a373")
        sauce_w.config(bg="#d4a373")
        sauce_m.config(bg="#d4a373")
    def sauceb_select():              # color changed
        Nsauce.config(bg="#d4a373")
        sauce_b.config(bg="#ffffff")
        sauce_t.config(bg="#d4a373")
        sauce_w.config(bg="#d4a373")
        sauce_m.config(bg="#d4a373")
    def sauce_t_select():            # color changed
        sauce_t.config(bg="#ffffff")
        Nsauce.config(bg="#d4a373")
        sauce_b.config(bg="#d4a373")
        sauce_w.config(bg="#d4a373")
        sauce_m.config(bg="#d4a373")
    def saucew_select():              # color changed
        Nsauce.config(bg="#d4a373")
        sauce_b.config(bg="#d4a373")
        sauce_t.config(bg="#d4a373")
        sauce_w.config(bg="#ffffff")
        sauce_m.config(bg="#d4a373")
    def saucem_select():              # color changed
        Nsauce.config(bg="#d4a373")
        sauce_b.config(bg="#d4a373")
        sauce_t.config(bg="#d4a373")
        sauce_w.config(bg="#d4a373")
        sauce_m.config(bg="#ffffff")

    Nsauce = tk.Button(custF_p, text="𝙉𝙤 𝙎𝙖𝙪𝙘𝙚", font=(25), fg="black", bg="#d4a373",command=lambda: (c_custom.update({"Sauce": "No"}),Nsauce_select()),width=20, height=4)
    Nsauce.place(x=100, y=550)
    sauce_b= tk.Button(custF_p, text="🍖 𝘽𝘽𝙌 𝙎𝙖𝙪𝙘𝙚", font=(25), fg="black", bg="#d4a373",command=lambda: (c_custom.update({"Sauce": "BBQ"}),sauceb_select()),width=20, height=4)
    sauce_b.place(x=350, y=550)
    sauce_t= tk.Button(custF_p, text="🥫 𝙏𝙤𝙢𝙖𝙩𝙤 𝙎𝙖𝙪𝙘𝙚", font=(25), fg="black", bg="#d4a373",command=lambda: (c_custom.update({"Sauce": "Tomato"}),sauce_t_select()),width=20, height=4)
    sauce_t.place(x=600, y=550)
    sauce_w= tk.Button(custF_p, text="🌶️ 𝘽𝙡𝙖𝙘𝙠 𝙥𝙚𝙥𝙥𝙚𝙧 \n𝙎𝙖𝙪𝙘𝙚", font=(25), fg="black", bg="#d4a373",command=lambda: (c_custom.update({"Sauce": "White"}),saucew_select()),width=20, height=4)
    sauce_w.place(x=850, y=550)
    sauce_m= tk.Button(custF_p, text="🧴 𝙈𝙖y𝙤 𝙎𝙖𝙪𝙘𝙚", font=(25), fg="black", bg="#d4a373",command=lambda: (c_custom.update({"Sauce": "Mayo"}),saucem_select()),width=20, height=4)
    sauce_m.place(x=1100, y=550)

    def resetf_select():
        # Reset all customizations to their default values
        c_custom.update({
            "Toasted": "No",
            "Cheese": "No",
            "Sauce": "No",
        })
        toasted.config(bg="#d4a373")
        Ntoasted.config(bg="#d4a373")
        cheese.config(bg="#d4a373")
        Ncheese.config(bg="#d4a373")
        Nsauce.config(bg="#d4a373")
        sauce_b.config(bg="#d4a373")
        sauce_t.config(bg="#d4a373")
        sauce_w.config(bg="#d4a373")
        sauce_m.config(bg="#d4a373")
    reset_btn = tk.Button(custF_p, text="🗑️𝙍𝙚𝙨𝙚𝙩", command=lambda: resetf_select(),font=(15), bg="#d4a373")
    reset_btn.place(x=700, y=700)
    back_btn = tk.Button(custF_p, text="𝙓", command=lambda: menu_page(custF_p),font=(20), bg="#d4a373")
    back_btn.place(x=1400, y=65)
    
    # save item system
    def save_item():
        global total_price      
        qty = qty_entry.get()
        add_btn.config(state="disabled")            # Make the button state to disable, for fixing double clicking

        if qty.isdigit():       # check is the input number or not
            qty = int(qty)
            if qty < 1:
                messagebox.showerror("Error", "Quantity must be more than 0\nclick ok to try again")
                add_btn.config(state="normal")       # make button state back to normal for next item
                return
            elif qty > 100:
                messagebox.showerror("Error", "Quantity must be less than 100\nclick ok to try again")
                add_btn.config(state="normal")       # make button state back to normal for next item
                return
            c_custom["Quantity"] = qty
            total_price = total_price * qty   # calculate the price
        else:
            messagebox.showerror("Error", "Please enter a number\nclick ok to try again")
            add_btn.config(state="normal")       # make button state back to normal for next item
            return
        
        # make order number in 1 more than the last order number, for each order
        global receipt_num     # global for receipt number, so it can be used in other function
        order_num = receipt_num
        receipt_num += 1
        c_custom["Order Number"] = order_num        # add order number
        c_custom["Price"] = total_price
        orders.append(c_custom.copy())      # add custom to order list
        messagebox.showinfo("Saved", f"Item added! Order #{order_num}\nclick ok to back menu")
        add_btn.config(state="normal")       # make button state back to normal for next item
        receipt_num += 1
        menu_page(custF_p)

    qty = tk.Label(custF_p, text="𝙌𝙪𝙖𝙣𝙩𝙞𝙩𝙮 : ", font=(30), bg="#faedcd")
    qty.place(x=100, y=700)
    qty_entry = tk.Entry(custF_p, font=(30), bg="#d4a373")
    qty_entry.place(x=220, y=700)
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

    def quick_add(name,price):
        global receipt_num      # global the receipt number, so it can be used in other function
        order ={}
        order["item"] = name
        order["Price"] = price
        order["Quantity"] = 1
        order["Order Number"] = receipt_num
        orders.append(order)        # add order to order list
        messagebox.showinfo("Quick Added", f"{name} added to order! Order #{receipt_num}\nclick ok for next")
        receipt_num += 1        # add 1 for next order

    # item 1
    canvas.create_rectangle(50, 50, 450, 270, fill="#faedcd", outline="black")
    item = tk.Label(menu2_p, text="🍔 𝘽𝙪𝙧𝙜𝙚𝙧\n$3.00", font=("Arial", 20),bg="#faedcd")
    btn = tk.Button(menu2_p, text="𝘾𝙪𝙨𝙩𝙤𝙢𝙞𝙯𝙚", bg="#d4aa73", font=("Arial", 20), command=lambda: customize_f_page(menu2_p,"𝘽𝙪𝙧𝙜𝙚𝙧"))
    quick_btn = tk.Button(menu2_p, text="➕", bg="#d4a373",font =(20), command=lambda: quick_add("𝘽𝙪𝙧�𝙚𝙧", 3.00))
    canvas.create_window(250, 120, window=item) 
    canvas.create_window(250, 200, window=btn)
    canvas.create_window(360, 200, window=quick_btn)

    # item 2
    canvas.create_rectangle(500, 50, 900, 270, fill="#faedcd", outline="black")
    item2 = tk.Label(menu2_p, text="🥪 𝙎𝙖𝙣𝙙𝙬𝙞𝙘𝙝\n$2.50", font=("Arial", 20), bg="#faedcd")
    btn2 = tk.Button(menu2_p, text="𝘾𝙪𝙨𝙩𝙤𝙢𝙞𝙯𝙚", bg="#d4aa73", font=("Arial", 20), command=lambda: customize_f_page(menu2_p,"𝙎𝙖𝙣𝙙𝙬𝙞𝙘𝙝"))
    quick_btn2 = tk.Button(menu2_p, text="➕", bg="#d4a373",font =(20), command=lambda: quick_add("𝙎𝙖𝙣𝙙𝙬𝙞𝙘𝙝", 2.50))
    canvas.create_window(700, 120, window=item2)
    canvas.create_window(700, 200, window=btn2)
    canvas.create_window(810, 200, window=quick_btn2)

    # item 3
    canvas.create_rectangle(50, 300, 450, 530, fill="#faedcd", outline="black")
    item3 = tk.Label(menu2_p, text="🍰 𝙘𝙝𝙤𝙘𝙤𝙡𝙖𝙩𝙚 𝙘𝙖𝙠𝙚\n$2.00", font=("Arial", 20),bg="#faedcd")
    btn3 = tk.Button(menu2_p, text="𝘾𝙪𝙨𝙩𝙤𝙢𝙞𝙯𝙚", bg="#d4aa73", font=("Arial", 20), command=lambda: customize_f_page(menu2_p,"𝙘𝙝𝙤𝙘𝙤𝙡𝙖𝙩𝙚 𝙘𝙖𝙠𝙚"))
    quick_btn3 = tk.Button(menu2_p, text="➕", bg="#d4a373",font =(20), command=lambda: quick_add("𝙘𝙝𝙤𝙘𝙤𝙡𝙖𝙩𝙚 𝙘𝙖𝙠𝙚", 2.00))
    canvas.create_window(250, 370, window=item3) 
    canvas.create_window(250, 450, window=btn3)
    canvas.create_window(360, 450, window=quick_btn3)

    # item 4
    canvas.create_rectangle(500, 300, 900, 530, fill="#faedcd", outline="black")
    item4 = tk.Label(menu2_p, text="🧁 𝙈𝙪𝙛𝙛𝙞𝙣\n$1.50", font=("Arial", 20), bg="#faedcd")
    btn4 = tk.Button(menu2_p, text="𝘾𝙪𝙨𝙩𝙤𝙢𝙞𝙯𝙚", bg="#d4aa73", font=("Arial", 20), command=lambda: customize_f_page(menu2_p,"𝙈𝙪𝙛𝙛𝙞𝙣"))
    quick_btn4 = tk.Button(menu2_p, text="➕", bg="#d4a373",font =(20), command=lambda: quick_add("𝙈𝙪𝙛𝙛𝙞𝙣", 1.50))
    canvas.create_window(700, 370, window=item4)
    canvas.create_window(700, 450, window=btn4)
    canvas.create_window(810, 450, window=quick_btn4)

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

    def quick_add(name,price):
        global receipt_num      # global the receipt number, so it can be used in other function
        order ={}
        order["item"] = name
        order["Price"] = price
        order["Quantity"] = 1
        order["Order Number"] = receipt_num
        orders.append(order)        # add order to order list
        messagebox.showinfo("Quick Added", f"{name} added to order! Order #{receipt_num}\nclick ok to next")
        receipt_num += 1        # add 1 for next order

    # item 1
    canvas.create_rectangle(50, 50, 450, 270, fill="#faedcd", outline="black")
    item = tk.Label(menu_p, text="☕ 𝙃𝙤𝙩 𝘾𝙝𝙤𝙘𝙤𝙡𝙖𝙩𝙚\n$2.50", font=("Arial", 20),bg="#faedcd")
    btn = tk.Button(menu_p, text="𝘾𝙪𝙨𝙩𝙤𝙢𝙞𝙯𝙚", bg="#d4aa73", font=("Arial", 20), command=lambda: customize_d_page(menu_p, "𝙃𝙤𝙩 𝘾𝙝𝙤𝙘𝙤𝙡𝙖𝙩𝙚"))
    quick_btn = tk.Button(menu_p, text="➕", bg="#d4a373",font =(20), command=lambda: quick_add("𝙃𝙤𝙩 𝘾𝙝𝙤𝙘𝙤𝙡𝙖𝙩𝙚", 2.50))
    canvas.create_window(250, 120, window=item) 
    canvas.create_window(250, 200, window=btn)
    canvas.create_window(360, 200, window=quick_btn)

    # item 2
    canvas.create_rectangle(500, 50, 900, 270, fill="#faedcd", outline="black")
    item2 = tk.Label(menu_p, text="☕︎ 𝘾𝙤𝙛𝙛𝙚𝙚\n$2.50", font=("Arial", 20), bg="#faedcd")
    btn2 = tk.Button(menu_p, text="𝘾𝙪𝙨𝙩𝙤𝙢𝙞𝙯𝙚", bg="#d4aa73", font=("Arial", 20), command=lambda: customize_d_page(menu_p, "𝘾𝙤𝙛𝙛𝙚𝙚"))
    quick_btn2 = tk.Button(menu_p, text="➕", bg="#d4a373",font =(20), command=lambda: quick_add("𝘾𝙤𝙛𝙛𝙚𝙚", 2.50))
    canvas.create_window(700, 120, window=item2)
    canvas.create_window(700, 200, window=btn2)
    canvas.create_window(810, 200, window=quick_btn2)

    # item 3
    canvas.create_rectangle(50, 300, 450, 530, fill="#faedcd", outline="black")
    item3 = tk.Label(menu_p, text="🥤 𝙈𝙖𝙘𝙝𝙖\n$2.00", font=("Arial", 20),bg="#faedcd")
    btn3 = tk.Button(menu_p, text="𝘾𝙪𝙨𝙩𝙤𝙢𝙞𝙯𝙚", bg="#d4aa73", font=("Arial", 20), command=lambda: customize_d_page(menu_p, "𝙈𝙖𝙘𝙝𝙖"))
    quick_btn3 = tk.Button(menu_p, text="➕", bg="#d4a373",font =(20), command=lambda: quick_add("𝙈𝙖𝙘𝙝𝙖", 2.00))
    canvas.create_window(250, 370, window=item3) 
    canvas.create_window(250, 450, window=btn3)
    canvas.create_window(360, 450, window=quick_btn3)

    # item 4
    canvas.create_rectangle(500, 300, 900, 530, fill="#faedcd", outline="black")
    item4 = tk.Label(menu_p, text="🍵 𝙏𝙚𝙖\n$1.50", font=("Arial", 20), bg="#faedcd")
    btn4 = tk.Button(menu_p, text="𝘾𝙪𝙨𝙩𝙤𝙢𝙞𝙯𝙚", bg="#d4aa73", font=("Arial", 20), command=lambda: customize_d_page(menu_p, "𝙏𝙚𝙖"))
    quick_btn4 = tk.Button(menu_p, text="➕", bg="#d4a373",font =(20), command=lambda: quick_add("𝙏𝙚𝙖", 1.50))
    canvas.create_window(700, 370, window=item4)
    canvas.create_window(700, 450, window=btn4)
    canvas.create_window(810, 450, window=quick_btn4)

    # Back, Next, and View Order buttons
    back_btn = tk.Button(menu_p, text="𝘽𝙖𝙘𝙠 𝙩𝙤 \n𝙡𝙤𝙜𝙞𝙣 𝙥𝙖𝙜𝙚", command=lambda: login_page(menu_p),font=(40), bg="#d4a373")
    back_btn.place(x=90, y=400)
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
    label = tk.Label(main_p, text="𝓦𝓮𝓵𝓬𝓸𝓶𝓮 𝓽𝓸 𝓽𝓱𝓮 𝓒𝓪𝓯𝓮!", font=("Arial", 80),bg="#faedcd")
    label.pack(pady=20)
    
    # Buttons to enter other pages 
    signup_p_enter2 = tk.Button(main_p, text="𝓢𝓲𝓰𝓷𝓾𝓹 𝓹𝓪𝓰𝓮", command=lambda: signup_page(main_p),width=70, height=2, font=(30), fg="white", bg="#d4a373")
    signup_p_enter2.pack(pady=120)
    login_p_enter2 = tk.Button(main_p, text="𝓛𝓸𝓰𝓲𝓷 𝓹𝓪𝓰𝓮", command=lambda: login_page(main_p),width=70, height=2, font=(30), fg="white", bg="#d4a373")
    login_p_enter2.pack(pady=120)


# Start the loop
if __name__ == "__main__":
    root.mainloop()
