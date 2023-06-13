import tkinter as tk
from tkinter import messagebox


class BankAccount:
    def __init__(self, username, opening_balance, pin):
        self.username = username
        self.balance = opening_balance
        self.pin = pin
        self.transactions = []

    def deposit_funds(self, amount):  # Renamed the method
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")

    def withdraw_funds(self, amount):  # Renamed the method
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: {amount}")
        else:
            messagebox.showerror("Insufficient Balance", "You have insufficient funds.")

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions


class BankAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Heroes Bank Account Management")
        self.root.geometry("800x600")

        # Set a custom color scheme
        self.root.configure(bg="#f0f0f0")  # Set background color

        # Variables to store user input
        self.username_var = tk.StringVar()
        self.balance_var = tk.DoubleVar()
        self.pin_var = tk.StringVar()
        self.amount_var = tk.DoubleVar()

        # Create labels and entry fields for sign-up and login
        tk.Label(
            root, text="Username:", bg="#f0f0f0", fg="#333333", font=("Arial", 12)
        ).grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(root, textvariable=self.username_var)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(
            root,
            text="Opening Balance:",
            bg="#f0f0f0",
            fg="#333333",
            font=("Arial", 12),
        ).grid(row=1, column=0, padx=10, pady=10)
        self.balance_entry = tk.Entry(root, textvariable=self.balance_var)
        self.balance_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(
            root, text="PIN:", bg="#f0f0f0", fg="#333333", font=("Arial", 12)
        ).grid(row=2, column=0, padx=10, pady=10)
        self.pin_entry = tk.Entry(root, textvariable=self.pin_var, show="*")
        self.pin_entry.grid(row=2, column=1, padx=10, pady=10)

        # Create sign-up and login buttons
        self.signup_btn = tk.Button(
            root, text="Sign Up", command=self.sign_up, fg="black", font=("Arial", 12)
        )
        self.signup_btn.grid(row=3, column=0, columnspan=2, pady=10)

        self.login_btn = tk.Button(
            root, text="Login", command=self.login, fg="black", font=("Arial", 12)
        )
        self.login_btn.grid(row=4, column=0, columnspan=2, pady=10)

        # Initialize account as None
        self.account = None

    def sign_up(self):
        username = self.username_var.get()
        balance = self.balance_var.get()
        pin = self.pin_var.get()

        # Create a new BankAccount object
        self.account = BankAccount(username, balance, pin)
        messagebox.showinfo("Account Created", "Account created successfully!")

        # Clear input fields
        self.username_var.set("")
        self.balance_var.set("")
        self.pin_var.set("")

    def login(self):
        username = self.username_var.get()
        pin = self.pin_var.get()

        if (
            self.account
            and self.account.username == username
            and self.account.pin == pin
        ):
            messagebox.showinfo("Login Successful", "Logged in successfully!")
            # Show functionality buttons after successful login
            self.show_functionality_buttons()

            # Remove username label and entry
            self.username_entry.grid_remove()

        else:
            messagebox.showerror("Login Failed", "Invalid username or PIN.")

        # Clear input fields
        self.username_var.set("")
        self.pin_var.set("")

    def show_functionality_buttons(self):
        # Remove sign-up and login buttons
        self.signup_btn.grid_remove()
        self.login_btn.grid_remove()

        # Remove username label
        self.root.grid_slaves(row=0, column=0)[0].grid_forget()

        # Create labels and entry fields for deposit and withdraw
        self.amount_entry_label = tk.Label(self.root, text="Amount:")
        self.amount_entry_label.grid(row=0, column=0, sticky="w", pady=10)
        self.amount_entry = tk.Entry(self.root, textvariable=self.amount_var)
        self.amount_entry.grid(row=0, column=1, sticky="ew", padx=10)

        # Create buttons for deposit and withdraw
        self.deposit_btn = tk.Button(
            self.root, text="Deposit", command=self.deposit_funds, fg="black"
        )
        self.deposit_btn.grid(row=1, column=0, sticky="ew", pady=10, padx=10)

        self.withdraw_btn = tk.Button(
            self.root, text="Withdraw", command=self.withdraw_funds, fg="black"
        )
        self.withdraw_btn.grid(row=1, column=1, sticky="ew", pady=10, padx=10)

        self.balance_btn = tk.Button(
            self.root, text="Check Balance", command=self.check_balance, fg="black"
        )
        self.balance_btn.grid(
            row=2, column=0, columnspan=2, sticky="ew", pady=10, padx=10
        )

        self.transactions_btn = tk.Button(
            self.root,
            text="View Transactions",
            command=self.view_transactions,
            fg="black",
        )
        self.transactions_btn.grid(
            row=3, column=0, columnspan=2, sticky="ew", pady=10, padx=10
        )

        # Center the buttons
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

    def hide_functionality_buttons(self):
        # Remove functionality buttons
        if hasattr(self, "deposit_btn"):
            self.deposit_btn.grid_remove()
            self.withdraw_btn.grid_remove()
            self.balance_btn.grid_remove()
            self.transactions_btn.grid_remove()

        # Remove labels and entry fields for deposit and withdraw
        if hasattr(self, "amount_entry"):
            self.amount_entry.grid_remove()
            tk.Label(self.root, text="Amount:").grid_remove()

    def deposit_funds(self):  # Renamed the method
        if self.account:
            amount = self.amount_var.get()
            self.account.deposit_funds(amount)
            messagebox.showinfo("Deposit", "Amount deposited successfully!")

            # Clear input field
            self.amount_var.set(0)
        else:
            messagebox.showerror("Error", "Please sign up or log in first.")

    def withdraw_funds(self):  # Renamed the method
        if self.account:
            amount = self.amount_var.get()
            self.account.withdraw_funds(amount)
            messagebox.showinfo("Withdrawal", "Amount withdrawn successfully!")

            # Clear input field
            self.amount_var.set(0)
        else:
            messagebox.showerror("Error", "Please sign up or log in first.")

    def check_balance(self):
        if self.account:
            balance = self.account.get_balance()
            messagebox.showinfo(
                "Balance Inquiry", f"Your current balance is: {balance}"
            )
        else:
            messagebox.showerror("Error", "Please sign up or log in first.")

    def view_transactions(self):
        if self.account:
            transactions = self.account.get_transactions()
            if transactions:
                transaction_text = "\n".join(transactions)
                messagebox.showinfo(
                    "Transaction History",
                    f"Your transaction history:\n{transaction_text}",
                )
            else:
                messagebox.showinfo("Transaction History", "No transactions yet.")
        else:
            messagebox.showerror("Error", "Please sign up or log in first.")


if __name__ == "__main__":
    root = tk.Tk()
    app = BankAppGUI(root)

    # Center the content
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(1, weight=1)
    app.signup_btn.grid_configure(pady=(100, 10))
    app.login_btn.grid_configure(pady=10)

    root.mainloop()
