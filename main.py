import customtkinter as ctk
import user_service as us
from tkinter import messagebox
from tkinter import PhotoImage
from sign_language import sign_language
from PIL import Image, ImageTk

c_negro = '#010101'
c_morado = '#7f5af0'
c_verde = '#2cb67d'


def switch_to_signup():
    signup_window = ctk.CTk()
    signup_window.title("Sign Up")
    signup_window.geometry("400x300")
    # Add sign-up form widgets here
    signup_window.mainloop()

def validate_login():
    email = correo.get()
    psw = password.get()
    user_service_inst = us.UserService()

    if email == '' or psw == '':
        print("Email or password is empty")
    else:
        user = user_service_inst.sign_in(email, psw)
        if user:
            print(user)
            print("Login successful")
            messagebox.showinfo("Info", "Logeado satisfactoriamente.")
            root.destroy()
            sign_language()

        else:
            print("Login failed")
            messagebox.showerror("Error", "Correo o contraseña incorrecta.")

root = ctk.CTk()
root.title("Iniciar Secion")
root.geometry("400x500")
root.config(bg = c_negro)

# Load the image using Pillow
image = Image.open('logoUnefa.png')

# Resize the image
resized_image = image.resize((200, 200))  # Set the desired size (width, height)

# Convert the resized image to a PhotoImage object
logo = ImageTk.PhotoImage(resized_image)

frame = ctk.CTkFrame(root, fg_color = c_negro)
frame.grid(row = 0, column = 0, sticky = ctk.NSEW, padx = 50, pady = 50)


frame.columnconfigure([0, 1], weight = 1)
frame.rowconfigure([0, 1, 2, 3, 4], weight = 1)

root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

ctk.CTkLabel(frame, image=logo, text="").grid(columnspan = 2, row = 0)

correo = ctk.CTkEntry(frame, text_color='#fff', font=('sans serif', 12), placeholder_text='Correo electronico', border_color=c_verde, fg_color=c_negro, width=220, height=40)
correo.grid(columnspan = 2, row=1, padx=4, pady=4)

password = ctk.CTkEntry(frame,  text_color='#fff', font=('sans serif', 12), placeholder_text='Contraseña', border_color=c_verde, fg_color=c_negro, width=220, height=40)
password.grid(columnspan = 2, row=2, padx=4, pady=4)

bt_iniciar = ctk.CTkButton(frame, font=('sans serif', 12), border_color=c_verde, fg_color=c_negro, text='Iniciar', corner_radius=12, border_width=4, command=validate_login)
bt_iniciar.grid(columnspan = 2, row=3, padx=4, pady=4)


root.mainloop()