#created by JEFF LEE

#This the program for school cafe system

#They can creat acc, login, order food and drink,customise their order, view their order, and save invoice
#(it will save thier time to line up and order unline.)

#Credits: 
#https://lingojam.com/FancyTextGenerator (for the special text)
#



#importing the necessary libraries
import math
import tkinter as tk
from tkinter import messagebox

accounts = {}


root = tk.Tk()
root.title("Cafe Menu")
root.geometry("3000x2000")
root.configure(bg="#faedcd")

# Add a Title
label = tk.Label(root, text="𝓦𝓮𝓵𝓸𝓬𝓶 𝓽𝓸 𝓽𝓱𝓮 𝓒𝓪𝓯𝓮!", font=("Arial", 80),bg="#faedcd")
label.pack(pady=20)


# login page function
def login_page(old_window):
    old_window.withdraw()
    login_p = tk.Toplevel()
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

    def login():
        user = username_entry.get()
        pwd = password_entry.get()

        # Check against saved accounts
        if user in accounts and accounts[user] == pwd:
            messagebox.showinfo("Login Success", f"Welcome, {user}!")
            login_p.destroy()
            menu_page()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    
    login_btn = tk.Button(login_p, text="𝓛𝓸𝓰𝓲𝓷", command=login,font=(30), bg="#d4a373",)
    login_btn.grid(row=3, column=1, pady=10)
    back_btn = tk.Button(login_p, text="𝘽𝙖𝙘𝙠", command=lambda: main_page(login_p),font=(30), bg="#d4a373")
    back_btn.grid(row=4, column=1, pady=10)

login_p_enter = tk.Button(root, text="𝓛𝓸𝓰𝓲𝓷 𝓹𝓪𝓰𝓮", command=lambda: login_page(root),width=70, height=2, font=(30), fg="white", bg="#d4a373")
login_p_enter.pack(pady=50)


# Sign up page function
def signup_page(old_window):
    old_window.withdraw()
    signup_p = tk.Toplevel()
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

    def signup():
        user = username_entry.get()
        pwd = password_entry.get()

        # Check if username already exists
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
signup_p_enter.pack(pady=50)


# View my order page function
def view_order_page(old_window):
    old_window.withdraw()
    order_window = tk.Toplevel()
    order_window.title("View My Order")
    order_window.geometry("3000x2000")
    order_window.configure(bg="#faedcd")

    menu_label = tk.Label(order_window, text="𝓥𝓲𝓮𝔀 𝓨𝓸𝓾𝓻 𝓞𝓻𝓭𝓮r", font=("Arial", 40), bg="#faedcd")
    menu_label.pack(pady=10)

    # Add order items here
    menu_label = tk.Label(order_window, text="Order Items", font=("Arial", 12), bg="#faedcd")
    menu_label.pack(pady=5)

    back_btn = tk.Button(order_window, text="BACK", command=lambda: main_page(order_window),font=(30), bg="#d4a373")
    back_btn.pack(pady=10)

view_order_p_enter = tk.Button(root, text="𝓥𝓲𝓮𝔀 𝓨𝓸𝓾𝓻 𝓞𝓻𝓭𝓮r", command=lambda: view_order_page(root),width=70, height=2, font=(30), fg="white", bg="#d4a373")
view_order_p_enter.pack(pady=50)


