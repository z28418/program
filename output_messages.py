#========================================
#
# this module is for the output messages only
# written by matt upton-cashmore
# last checked 16/05/22
# known bugs: none
# NOTES - none
#=============================================

from tkinter import messagebox
from tkinter import *

def exit_yes_no(form):
    exitQ = messagebox.askyesno("exit?","are you sure you want to exit")


    if exitQ == True:
        form.destroy()

