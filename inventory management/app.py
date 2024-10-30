import mysql.connector
import tkinter as tk
from tkinter import messagebox, ttk
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="inventory_db"
)
cursor = connection.cursor()
def add_item():
    item_name = entry_name.get()
    quantity = entry_quantity.get()
    price = entry_price.get()
    
    if item_name and quantity and price:
        cursor.execute("INSERT INTO inventory (item_name, quantity, price) VALUES (%s, %s, %s)",
                       (item_name, int(quantity), float(price)))
        connection.commit()
        messagebox.showinfo("Success", "Item added successfully!")
        entry_name.delete(0, tk.END)
        entry_quantity.delete(0, tk.END)
        entry_price.delete(0, tk.END)
        view_items()
    else:
        messagebox.showerror("Error", "All fields are required!")
def view_items():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM inventory")
    items = cursor.fetchall()
    for item in items:
        tree.insert("", tk.END, values=item)
def update_item():
    selected_item = tree.selection()
    if selected_item:
        item_id = tree.item(selected_item)["values"][0]
        new_quantity = entry_quantity.get()
        new_price = entry_price.get()
        
        if new_quantity and new_price:
            cursor.execute("UPDATE inventory SET quantity = %s, price = %s WHERE item_id = %s",
                           (int(new_quantity), float(new_price), item_id))
            connection.commit()
            messagebox.showinfo("Success", "Item updated successfully!")
            view_items()
        else:
            messagebox.showerror("Error", "Quantity and Price are required to update an item.")
    else:
        messagebox.showerror("Error", "No item selected for updating.")
def delete_item():
    selected_item = tree.selection()
    if selected_item:
        item_id = tree.item(selected_item)["values"][0]
        cursor.execute("DELETE FROM inventory WHERE item_id = %s", (item_id,))
        connection.commit()
        messagebox.showinfo("Success", "Item deleted successfully!")
        view_items()
    else:
        messagebox.showerror("Error", "No item selected for deletion.")
root = tk.Tk()
root.title("Inventory Management System")
root.geometry("600x400")
tk.Label(root, text="Item Name:").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)
tk.Label(root, text="Quantity:").grid(row=1, column=0, padx=10, pady=5)
entry_quantity = tk.Entry(root)
entry_quantity.grid(row=1, column=1, padx=10, pady=5)
tk.Label(root, text="Price:").grid(row=2, column=0, padx=10, pady=5)
entry_price = tk.Entry(root)
entry_price.grid(row=2, column=1, padx=10, pady=5)
tk.Button(root, text="Add Item", command=add_item).grid(row=3, column=0, padx=10, pady=10)
tk.Button(root, text="Update Item", command=update_item).grid(row=3, column=1, padx=10, pady=10)
tk.Button(root, text="Delete Item", command=delete_item).grid(row=3, column=2, padx=10, pady=10)
columns = ("ID", "Name", "Quantity", "Price")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Quantity", text="Quantity")
tree.heading("Price", text="Price")
tree.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
view_items()
root.mainloop()
cursor.close()
connection.close()
