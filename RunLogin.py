import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

#Function to handle login------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()
    if entered_username == 'admin' and entered_password == '123':
        open_student_management()
    else:
        messagebox.showerror("Login Error", "Invalid username or password")

# Function to toggle password visibility
def toggle_password_visibility():
    if password_entry.cget('show') == '•':
        password_entry.config(show='')
        eye_icon_button.config(image=eye_open_icon)
    else:
        password_entry.config(show='•')
        eye_icon_button.config(image=eye_closed_icon)

# Function to open the student management interface------------------------------------------------------------------------------------------------------------------------------------------------
def open_student_management():
    login_window.destroy()
    
    # Create a new window for student management
    student_management_window = tk.Tk()
    student_management_window.title("Student Database Management")
    
    # Define the student management UI here
    # You can create labels, entry fields, buttons, and other widgets
    
    student_management_window.mainloop()
    

# GUI OF LOGIN WINDOW ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("1920x1080")  # Set the window size to fullscreen

bg_image = Image.open("bg.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(login_window, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

frame_width = 450
frame_height = 300
frame_x = (login_window.winfo_screenwidth() - frame_width) // 2  # Center horizontally
frame_y = (login_window.winfo_screenheight() - frame_height) // 2  # Center vertically

frame = tk.Canvas(login_window, bg="white", highlightthickness=0)
frame.place(x=frame_x, y=frame_y, width=frame_width, height=frame_height)

login_label = ttk.Label(frame, text="SIGN UP", foreground="dark orange", background="white", font=("Trebuchet MS", 20,"bold"))
login_label.place(relx=0.1, rely=0.05, anchor="nw") 

username_label = ttk.Label(frame, text="Username", foreground="black", background="white", font=("Trebuchet MS", 12))
username_label.place(relx=0.1, rely=0.3, anchor="w")

username_entry = ttk.Entry(frame, font=("Helvetica", 12), width=39)
username_entry.place(relx=0.1, rely=0.4, anchor="w")

password_label = ttk.Label(frame, text="Password", foreground="black", background="white", font=("Trebuchet MS", 12))
password_label.place(relx=0.1, rely=0.5, anchor="w")

password_entry = ttk.Entry(frame, show='•', font=("Helvetica", 12), width=39)  
password_entry.place(relx=0.1, rely=0.6, anchor="w")

eye_open_image = Image.open("view.png")
eye_open_image = eye_open_image.resize((18, 18), Image.LANCZOS) 
eye_open_icon = ImageTk.PhotoImage(eye_open_image)

eye_closed_image = Image.open("hide.png")
eye_closed_image = eye_closed_image.resize((18, 18), Image.LANCZOS) 
eye_closed_icon = ImageTk.PhotoImage(eye_closed_image)

eye_icon_button = tk.Button(password_entry, image=eye_closed_icon, command=toggle_password_visibility, bd=0, bg="white", cursor="hand2")
eye_icon_button.place(relx=1, rely=0.5, anchor="e")

login_button = tk.Button(frame, text="LOGIN", command=login, width=44, height=2, background="dark orange",foreground="white",font=("Trebuchet MS", 10,"bold"),borderwidth=0,highlightthickness=0, cursor="hand2")
login_button.place(relx=0.1, rely=0.85, anchor="w") 

login_window.mainloop()


