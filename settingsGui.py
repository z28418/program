#========================================
#
# this module is for the login gui codes only
# written by matt upton-cashmore
# last checked 16/05/22
# known bugs: none
# NOTES - adjust all variables for settings
#=============================================
from tkinter import *
from tkinter import Menu
from commitUser import *
from tkinter.colorchooser import askcolor
from loginGui import *

def create_signup_gui(w):
    w.destroy()
    global  form
    global welcomeLabel
    form = Tk()
    form.title("login screen")
    form.geometry("550x280")
        # creating welcome label:
    welcomeLabel = Label(form, text="welcome to the sign up ")
    welcomeLabel.config(font=("Times new roman", 14))
    welcomeLabel.place(relx = 0.15,rely = 0.05,relwidth = 0.3,relheight = 0.2)


    usernamelabel = Label(form, text="enter name")
    email_label = Label(form, text="enter email")


    usernamelabel.place(relx = 0.07,rely = 0.25,relwidth = 0.3,relheight = 0.1)
    email_label.place(relx = 0.07,rely = 0.45,relwidth = 0.3,relheight = 0.1)

    addlabel = Label(form, text="enter address")
    addlabel.place(relx=0.07, rely=0.85, relwidth=0.4, relheight=0.1)

    doblabel = Label(form, text="enter date of birth")
    doblabel.place(relx=0.07, rely=0.65, relwidth=0.4, relheight=0.1)





    userEntry = Entry(form, width="30", borderwidth=2, relief="solid",)
    userEntry.place(relx = 0.4,rely = 0.25,relwidth = 0.4,relheight = 0.1)


    emailEntry = Entry(form, width="30", borderwidth=2, relief="solid",)
    emailEntry.place(relx = 0.4,rely = 0.45,relwidth = 0.4,relheight = 0.1)

    DobEntry = Entry(form, width="30", borderwidth=2, relief="solid", )
    DobEntry.place(relx=0.4, rely=0.65, relwidth=0.4, relheight=0.1)


    addEntry = Entry(form, width="30", borderwidth=2, relief="solid", )
    addEntry.place(relx=0.4, rely=0.85, relwidth=0.4, relheight=0.1)


    clearButton = Button(form, text="Clear", width=12, borderwidth=2, relief="solid", command=lambda: CreateGUI())
    clearButton.place(relx = 0.05,rely = 0.85,relwidth = 0.15,relheight = 0.1)

    loginButton = Button(form, text="login", width=12, borderwidth=2, relief="solid", command=lambda:createUser(userEntry,
                                                                                        emailEntry,DobEntry,addEntry))
    loginButton.place(relx = 0.85,rely = 0.9,relwidth = 0.15,relheight = 0.1)



    userEntry.focus()



    menubar = Menu(form)
    form.config(menu = menubar)

    file_menu = Menu(menubar)

    file_menu.add_command(label = "exit",command = form.destroy)

    menubar.add_cascade(label = "file", menu = file_menu)

    file_menu.add_command(label="colour change", command=lambda : colourChange())

    def colourChange():
        global form
        global welcomeLabel

        colors = askcolor(title="Tkinter Color Chooser")
        form.configure(bg=colors[1])

        welcomeLabel.config(bg=colors[1])

    form.mainloop()















