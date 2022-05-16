#========================================
#
# this module is for the login gui codes only
# written by matt upton-cashmore
# last checked 16/05/22
# known bugs: none
# NOTES - adjust all variables for settings
#=============================================
from tkinter import *






def create_settings_gui():

    global form
    global welcomeLabel
    form = Tk()
    form.title("login screen")
    form.geometry("550x280")
    # creating welcome label:
    welcomeLabel = Label(form, text="welcome to the settings ")
    welcomeLabel.config(font=("Times new roman", 14), )
    welcomeLabel.place(relx=0.3, rely=0.05, relwidth=0.3, relheight=0.2)

    # making the weight labels nd height labels






    loginButton = Button(form, text="login", width=12, borderwidth=2, relief="solid", command=lambda:
    calcbmi(form, userEntry, passwordEntry))
    loginButton.place(relx=0.2, rely=0.8, relwidth=0.15, relheight=0.1)
    loginButton.config(bg="#FFFFFF")



    menubar = Menu(form)
    form.config(menu=menubar)

    file_menu = Menu(menubar)

    file_menu.add_command(label="Exit", command=lambda: exit_yes_no(form))

    menubar.add_cascade(label="File", menu=file_menu)

    file_menu.add_command(label="Colour Change", command=lambda: colourChange())