from tkinter import Tk, Label, Frame, Entry, ttk, Checkbutton, Button, StringVar, messagebox, IntVar
from tkinter.ttk import Combobox

from PIL import Image, ImageTk
import pymysql

class First:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1700x900+0+0")
        self.root.config(bg="white")
        # ===BG Image===
        self.bg = ImageTk.PhotoImage(file="images/862206.jpg")
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        # ===Left Image===
        self.left = ImageTk.PhotoImage(file="images/harveywinner.jpg")
        left = Label(self.root, image=self.left).place(x=20, y=95, relwidth=0.40, relheight=0.68)

        # ====Register Frame====width=700, height=700
        frame1: Frame = Frame(self.root, bg="white")
        frame1.place(x=580, y=100, width=600, height=500)

        title = Label(frame1, text="Welcome to Photo Editor", font=("Arial", 25, "bold"), bg="white", fg="blue").place(x=50, y=30)

        btn_register = Button(frame1, text="Register", font=("arial", 20), bg="blue", fg="white", bd=0,
                       cursor="hand2",command=self.register_window).place(x=130, y=200, relwidth=0.3, relheight=0.1)
        btn_login = Button(frame1, text="Sign In", font=("arial", 20), bg="Red", fg="white", bd=0,
                              cursor="hand2",command=self.login_window).place(x=130, y=300, relwidth=0.3, relheight=0.1)
        #btn_editor = Button(frame1, text="Start Editing", font=("arial", 20), bg="Red", fg="white", bd=0,
         #                     cursor="hand2",command=self.editor_window).place(x=130, y=200, relwidth=0.3, relheight=0.1)

    def register_window(self):
        self.root.destroy()
        import register

    def login_window(self):
        self.root.destroy()
        import login

    def editor_window(self):
        self.root.destroy()
        import init

root = Tk()
obj = First(root)
root.iconbitmap(r"C:\Users\Acer\Documents\Login_with_database\images\favicon.ico")
root.mainloop()