# Original
import mysql.connector
from tkinter import *
import tkinter
import customtkinter
from tkinter import Label, PhotoImage
from PIL import Image, ImageTk


customtkinter.set_appearance_mode("Dark")
def loginPage(logdata):
    global loginPage
    login = customtkinter.CTk()
    login.title('Quiz App Login')
    login.geometry("800x700")
    
    user_name = StringVar()
    password = StringVar()

    # Heading
    heading = Label(login, text="Quiz App Login",
                    fg="cyan", bg="#212325")
    heading.config(font=('calibri 35 italic bold'))
    heading.place(relx=0.1, rely=0.15)
    
    
    # Image
    image = Image.open('login_edited.png')
    imgre = image.resize((280, 280))
    img1 = ImageTk.PhotoImage(imgre)

    img = customtkinter.CTkLabel(
        login, image=img1, fg='black', bg='black')
    img.place(relx=0.6, rely=0.3)
    

    #USER NAME
    ulabel = customtkinter.CTkLabel(
        login, text="Username", fg='white', bg='black')
    ulabel.place(relx=0.15, rely=0.5)
    uname = customtkinter.CTkEntry(login, bg='black', fg='black',
                                textvariable=user_name)
    uname.config(width=15)
    uname.place(relx=0.28, rely=0.5)

    #PASSWORD
    plabel = customtkinter.CTkLabel(
        login, text="Password", fg='white', bg='black')
    plabel.place(relx=0.15, rely=0.6)
    pas = customtkinter.CTkEntry(login, bg='black', fg='black',
                                textvariable=password, show="*")
    pas.config(width=15)
    pas.place(relx=0.28, rely=0.6)

    # QUIT BUTTON
    quit_button = customtkinter.CTkButton(text="Quit", master=login,
                                        corner_radius=15, command=login.destroy)
    quit_button.place(relx=0.1, rely=0.95, anchor=tkinter.CENTER)

    def check():
        for a, b, c in logdata:
            if b == uname.get() and c == pas.get():
                #print(logdata)
                login.destroy()
                import mainquiz_original
                
                
                 
            else:
                error = Label(
                    login, text="Wrong Username or Password!", fg='blue', bg='grey')
                error.place(relx=0.37, rely=0.7)


    #LOGIN BUTTON
    log = customtkinter.CTkButton(
        login, text='Login', command=check,  corner_radius=10)
    log.place(relx=0.35, rely=0.7, anchor=tkinter.CENTER)

    login.mainloop()


def signUpPage():
    fpage.destroy()
    global sup
    sup = customtkinter.CTk()
    sup.title('Quiz App')
    sup.geometry("800x700")

    fname = StringVar()
    uname = StringVar()
    passW = StringVar()

    heading = Label(sup, text="Quiz App Signup",
                    fg="#fc034e", bg="#212325")
    heading.config(font=('calibri 42 italic bold'))
    heading.place(relx=0.1, rely=0.15)
    
    # Image 
    image = Image.open('signup.png')
    imgre = image.resize((280, 280))
    img1 = ImageTk.PhotoImage(imgre)

    img = customtkinter.CTkLabel(
        sup, image=img1, fg='black', bg='black')
    img.place(relx=0.6, rely=0.3)
    
    #full name
    flabel = customtkinter.CTkLabel(
        sup, text="Full Name", fg='white', bg='black')
    flabel.place(relx=0.15, rely=0.4)
    fname = customtkinter.CTkEntry(sup, bg='black', fg='black',
                                   textvariable=fname)
    fname.place(relx=0.28, rely=0.4)

    #username
    ulabel = customtkinter.CTkLabel(
        sup, text="Username", fg='white', bg='black')
    ulabel.place(relx=0.15, rely=0.5)
    user = customtkinter.CTkEntry(sup, bg='black', fg='black',
                                  textvariable=uname)
    user.place(relx=0.28, rely=0.5)

    #password
    plabel = customtkinter.CTkLabel(
        sup, text="Password", fg='white', bg='black')
    plabel.place(relx=0.15, rely=0.6)
    pas = customtkinter.CTkEntry(sup, bg='black', fg='black',
                                 textvariable=passW, show="*")
    pas.place(relx=0.28, rely=0.6)

    def addUserToDataBase():

        fullname = fname.get()
        username = user.get()
        password = pas.get()

        if len(fname.get()) == 0 and len(user.get()) == 0 and len(pas.get()) == 0:
            error = Label(
                text="You haven't enter any field...Please Enter all the fields", fg='black', bg='white')
            error.place(relx=0.37, rely=0.7)

        elif len(fname.get()) == 0 or len(user.get()) == 0 or len(pas.get()) == 0:
            error = Label(text="Please Enter all the fields",
                          fg='black', bg='white')
            error.place(relx=0.37, rely=0.7)

        elif len(user.get()) == 0 and len(pas.get()) == 0:
            error = Label(
                text="Username and password can't be empty", fg='black', bg='white')
            error.place(relx=0.37, rely=0.7)

        elif len(user.get()) == 0 and len(pas.get()) != 0:
            error = Label(text="Username can't be empty",
                          fg='black', bg='white')
            error.place(relx=0.37, rely=0.7)

        elif len(user.get()) != 0 and len(pas.get()) == 0:
            error = Label(text="Password can't be empty",
                          fg='black', bg='white')
            error.place(relx=0.37, rely=0.7)

        else:

            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password='root',
                database='quiz123'
            )

            create = conn.cursor()
            create.execute(
                'CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, USERNAME text,PASSWORD text)')
            create.execute("INSERT INTO userSignUp VALUES (%s,%s,%s)",
                           (fullname, username, password))
            conn.commit()
            create.execute('SELECT * FROM userSignUp')
            z = create.fetchall()
            #print(z)
            #L2.config(text="Username is "+z[0][0]+"\nPassword is "+z[-1][1])
            conn.close()
            sup.destroy()
            loginPage(z)

    def gotoLogin():
        sup.destroy()
        conn = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password='root',
                                       database='quiz123'
                                       )
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z = create.fetchall()
        loginPage(z)

     #signup BUTTON
    sp = customtkinter.CTkButton(sup, text='SignUp', corner_radius=15,
                                 command=addUserToDataBase, bg="black")
    sp.place(relx=0.35, rely=0.7, anchor=tkinter.CENTER)

    # QUIT BUTTON
    quit_button = customtkinter.CTkButton(text="Quit", master=sup,
                                          corner_radius=15,
                                          command=sup.destroy)

    quit_button.place(relx=0.1, rely=0.95, anchor=tkinter.CENTER)

    #Already have a account
    log = customtkinter.CTkButton(sup, text='Already have a Account?', corner_radius=15,
                                  command=gotoLogin)
    log.place(relx=0.35, rely=0.8, anchor=tkinter.CENTER)
    sup.mainloop()



def start():
    global fpage
    fpage = tkinter.Tk()
    fpage.title("Trivia Masters")
    fpage.geometry("1100x700")
    fpage.config(background="#000000")
    img1 = PhotoImage(file="bg_returns.png")
    labelimage = Label(
        fpage,
        image=img1,
        background="#000000",
    )
    labelimage.pack(pady=(80, 40))

    #Button
    button = customtkinter.CTkButton(master=fpage,
                                     text="Start",
                                     command=signUpPage,
                                     corner_radius=0
                                     )
    button.pack(pady=20)
    button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
    fpage.mainloop()


if __name__ == '__main__':
    start()
