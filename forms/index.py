import tkinter.messagebox
from tkinter import *
from forms.form_master import MasterPanel
from forms.home import Home
from forms.form_signup import signupForm

from forms.form_login import loginForm
import pyrebase


class index:

    def __init__(self):
        global userEntry
        global passEntry
        global firebase
        global auth
        firebaseConfig={
        'apiKey': "AIzaSyDSZjomBNX_I3NjjpOIK4-pGIziuEx4ksg",
        'authDomain': "vozasenas.firebaseapp.com",
        'databaseURL':"https://vozasenas-default-rtdb.firebaseio.com/",
        'projectId': "vozasenas",
        'storageBucket': "vozasenas.appspot.com",
        'messagingSenderId': "582507067663",
        'appId': "1:582507067663:web:fdab16b877d7f16b6ce67a",
        'measurementId': "G-FNDHYGXZTG"
        }

        firebase=pyrebase.initialize_app(firebaseConfig)
        auth=firebase.auth()

        # def logIn():
        #     username=userEntry.get()
        #     password=passEntry.get()
        #     print(f"diste click\n usuario:{username}\n contraseña {password}")
        #     try:
        #         # user=auth.create_user_with_email_and_password(username,password)
        #         user=auth.sign_in_with_email_and_password(username,password)
        #         print("Sesión iniciada con exito")
        #         window.destroy()
        #         Home()
        #     except:
        #         tkinter.messagebox.showerror(title="error",message="Credenciales incorrectas")

        def LogInForm():
            window.destroy()
            loginForm()


        def SignUpForm():
            window.destroy()
            signupForm()



        window = Tk()

        window.geometry("1000x600")
        window.configure(bg = "#ffffff")
        window.title("vosAseñas")
        canvas = Canvas(
            window,
            bg = "#ffffff",
            height = 600,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file =f"./images/signup/background.png")
        background = canvas.create_image(
            668.5, 294.5,
            image=background_img)

        canvas.create_text(
            740.0, 137.5,
            text = "BIENVENIDO",
            fill = "#000468",
            font = ("Inter-Bold", int(48.0)))

        

        logInimg = PhotoImage(file = f"./images/signup/img1.png")
        logInBtn = Button(
            image = logInimg,
            borderwidth = 0,
            highlightthickness = 0,
            command = LogInForm,
            relief = "flat")

        logInBtn.place(
            x = 678, y = 300,
            width = 123,
            height = 22)



        img1 = PhotoImage(file = f"./images/login/img1.png")
        b1 = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = SignUpForm,
            relief = "flat")

        b1.place(
            x = 678, y = 350,
            width = 123,
            height = 22)
        window.resizable(False, False)
        #window.resizable(True, True)
        window.mainloop()
