import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage



window = tk.Tk()
window.title("Application")
window.geometry('800x500')

bg_image = PhotoImage(file="app/gui/assets/background_city.png")
icon = PhotoImage(file="app/gui/assets/car-logo.png")
window.iconphoto(True, icon)

back_ground_label = tk.Label(window, image=bg_image)
back_ground_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window, bg="#333333", bd=5)
frame.place(relx=0.5, rely=0.5, anchor='center')

def login():
    username = "amir"
    password = "12345"
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title="Login Success", message="you successfully logged in")
    else:
        messagebox.showerror(title="Error", message="Wrong pass wowoedeflk")


login_label = tk.Label(frame, text="Login", bg="#333333", fg="#ffffff", font=("Arial", 20))
username_label = tk.Label(frame, text="Username", bg="#333333",fg='#ffffff',font=("Arial", 15))
username_entry = tk.Entry(frame, font=("Arial", 10))
password_entry = tk.Entry(frame, show="*", font=("Arial", 10))
password_label = tk.Label(frame,
                            text="Password", 
                            bg="#333333",
                            fg='#ffffff',
                            font=("Arial", 15))
login_button = tk.Button(frame,
                        relief="groove",
                        text="Login",
                        bg="#333333",
                        fg='#ffffff',
                        font=("Arial", 15),
                        command=login)


login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=10)
username_label.grid(row=1, column=0, padx=5, pady=5)
username_entry.grid(row=1, column=1, padx=5, pady=5)
password_label.grid(row=2, column=0, padx=5, pady=5)
password_entry.grid(row=2, column=1, padx=5, pady=5)
login_button.grid(row=3, column=0, columnspan=2, pady=10)

window.mainloop()