
# import random

# lower = "abcdefghijklmnñopqrstuvwxyz"
# upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# numbers = "0123456789"
# symbols = "!@#$%^&*()_+-={}[]:;<>,."

# string = lower + upper + numbers + symbols
# length = int(input("INGRESA LA LONGITUD DE TU PASSWORD: "))
# password = "".join(random.sample(string, length))

# print("tu contraseña es: " + password)



#######################################################################


# import tkinter
# import customtkinter as ctk


# customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
# customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# app = customtkinter.CTk()  # create CTk window like you do with the Tk window
# app.geometry("400x240")

# def button_function():
#     print("button pressed")

# # Use CTkButton instead of tkinter Button
# button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
# button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# app.mainloop()


import random
from tkinter import *
import tkinter as tk


#funcion para generar la contraseña
def password_generator():
    password = ""
    lower = "abcdefghijklmnñopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+-={}[]:;<>,."

    string = lower + upper + numbers + symbols
    #length = int(input("INGRESA LA LONGITUD DE TU PASSWORD: "))
    password = "".join(random.sample(string))
    #password_label.configure(text=password)
    # print("tu contraseña es: " + password)

#ventana principal
def gui():
    principal = Tk()
    principal.title("Generador de Contraseñas")
    principal.geometry("600x100")
    #principal.resizable(False,False)

    #se crea la caja de texto que contendra la password
    text_password = Text(principal, height=3, width=56, borderwidth=2)
    text_password.grid(row=2, column=0, columnspan=3, sticky=W, ipady=4, padx=16, pady=16)
    text_password["state"]=DISABLED

    #se crea el nombre del label
    nombre_label = Label(principal, text="Ingresa la longitud de la contraseña:")
    nombre_label.grid(row=0, column=0,padx=5, pady=5)

    #se crea el label que producira la contraseña
    # password_label= Label(principal, width=40)
    # password_label.grid(row=1, column=1,sticky='ew')

    #se crea el entry para ingresar la contraseña
    entrada = Entry(principal, width=40)
    entrada.insert(0, "Escriba aqui la longitud de la contraseña...")
    entrada.grid(row=0, column=1)

    #se crea el boton para generar la contraseña
    button = Button(principal, text="Generar Contraseña", command=password_generator)
    button.grid(row=1, column=0, sticky='w',padx=5)

def init_app():
    gui.mainloop()

if __name__ == '__main__':
    init_app()
