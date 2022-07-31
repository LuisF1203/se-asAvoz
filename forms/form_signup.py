import tkinter.messagebox
from tkinter import *
from forms.form_master import MasterPanel
from forms.home import Home
# import main
import pyrebase


class signupForm:

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

        def signup():
            username=userEntry.get()
            password=passEntry.get()
            print(f"diste click\n usuario:{username}\n contraseña {password}")
            try:
                user=auth.create_user_with_email_and_password(username,password)
                print("usuario creado con exito")
                window.destroy()
                Home()
            except:
                tkinter.messagebox.showerror(title="error",message="Usuario ya registrado")
        def loginForm():
            print("diste click")

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

        entry0_img = PhotoImage(file =f"./images/signup/img_textBox0.png")
        entry0_bg = canvas.create_image(
            748.0, 264.5,
            image = entry0_img)

        userEntry = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0,
            font=("",15)
        )

        userEntry.place(
            x = 582.0, y = 235,
            width = 332.0,
            height = 57)

        canvas.create_text(
            740.0, 137.5,
            text = "CREA USUARIO",
            fill = "#000468",
            font = ("Inter-Bold", int(48.0)))

        canvas.create_text(
            630, 210,
            text = "username",
            fill = "#8C8C8C",
            font = ("Inter-Medium", int(20.0)))

        entry1_img = PhotoImage(file =f"./images/signup/img_textBox1.png")
        entry1_bg = canvas.create_image(
            748.0, 375.5,
            image = entry1_img)

        passEntry = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0,
            font=("",15),
            show="*"

        )

        passEntry.place(
            x = 582.0, y = 346,
            width = 332.0,
            height = 57)

        canvas.create_text(
            630, 320,
            text = "password",
            fill = "#8C8C8C",
            font = ("Inter-Medium", int(20.0)))

        img0 = PhotoImage(file =f"./images/signup/img0.png")
        BtnSign = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = signup,
            relief = "flat",
            cursor="target"
            )

        BtnSign.place(
            x = 650, y = 445,
            width = 179,
            height = 43)
        BtnSign.bind("<Return>",(lambda x: print("") 
        
        #event:btn_clicked()
        
        ))

        # img1 = PhotoImage(file = f"./images/signup/img1.png")
        # b1 = Button(
        #     image = img1,
        #     borderwidth = 0,
        #     highlightthickness = 0,
        #     command = loginForm,
        #     relief = "flat")

        # b1.place(
        #     x = 678, y = 540,
        #     width = 123,
        #     height = 22)

        # canvas.create_text(
        #     740.0, 526.5,
        #     text = "Tienes cuenta?",
        #     fill = "#000000",
        #     font = ("Inter-Medium", int(10.0)))

        window.resizable(False, False)
        #window.resizable(True, True)
        window.mainloop()
