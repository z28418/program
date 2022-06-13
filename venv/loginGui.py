#========================================
#
# this module is for the login gui codes only
# written by matt upton-cashmore
# last checked 16/05/22
# known bugs: none
# NOTES - buttons say calc bmi which needs to be updated with corresponding function
#=============================================
from output_messages import*

from tkinter.colorchooser import askcolor
from settingsGui import *

from tkinter import *
from tkinter import Menu
from tkinter import messagebox


def CreateGUI():
    
    global  form
    global welcomeLabel
    form = Tk()
    form.title("login screen")
    form.geometry("550x280")
        # creating welcome label:
    welcomeLabel = Label(form, text="welcome to the login ")
    welcomeLabel.config(font=("Times new roman", 14),)
    welcomeLabel.place(relx = 0.3,rely = 0.05,relwidth = 0.3,relheight = 0.2)

        # making the weight labels nd height labels
    usernamelabel = Label(form, text="enter username")
    passwordlabel = Label(form, text="enter password")
    usernamelabel.place(relx = 0.07,rely = 0.35,relwidth = 0.3,relheight = 0.1)
    passwordlabel.place(relx = 0.07,rely = 0.55,relwidth = 0.3,relheight = 0.1)
    usernamelabel.config(bg = "#FFFFFF")
    passwordlabel.config(bg = "#FFFFFF")


        # making the textboxes :
    userEntry = Entry(form, width="30", borderwidth=2, relief="solid",)
    userEntry.place(relx = 0.4,rely = 0.35,relwidth = 0.4,relheight = 0.1)
    passwordEntry = Entry(form, width="30", borderwidth=2, relief="solid",)
    passwordEntry.place(relx = 0.4,rely = 0.55,relwidth = 0.4,relheight = 0.1)
        # making buttons:


    clearButton = Button(form, text="Clear", width=12, borderwidth=2, relief="solid", command=lambda:
    clearboxes(userEntry, passwordEntry))
    clearButton.place(relx = 0.4,rely = 0.8,relwidth = 0.15,relheight = 0.1)
    clearButton.config(bg = "#FFFFFF")


    loginButton = Button(form, text="login", width=12, borderwidth=2, relief="solid", command=lambda:
    calcbmi(form, userEntry, passwordEntry))
    loginButton.place(relx = 0.2,rely = 0.8,relwidth = 0.15,relheight = 0.1)
    loginButton.config(bg = "#FFFFFF")


    signupButton = Button(form, text="sign up", width=12, borderwidth=2, relief="solid", command=lambda:create_signup_gui(form))

    signupButton.place(relx = 0.6,rely = 0.8,relwidth = 0.15,relheight = 0.1)
    signupButton.config(bg = "#FFFFFF")
    userEntry.focus()



    menubar = Menu(form)
    form.config(menu = menubar)

    file_menu = Menu(menubar)

    file_menu.add_command(label = "Exit",command = lambda: exit_yes_no(form))

    menubar.add_cascade(label = "File", menu = file_menu)

    file_menu.add_command(label="Colour Change", command=lambda : colourChange())



    

    def clearboxes(e1, e2):
        e1.delete(0, "end")
        e2.delete(0, "end")
        e1.focus()

    form.mainloop()


def colourChange():
    global form
    global welcomeLabel

    colors = askcolor(title="Tkinter Color Chooser")
    form.configure(bg=colors[1])

    welcomeLabel.config(bg = colors[1])

if __name__ == "__main__":
    CreateGUI()