from tkinter import *
import mysql.connector
from datetime import datetime
from PIL import Image, ImageTk

# Database connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="inventory"
)

cursor = connection.cursor()

# Exit function
def exit1():
    quit()

class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.title("Login Page")

        # Load and set the background image
        self.bg_image = Image.open(r"C:\java dsa\tkinter\WhatsApp Image 2024-10-20 at 16.52.46_f7398b43.png.png")
        self.bg_image = self.bg_image.resize((400, 300), Image.Resampling.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = Label(self.root, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Login Page UI
        Label(self.root, text="Login", font=("times new roman", 20, "bold"), bg="#ffffff").pack(pady=20)

        Label(self.root, text="Username", font=("times new roman", 15), bg="#ffffff").place(x=50, y=80)
        self.username_entry = Entry(self.root, font=("times new roman", 15))
        self.username_entry.place(x=150, y=80)

        Label(self.root, text="Password", font=("times new roman", 15), bg="#ffffff").place(x=50, y=130)
        self.password_entry = Entry(self.root, show="*", font=("times new roman", 15))
        self.password_entry.place(x=150, y=130)

        # Login Button
        Button(self.root, text="Login", font=("times new roman", 15, "bold"), bg="green", fg="white",
               command=self.login).place(x=150, y=180, width=100)

        # Button for new user registration
        Button(self.root, text="NEW USER?", font=("times new roman", 10, "bold"),
               command=self.newuser1).place(x=160, y=230, width=80)

    def newuser1(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            if cursor.fetchone():
                print("Username already exists.")
            else:
                self.add_user(username, password)
                print("User registered successfully.")
        else:
            print("Please fill in both fields.")

    def add_user(self, username, password):
        # Add user to the database
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        connection.commit()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check credentials against the database
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        if cursor.fetchone():
            self.root.destroy()  # Close the login window
            main_window = Tk()
            IMS(main_window)  # Open the main application window
            main_window.mainloop()
        else:
            Label(self.root, text="Invalid credentials. Try again.", fg="red", font=("times new roman", 10), bg="#ffffff").place(x=110, y=220)


class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed by BYTE ME")
        self.root.config(bg="white")

        # == Title == 
        self.icon_title = PhotoImage(file=r"C:\java dsa\tkinter\lol\logo1.png")
        title = Label(self.root, text="Inventory Management System", image=self.icon_title, compound=LEFT,
                      font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

        # === Logout Button ===
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"), bg="yellow",
                            cursor="hand2", command=exit1)
        btn_logout.place(x=1100, y=10, height=50, width=150)

        # === Clock ===
        self.lbl_clock = Label(self.root, font=("times new roman", 15, "italic"), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)
        self.update_clock()  # Initialize clock update

        # === Footer ===  
        self.footer_frame = Frame(self.root, bg="#4d636d")
        self.footer_frame.pack(side=BOTTOM, fill=X)

        self.lbl_footer = Label(self.footer_frame, text="IMS-Inventory Management System | Developed by BYTE ME\nFor Technical Support: Contact *84******42", 
                                font=("times new roman", 10, "italic"), bg="#4d636d", fg="white")
        self.lbl_footer.pack()

    def update_clock(self):
        current_time = datetime.now().strftime("Date: %d-%m-%Y \t Time: %H:%M:%S")
        self.lbl_clock.config(text="Welcome to Inventory Management System\t\t" + current_time)
        self.root.after(1000, self.update_clock)

 
        # === Left Menu ===
        self.MenuLogo = Image.open(r"C:\java dsa\tkinter\lol\menu_im.png")
        self.MenuLogo = self.MenuLogo.resize((200, 200), Image.Resampling.NEAREST)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu = Frame(self.root, bd=10, relief=RIDGE, bg="grey")
        LeftMenu.place(x=0, y=102, width=200, height=565)

        lbl_menuLogo = Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X)

        # === Menu Buttons ===
        self.icon_side = PhotoImage(file=r"C:\java dsa\tkinter\lol\side.png")

        btn_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20, "bold"), bg="#009688")
        btn_menu.pack(side=TOP, fill=X)
        btn_employee = Button(LeftMenu, text="Employee", image=self.icon_side, compound=LEFT, padx=5, anchor="w",
                              font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2")
        btn_employee.pack(side=TOP, fill=X)
        btn_supplier = Button(LeftMenu, text="Supplier", image=self.icon_side, compound=LEFT, padx=5, anchor="w",
                              font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2")
        btn_supplier.pack(side=TOP, fill=X)
        btn_category = Button(LeftMenu, text="Category", image=self.icon_side, compound=LEFT, padx=5, anchor="w",
                              font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2")
        btn_category.pack(side=TOP, fill=X)
        btn_product = Button(LeftMenu, text="Product", image=self.icon_side, compound=LEFT, padx=5, anchor="w",
                             font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2")
        btn_product.pack(side=TOP, fill=X)
        btn_sales = Button(LeftMenu, text="Sales", image=self.icon_side, compound=LEFT, padx=5, anchor="w",
                           font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2")
        btn_sales.pack(side=TOP, fill=X)
        btn_exit = Button(LeftMenu, text="Exit", image=self.icon_side, compound=LEFT, padx=5, anchor="w",
                          font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2", command=exit1)
        btn_exit.pack(side=TOP, fill=X)

        # === Main Content Section ===
        self.lbl_employee = Label(self.root, text="Total Employees\n[ 0 ]", bd=5, relief=RIDGE, 
                                  bg="#33bbf9", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_employee.place(x=300, y=120, width=300, height=150)

        self.lbl_supplier = Label(self.root, text="Total Suppliers\n[ 0 ]", bd=5, relief=RIDGE, 
                                  bg="#ff5722", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_supplier.place(x=650, y=120, width=300, height=150)

        self.lbl_category = Label(self.root, text="Total Categories\n[ 0 ]", bd=5, relief=RIDGE, 
                                  bg="#009688", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_category.place(x=1000, y=120, width=300, height=150)

        self.lbl_product = Label(self.root, text="Total Products\n[ 0 ]", bd=5, relief=RIDGE, 
                                 bg="#607d8b", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_product.place(x=300, y=300, width=300, height=150)

        self.lbl_sales = Label(self.root, text="Total Sales\n[ 0 ]", bd=5, relief=RIDGE, 
                               bg="#ffc107", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_sales.place(x=650, y=300, width=300, height=150)

      


# Run the application
root = Tk()
login = Login(root)
root.mainloop()
cursor.close()
connection.close()