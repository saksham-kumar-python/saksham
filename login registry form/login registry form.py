from tkinter import *

import os
def delete_suc():
    #closes login succesful screen
    log_suc.destroy()
def delete_pass():
    #closes password wrong screen
    log_pass.destroy()
def delete_user():
    #closes wrong username screen
    log_user.destroy()
def back_log():
    #closes login screen
    pass_entry1.delete(0,END)
    user_entry1.delete(0,END)
    login_scr.destroy()
    
def back_reg():
    #closes registration screen
    user_entry.delete(0,END)
    pass_entry.delete(0,END)
    reg_screen.destroy()
    
    
def pass_wrong():
    #if password is wrong
    global log_pass
    log_pass = Toplevel(login_scr)
    log_pass.geometry("150x70")
    log_pass_text = Label(log_pass, text = "Wrong Password")
    log_pass_text.config(font = ("calibri", "15"))
    log_pass_text.grid(row=1,column=1)
    des_b = Button(log_pass, text = "OK", command = delete_pass,padx=15)
    des_b.grid(row=2,column=1)
def user_wrong():
    #if username is wrong
    global log_user
    log_user = Toplevel(login_scr)
    log_user.geometry("150x70")
    log_user_text = Label(log_user, text = "Wrong Username")
    log_user_text.config(font = ("calibri", "15"))
    log_user_text.grid(row=1,column=1)
    des_b = Button(log_user, text = "OK", command = delete_user,padx=15)
    des_b.grid(row=2,column=1)
def login_success():
    #login succesful
    global log_suc
    log_suc = Toplevel(login_scr)
    log_suc.geometry("100x100")
    log_suc_text = Label(log_suc, text = "Login Success")
    log_suc_text.config(font = ("calibri", "15"))
    log_suc_text.grid(row=1,column=1)
    des_b = Button(log_suc, text = "OK", command = delete_suc,padx=15)
    des_b.grid(row=2,column=1)
def login_user():
    #checks username and password
    username1 = user_entry1.get()
    password1 = pass_entry1.get()
    user_entry1.delete(0, END)
    pass_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            pass_wrong()
    else:
        user_wrong()
def hide_pass():
    #hides password in login scr
    get = pass_entry1.get()
    pass_entry1.delete(0,END)
    bullet = "\u2022"
    p_entry1 = Entry(login_scr,show = bullet,width = "50",textvariable = "password_e ")
    p_entry1.config(font = ("Arial Tur", "13"))
    p_entry1.grid(row=5,column=1,ipady=2)
    p_entry1.insert(0, get)
    photo = PhotoImage(file = r"images.png")
    eye = Button(login_scr, text = "show",command= show_pass)
    eye.grid(row=5,column=3)
def show_pass():
    #shows password in login screen
    get = pass_entry1.get()
    pass_entry1.delete(0,END)
    global a
    a = ""
    
    p_entry1 = Entry(login_scr,show = a,width = "50",textvariable = "password_e ")
    p_entry1.config(font = ("Arial Tur", "13"))
    p_entry1.grid(row=5,column=1,ipady=2)
    p_entry1.insert(0, get)
    hide_p = Button(login_scr, text = "hide",command=hide_pass,padx=3.4)
    hide_p.grid(row=5,column=3)

def login():
    #login screen
    global user_entry1
    global pass_entry1
    global login_scr
    login_scr = Toplevel(win)
    login_scr.title("Login Screen")
    login_scr.geometry("700x300")
    heading = Label(login_scr, text = "Enter the following details")
    heading.config(font = ("Lucida Console", "15"))
    heading.grid(row=0,column=1)
    Label(login_scr,text = "").grid(row=1,column=0)
    Label(login_scr,text = "").grid(row=2,column=0)
    user_text = Label(login_scr, text = "Enter Username: ")
    user_text.config(font = ("Lucida Console", "15"))
    user_text.grid(row=3,column=0)
    user_entry1 =Entry(login_scr,width = "50",textvariable = "username_e")
    user_entry1.config(font = ("Arial Tur", "13"))
    user_entry1.grid(row=3,column=1,ipady=2)
    Label(login_scr,text = "").grid(row=4,column=0)
    pass_text = Label(login_scr, text = "Enter Password: ")
    pass_text.config(font = ("Lucida Console", "15"))
    pass_text.grid(row=5,column=0)
    eye = Button(login_scr, text = "show",command= show_pass)
    eye.grid(row=5,column=3)
    bullet = "\u2022"
    pass_entry1 = Entry(login_scr,show = bullet,width = "50",textvariable = "password_e ")
    pass_entry1.config(font = ("Arial Tur", "13"))
    pass_entry1.grid(row=5,column=1,ipady=2)
    Label(login_scr,text = "").grid(row=6,column=0)
    register_b = Button(login_scr, text = "Log In",command = login_user, padx = 10,pady=10)
    register_b.config(font = ("Lucida console", "13"))
    register_b.grid(row=7,column=1)
    
    back_b = Button(login_scr, text = "Back",command = back_log, padx = 20,pady=10)
    back_b.config(font = ("Lucida console", "13"))
    back_b.grid(row=8,column=1)

