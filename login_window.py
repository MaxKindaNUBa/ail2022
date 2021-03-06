from tkinter import Toplevel, Text, IntVar, Radiobutton, Button
from student_scope import *

container = mainWindow()
infof = userInfoFrame(container)
marksf = markWindow(container)


class topLevel(Toplevel):
    @staticmethod
    def __place_widgets(bgimg, topic):
        bgimg.place(x=0, y=0)
        topic.place(x=10, y=10)

    def get_in_front(self, root):
        self.wm_transient(root)

    def __init__(self, root):
        super().__init__(root)
        self.style = ThemedStyle()
        self.geometry('500x375')
        self.login_icon = PhotoImage(file="login_icon.png")
        self.login_background = PhotoImage(file="login_background_edited.png")
        self.title("Student Mark Processing - Login")
        self.iconphoto(False, self.login_icon)
        self.bgimg = Label(self, image=self.login_background)
        self.topic = Label(self, text="Student mark processing program 2022", font=("Ubuntu", 20)
                           , borderwidth=3, relief=GROOVE)
        self.__place_widgets(self.bgimg, self.topic)

    def set_theme(self, th: str):
        self.style.theme_use(th)


login_page = topLevel(container)


class InfoFrame(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.style = ThemedStyle()
        self.idlabel = Label(self, text="Username :", font=("lora", 15), borderwidth=2, relief=SUNKEN)
        self.passlabel = Label(self, text="Password :", font=("lora", 15), borderwidth=2, relief=SUNKEN)
        self.incorrectlabel = Label(self, text="     ", font=("lora", 15),
                                    foreground="#f54242",
                                    background="#d4d4d2")
        self.idbox = Text(self, height=1, width=15, font=("lora", 15))
        self.passbox = Text(self, height=1, width=15, font=("lora", 15))
        self.optionchooser = IntVar(self)
        self.teacher = Radiobutton(self, text="Teacher", variable=self.optionchooser, value=0, font=("lora", 12),
                                   background="#d4d4d2")
        self.student = Radiobutton(self, text="Student", variable=self.optionchooser, value=1, font=("lora", 12),
                                   background="#d4d4d2")
        self.loginbutt = Button(self, text="Login", command=self.check_correct_login)
        self.__place_widgets()

    def check_correct_login(self):
        if (self.idbox.get(0.0, END).strip() == "Chandran") and (self.passbox.get(0.0, END).strip() == "12345") and (
                self.optionchooser.get() == 1):
            print("login successfull")
            login_page.destroy()
            container.remove_standby()
            infof.place(x=0, y=0)
            marksf.place(x=190, y=0)
            container.change_theme("breeze")
        else:
            self.incorrectlabel.config(text="Incorrect username/password!")

    def get_focus(self):
        self.idbox.focus_set()

    def __place_widgets(self):
        self.idlabel.grid(row=0, column=0, sticky=W)
        self.passlabel.grid(row=1, column=0, sticky=W)
        self.idbox.grid(row=0, column=1, sticky=W)
        self.passbox.grid(row=1, column=1, sticky=W)
        self.incorrectlabel.grid(row=2, column=0, columnspan=2)
        self.teacher.grid(column=0, row=3, sticky=E)
        self.student.grid(column=1, row=3, sticky=W)
        self.loginbutt.grid(row=4, column=1, sticky=W)
        self.place(x=120, y=140)


login_frame = InfoFrame(login_page)
login_frame.get_focus()
login_frame.style.theme_use("elegance")

container.mainloop()
