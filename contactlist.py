import tkinter as tk
from tkinter import messagebox

contacts = []


def update_contact_list():
    contact_listbox.delete(0, tk.END)  
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['first_name']} - {contact['phone']} - {contact['email']} - {contact['address']}")


def add_contact():
    first_name = first_name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()
    
    if not first_name or not phone or not email or not address:
        messagebox.showerror("Error", "First Name, Phone, Email, and Address are required!")
        return

    contacts.append({"first_name": first_name, "phone": phone, "email": email, "address": address})
    messagebox.showinfo("Success", f"Contact {first_name} added successfully!")
    clear_fields()
    update_contact_list()


def edit_contact():
    selected_contact_index = contact_listbox.curselection()
    if not selected_contact_index:
        messagebox.showerror("Error", "Please select a contact to edit!")
        return

    new_first_name = first_name_entry.get().strip()
    new_phone = phone_entry.get().strip()
    new_email = email_entry.get().strip()
    new_address = address_entry.get().strip()

    if not new_first_name or not new_phone or not new_email or not new_address:
        messagebox.showerror("Error", "First Name, Phone, Email, and Address are required!")
        return

    contacts[selected_contact_index[0]] = {"first_name": new_first_name, "phone": new_phone, "email": new_email, "address": new_address}
    messagebox.showinfo("Success", f"Contact {new_first_name} updated successfully!")
    clear_fields()
    update_contact_list()


def delete_contact():
    selected_contact_index = contact_listbox.curselection()
    if not selected_contact_index:
        messagebox.showerror("Error", "Please select a contact to delete!")
        return
    
    contact = contacts.pop(selected_contact_index[0])
    messagebox.showinfo("Deleted", f"Contact {contact['first_name']} deleted successfully!")
    update_contact_list()


def search_contact():
    search_first_name = search_entry.get().strip().lower()
    if not search_first_name:
        messagebox.showerror("Error", "Please enter a first name to search!")
        return

    for contact in contacts:
        if contact['first_name'].lower() == search_first_name:
            messagebox.showinfo("Contact Found", f"First Name: {contact['first_name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
            return

    messagebox.showerror("Not Found", "Contact not found!")

def clear_fields():
    first_name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Contact Book")
root.geometry("600x600")

form_frame = tk.Frame(root)
form_frame.pack(pady=10)

tk.Label(form_frame, text="First Name:", font=('Arial', 12)).grid(row=0, column=0, padx=5, pady=5)
first_name_entry = tk.Entry(form_frame, font=('Arial', 12))
first_name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Phone:", font=('Arial', 12)).grid(row=1, column=0, padx=5, pady=5)
phone_entry = tk.Entry(form_frame, font=('Arial', 12))
phone_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Email:", font=('Arial', 12)).grid(row=2, column=0, padx=5, pady=5)
email_entry = tk.Entry(form_frame, font=('Arial', 12))
email_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Address:", font=('Arial', 12)).grid(row=3, column=0, padx=5, pady=5)
address_entry = tk.Entry(form_frame, font=('Arial', 12))
address_entry.grid(row=3, column=1, padx=5, pady=5)

add_button = tk.Button(form_frame, text="Add Contact", font=('Arial', 12), command=add_contact, bg='#4682B4', fg='white')
add_button.grid(row=4, column=0, padx=5, pady=10)

edit_button = tk.Button(form_frame, text="Edit Contact", font=('Arial', 12), command=edit_contact, bg='#FFA500', fg='white')
edit_button.grid(row=4, column=1, padx=5, pady=10)

delete_button = tk.Button(form_frame, text="Delete Contact", font=('Arial', 12), command=delete_contact, bg='#FF6347', fg='white')
delete_button.grid(row=5, column=0, padx=5, pady=10)

list_frame = tk.Frame(root)
list_frame.pack(pady=10)

contact_listbox = tk.Listbox(list_frame, font=('Arial', 12), width=70, height=8)
contact_listbox.pack(side=tk.LEFT, padx=10)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

contact_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=contact_listbox.yview)

search_frame = tk.Frame(root)
search_frame.pack(pady=10)

tk.Label(search_frame, text="Search Contact:", font=('Arial', 12)).grid(row=0, column=0, padx=5, pady=5)
search_entry = tk.Entry(search_frame, font=('Arial', 12))
search_entry.grid(row=0, column=1, padx=5, pady=5)

search_button = tk.Button(search_frame, text="Search", font=('Arial', 12), command=search_contact, bg='#4682B4', fg='white')
search_button.grid(row=1, column=0, padx=5, pady=10)

clear_button = tk.Button(search_frame, text="Clear Fields", font=('Arial', 12), command=clear_fields, bg='#DAA520', fg='white')
clear_button.grid(row=1, column=1, padx=5, pady=10)

root.mainloop()