def register_user():
    #checks if username already exists
    username = user_entry.get()
    password = pass_entry.get()
    list_file = os.listdir()
    if username in list_file:
        user_same = Label(reg_screen, text = "Username already exists", fg = "red")
        user_same.config(font= ("Arial Tur","15"))
        user_same.grid(row=8,column=1)
    else:
        file = open(username, "w")
        file.write(username)
        space = " \n"
        file.write(space)
        file.write(password)
        file.close()
        user_entry.delete(0,END)
        pass_entry.delete(0,END)

        reg_success = Label(reg_screen, text = "Registration Success!",fg = "Green")
        reg_success.config(font= ("Arial Tur","15"))
        reg_success.grid(row=8,column=1)
def hide_pass1():
    #hides password in registration screen
    get = pass_entry.get()
    pass_entry.delete(0,END)
    bullet = "\u2022"
    p_entry = Entry(reg_screen,show = bullet,width = "50",textvariable = "password_e ")
    p_entry.config(font = ("Arial Tur", "13"))
    p_entry.grid(row=5,column=1,ipady=2)
    p_entry.insert(0, get)
    
    eye = Button(reg_screen, text = "show",command= show_pass1)
    eye.grid(row=5,column=2)
def show_pass1():
    #shows password in registration screen
    get = pass_entry.get()
    pass_entry.delete(0,END)

    
    p_entry = Entry(reg_screen,show = "",width = "50",textvariable = "password_e ")
    p_entry.config(font = ("Arial Tur", "13"))
    p_entry.grid(row=5,column=1,ipady=2)
    p_entry.insert(0, get)
    show_p = Button(reg_screen, text = "hide",command=hide_pass1,padx=3.4)
    show_p.grid(row=5,column=2)
def register():
    #registration screen
    global reg_screen
    global user_entry
    global pass_entry
    reg_screen = Toplevel(win)
    reg_screen.title("Registration Screen")
    reg_screen.geometry("700x300")
    heading = Label(reg_screen, text = "Enter the following details")
    heading.config(font = ("Lucida Console", "15"))
    heading.grid(row=0,column=1)
    Label(reg_screen,text = "").grid(row=1,column=0)
    Label(reg_screen,text = "").grid(row=2,column=0)
    user_text = Label(reg_screen, text = "Enter Username: ")
    user_text.config(font = ("Lucida Console", "15"))
    user_text.grid(row=3,column=0)
    user_entry =Entry(reg_screen,width = "50",textvariable = "username_e")
    user_entry.config(font = ("Arial Tur", "13"))
    user_entry.grid(row=3,column=1,ipady=2)
    Label(reg_screen,text = "").grid(row=4,column=0)
    pass_text = Label(reg_screen, text = "Enter Password: ")
    pass_text.config(font = ("Lucida Console", "15"))
    pass_text.grid(row=5,column=0)
    eye = Button(reg_screen, text = "show", command = show_pass1)
    eye.grid(row=5,column=2)
    bullet = "\u2022"
    pass_entry = Entry(reg_screen,show = bullet,width = "50",textvariable = "password_e ")
    pass_entry.config(font = ("Arial Tur", "13"))
    pass_entry.grid(row=5,column=1,ipady=2)
    Label(reg_screen,text = "").grid(row=6,column=0)
    register_b = Button(reg_screen, text = "Sign Up",command = register_user, padx = 10,pady=10)
    register_b.config(font = ("Lucida console", "13"))
    register_b.grid(row=7,column=1)
    Label(reg_screen,text = "").grid(row=8,column=1)
    back_b = Button(reg_screen, text = "Back",command = back_reg, padx = 20,pady=10)
    back_b.config(font = ("Lucida console", "13"))
    back_b.grid(row=9,column=1)
def main_screen():
    #home screen
    global win
    win = Tk()
    win.title("Home Screen")
    win.geometry("470x300")
    heading = Label(win,text = "login to continue")
    heading.config(font = ("Courier","15"))
    heading.grid(row=0,column=1)
    heading2 = Label(win,text = "Dont't have an account signup for free")
    heading2.config(font=("Courier","15"))
    heading2.grid(row=1,column=1)
    
    Label(win,text = "").grid(row=3,column=1)
    Label(win,text = "").grid(row=4,column=1)
    login_b = Button(win,text = "Login",height = 2,width = 20, command = login)
    login_b.config(font = ("Lucida Console", "13"))
    login_b.grid(row = 5,column=1)
    Label(win,text = "").grid(row=6,column=1)
    register_b = Button(win,text = "Register",height=2,width = 20,command = register)
    register_b.config(font = ("Lucida Console", "13"))
    register_b.grid(row = 7,column=1)
    
main_screen()
    
