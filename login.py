import tkinter as tk

def submit_login():
    # Get the values entered by the user
    username = username_entry.get()
    password = password_entry.get()

    # Check if the username and password fields are empty or contain white space
    if not username.strip() or not password.strip():
        message_label.config(text="Please enter a valid username and password")
        return

    # Check if the username and password are correct
    if username == "Maryam" and password == "12345678":
        message_label.config(text="Login successful!")
        login_window.destroy()
    else:
        message_label.config(text="Incorrect username or password")

# Create the main window
login_window = tk.Tk()
login_window.title("Login Page")
login_window.geometry("500x300")
login_window.config(bg="black")

# Create the username entry field
username_label = tk.Label(login_window, text="Username:", font=("Arial", 12), bg="grey")
username_label.pack(pady=10)
username_entry = tk.Entry(login_window, font=("Arial", 12))
username_entry.pack()

# Create the password entry field
password_label = tk.Label(login_window, text="Password:", font=("Arial", 12), bg="grey")
password_label.pack(pady=10)
password_entry = tk.Entry(login_window, font=("Arial", 12), show="*")
password_entry.pack()

# Create the submit button
submit_button = tk.Button(login_window, text="Submit", font=("Arial", 12), bg="white", command=submit_login)
submit_button.pack(pady=10)

# Create the message label
message_label = tk.Label(login_window, font=("Arial", 12), bg="grey")
message_label.pack(pady=10)

# Run the main loop
login_window.mainloop()