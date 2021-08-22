from tkinter import *
import os

def main_acc():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x260")
    main_screen.title("Main")
    Label(text="Click For Login", bg="#7b5cc7", fg="white",
          width="300", height="2", font=("Calibri", 13)).pack(padx=20, pady=23 )
    Button(text="LOGIN", height="2", width="15", fg="#7b5cc7",command=login).pack(padx=1, pady=20)

    main_screen.mainloop()

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("320x350")
    Label(login_screen,text="Enter Details Below to Login!",bg="#7b5cc7", fg="white",
          width="300", height="2",font=("Calibri", 13)).pack(padx=20, pady=23 )
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username",fg="white", bg="#7b5cc7").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()

    Label(login_screen, text="").pack()
    Label(login_screen, text="Password",fg="white", bg="#7b5cc7").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()

    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "a")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
        else:
            password_not_recognised()
    else:
        user_not_found()

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("ERROR")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("ERROR")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen,fg="red", text="User Not Found!").pack(pady=20)
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def delete_login_success():
    login_success_screen.destroy()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()

main_acc()