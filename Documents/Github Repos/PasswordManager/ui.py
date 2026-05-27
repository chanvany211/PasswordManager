import tkinter as tk
from tkinter import messagebox
from logic import generate_password, save_entry, search_entry

class PasswordManagerUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password Manager")
        self.root.geometry("400x300")

        # Website
        tk.Label(self.root, text="Website:").pack()
        self.website_entry = tk.Entry(self.root)
        self.website_entry.pack()

        # Username
        tk.Label(self.root, text="Username:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        # Password
        tk.Label(self.root, text="Password:").pack()
        self.password_entry = tk.Entry(self.root)
        self.password_entry.pack()

        # Generate password button
        tk.Button(self.root, text="Generate Password", command=self.generate).pack(pady=5)

        # Save button
        tk.Button(self.root, text="Save Entry", command=self.save).pack(pady=5)

        # Search button
        tk.Button(self.root, text="Search Entry", command=self.search).pack(pady=5)

        self.root.mainloop()

    def generate(self):
        pwd = generate_password()
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, pwd)

    def save(self):
        website = self.website_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        save_entry(website, username, password)
        messagebox.showinfo("Saved", "Entry saved successfully!")

    def search(self):
        website = self.website_entry.get()
        result = search_entry(website)

        if result:
            self.username_entry.delete(0, tk.END)
            self.username_entry.insert(0, result["username"])

            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, result["password"])
        else:
            messagebox.showerror("Not Found", "No entry found for that website.")