def menu_page2(old_window):
    old_window.withdraw()
    menu2_p = tk.Toplevel()
    menu2_p.title("Menu Page")
    menu2_p.geometry("3000x2000")
    menu2_p.configure(bg="#faedcd")

    tk.Label(menu2_p, text="𝓜𝓮𝓷𝓾 𝓟𝓪𝓰𝓮【２】\n𝓕𝓸𝓸𝓭", font=("Arial", 40), bg="#faedcd")\
        .grid(row=0, column=0, columnspan=2, pady=20)

    canvas = tk.Canvas(menu2_p, width=960, height=600, bg="#d4aa73")
    canvas.grid(row=1, column=1, pady=20, padx=270,)

    # item 1
    canvas.create_rectangle(50, 50, 450, 270, fill="#faedcd", outline="black")

    item = tk.Label(menu2_p, text="Burger", font=("Arial", 20),bg="#faedcd")
    btn = tk.Button(menu2_p, text="Customize", bg="#d4aa73", fg="white", font=("Arial", 20))

    canvas.create_window(250, 120, window=item) 
    canvas.create_window(250, 200, window=btn)

    # item 2
    canvas.create_rectangle(500, 50, 900, 270, fill="#faedcd", outline="black")

    item2 = tk.Label(menu2_p, text="Sandwich", font=("Arial", 20), bg="#faedcd")
    btn2 = tk.Button(menu2_p, text="Customize", bg="#d4aa73", fg="white", font=("Arial", 20))

    canvas.create_window(700, 120, window=item2)
    canvas.create_window(700, 200, window=btn2)

    # item 3
    canvas.create_rectangle(50, 300, 450, 530, fill="#faedcd", outline="black")

    item3 = tk.Label(menu2_p, text="chocolate cake", font=("Arial", 20),bg="#faedcd")
    btn3 = tk.Button(menu2_p, text="Customize", bg="#d4aa73", fg="white", font=("Arial", 20))

    canvas.create_window(250, 370, window=item3) 
    canvas.create_window(250, 450, window=btn3)

    # item 4
    canvas.create_rectangle(500, 300, 900, 530, fill="#faedcd", outline="black")

    item4 = tk.Label(menu2_p, text="Muffin", font=("Arial", 20), bg="#faedcd")
    btn4 = tk.Button(menu2_p, text="Customize", bg="#d4aa73", fg="white", font=("Arial", 20))

    canvas.create_window(700, 370, window=item4)
    canvas.create_window(700, 450, window=btn4)

    next_btn = tk.Button(menu2_p, text="Next", command=lambda: view_order_page(menu2_p),font=(30), bg="#d4a373")
    next_btn.place(x=1350, y=400)


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

    item = tk.Label(menu_p, text="Hot chocolate", font=("Arial", 20),bg="#faedcd")
    btn = tk.Button(menu_p, text="Customize", bg="#d4aa73", fg="white", font=("Arial", 20))

    canvas.create_window(250, 120, window=item) 
    canvas.create_window(250, 200, window=btn)

    # item 2
    canvas.create_rectangle(500, 50, 900, 270, fill="#faedcd", outline="black")

    item2 = tk.Label(menu_p, text="Coffee", font=("Arial", 20), bg="#faedcd")
    btn2 = tk.Button(menu_p, text="Customize", bg="#d4aa73", fg="white", font=("Arial", 20))

    canvas.create_window(700, 120, window=item2)
    canvas.create_window(700, 200, window=btn2)

    # item 3
    canvas.create_rectangle(50, 300, 450, 530, fill="#faedcd", outline="black")

    item3 = tk.Label(menu_p, text="Macha", font=("Arial", 20),bg="#faedcd")
    btn3 = tk.Button(menu_p, text="Customize", bg="#d4aa73", fg="white", font=("Arial", 20))

    canvas.create_window(250, 370, window=item3) 
    canvas.create_window(250, 450, window=btn3)

    # item 4
    canvas.create_rectangle(500, 300, 900, 530, fill="#faedcd", outline="black")

    item4 = tk.Label(menu_p, text="Tea", font=("Arial", 20), bg="#faedcd")
    btn4 = tk.Button(menu_p, text="Customize", bg="#d4aa73", fg="white", font=("Arial", 20))

    canvas.create_window(700, 370, window=item4)
    canvas.create_window(700, 450, window=btn4)

    next_btn = tk.Button(menu_p, text="Next", command=lambda: menu_page2(menu_p),font=(30), bg="#d4a373")
    next_btn.place(x=1350, y=400)

    
    
def main_page(old_window):
    old_window.withdraw()
    main_p = tk.Toplevel()
    main_p.title("Cafe Menu")
    main_p.geometry("3000x2000")
    main_p.configure(bg="#faedcd")
    label = tk.Label(main_p, text="𝓦𝓮𝓵𝓸𝓬𝓶 𝓽𝓸 𝓽𝓱𝓮 𝓒𝓪𝓯𝓮!", font=("Arial", 80),bg="#faedcd")
    label.pack(pady=20)
    
    login_p_enter2 = tk.Button(main_p, text="𝓛𝓸𝓰𝓲𝓷 𝓹𝓪𝓰𝓮", command=lambda: login_page(main_p),width=70, height=2, font=(30), fg="white", bg="#d4a373")
    login_p_enter2.pack(pady=50)
    signup_p_enter2 = tk.Button(main_p, text="𝓢𝓲𝓰𝓷𝓾𝓹 𝓹𝓪𝓰𝓮", command=lambda: signup_page(main_p),width=70, height=2, font=(30), fg="white", bg="#d4a373")
    signup_p_enter2.pack(pady=50)
    view_order_p_enter2 = tk.Button(main_p, text="𝓥𝓲𝓮𝔀 𝓨𝓸𝓾𝓻 𝓞𝓻𝓭𝓮r", command=lambda: view_order_page(main_p),width=70, height=2, font=(30), fg="white", bg="#d4a373")
    view_order_p_enter2.pack(pady=50)
    menu_p_enter2 = tk.Button(main_p, text="𝓜𝓮𝓷𝓾", command=lambda: menu_page(main_p),width=70, height=2, font=(30), fg="white", bg="#d4a373")
    menu_p_enter2.pack(pady=50)

menu_p_enter = tk.Button(root, text="𝓜𝓮𝓷𝓾", command=lambda: menu_page(root),width=70, height=2, font=(30), fg="white", bg="#d4a373")
menu_p_enter.pack(pady=50)


# Start the application
if __name__ == "__main__":
    root.mainloop()
