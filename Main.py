# Original
from cProfile import label
from fnmatch import fnmatch
from gzip import FNAME
from this import d
from tkinter import LEFT, IntVar, Button, Label, PhotoImage, Radiobutton, Tk, Entry ###
from itertools import count, cycle
from tkinter import messagebox as mb ###
import csv
from unicodedata import name
from pandas import *
import numpy
from tkinter.messagebox import QUESTION
from re import A, I
import pandas as pd
import requests as r
from matplotlib.ft2font import BOLD
from cv2 import destroyAllWindows
from unittest import result
from tracemalloc import start
from tkinter.font import ITALIC
import tkinter as tk
from multiprocessing.sharedctypes import Value
from io import BytesIO
from gettext import install
from email.mime import image
from doctest import master
import tkinter.messagebox
import PIL
from turtle import width
import mysql.connector ###
from tkinter import *
import tkinter
import customtkinter
from tkinter import Label, PhotoImage ###
from PIL import Image, ImageTk ###


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
    heading.config(font=('calibri 100 italic bold'))
    heading.place(relx=0.1, rely=0.15)
    
    
    # Image
    image = Image.open('login_edited.png')
    imgre = image.resize((600, 600))
    img1 = ImageTk.PhotoImage(imgre)

    img = customtkinter.CTkLabel(
        login, image=img1, fg='black', bg='black')
    img.place(relx=0.6, rely=0.3)
    

    #USER NAME
    user_name = StringVar()
    ulabel = customtkinter.CTkLabel(
        login, text="Username", fg='white', bg='black')
    ulabel.place(relx=0.15, rely=0.5)
    uname = customtkinter.CTkEntry(login, bg='black', fg='black',
                                textvariable=user_name)
    uname.config(width=15)
    uname.place(relx=0.28, rely=0.5)
    
        
    # PASSWORD
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
        global b
        for a, b, c in logdata:
            if b == uname.get() and c == pas.get():
                #print(logdata)
                login.destroy()
                ### Ignore this file. Use mainlogreg.py ###
                # import required classes from tkinter
                # and import messagebox as mb from tkinter

                customtkinter.set_appearance_mode("Dark")
                # For GIF


                class ImageLabel(tk.Label):
                    def load(self, im):
                        if isinstance(im, str):
                            im = Image.open(im)
                        frames = []

                        try:
                            for i in count(1):
                                frames.append(ImageTk.PhotoImage(im.copy()))
                                im.seek(i)
                        except EOFError:
                            pass
                        self.frames = cycle(frames)

                        try:
                            self.delay = im.info['duration']
                        except:
                            self.delay = 100

                        if len(frames) == 1:
                            self.config(image=next(self.frames))
                        else:
                            self.next_frame()

                    def unload(self):
                        self.config(image=None)
                        self.frames = None

                    def next_frame(self):
                        if self.frames:
                            self.config(image=next(self.frames))
                            self.after(self.delay, self.next_frame)
                #############################################################################################################################


                class Quiz:
                    def __init__(self):
                        self.title_label = Label(gui, text='Trivia Masters',
                                                fg="cyan", bg="#212325")
                        self.title_label.config(font=('calibri 80 italic bold'))
                        self.title_label.place(relx=0.03, rely=0.05)
                        self.info_label = Label(
                            gui, text="Press Continue to Start the Quiz:", bg="#212325")
                        self.info_label.config(font=('calibri 69 italic bold'))
                        self.info_label.place(relx=0.03, rely=0.25)

                        self.info_label1 = Label(gui, text="1. There are a total of 5 questions.\n2. The quiz is in the form of a MCQ\
                        \n3. There is no negative marking.\n 4. The quiz is based on current affairs.\n\n\n\n\
                        Press continue to start the quiz now.", fg="white", bg="#212325", justify=LEFT)
                        self.info_label1.config(font=('calibri 60 italic bold'))
                        self.info_label1.place(relx=0.03, rely=0.25)
                        self.lbl = ImageLabel(gui)
                        self.lbl.pack()
                        self.lbl.load('brainisback.png')
                        self.lbl.place(relx=0.7, rely=0.3)

                    ###
                    ###
                        self.buttons(place_next=False)
                        self.entr = self.entry_button()
                    ###

                    def add_label(self, display_text, x, y):
                        label = Label(gui, text=display_text, width=20,
                                    font=('ariel', 12, 'bold'), anchor='w')
                        label.place(x=x, y=y)
                        return label

                    def start(self):
                        self.title_label.destroy()
                        self.info_label.destroy()
                        self.info_label1.destroy()
                        self.lbl.destroy()
                        self.info_label
                        self.entr.destroy()
                        self.q_no = 0
                        self.img = None
                        self.display_image()
                        self.display_title()
                        self.display_question()
                        self.back_button()
                        self.opt_selected = IntVar()
                        self.opts = self.radio_buttons()
                        self.display_options()
                        self.next, self.quit = self.buttons()
                        self.data_size = len(question)
                        self.correct = 0

                    def show_msg(self, msg):
                        mb.showinfo(msg)

                    def display_result(self):

                        wrong_count = self.data_size - self.correct
                        sum = 0
                        for value in result_ans.values():
                            sum += value
                        wrong_count = self.data_size-sum
                        correct = f"{sum}"
                        wrong = f"{wrong_count}"
                        score = int(sum / self.data_size * 100)
                        result = f"Score: {score}%"
                        # mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")
                        gui.destroy()
                        app = customtkinter.CTk()
                        app.overrideredirect(True)
                        app.geometry(
                            "{0}x{1}+0+0".format(app.winfo_screenwidth(), app.winfo_screenheight()))

                        app.title("Result")
                        
                        #Name
                        name_label = tkinter.Label(
                            master=app, text="Congratulations", justify=tkinter.LEFT)
                        name_label.config(font=('calibri 55 italic bold'),
                                       fg="white", bg="#222325")
                        name_label.place(relx=0.05, rely=0.10)
                        
                        name_name = tkinter.Label(
                            master=app, text=b, justify=tkinter.LEFT)
                        name_name.config(font=('calibri 55 italic bold'),
                                          fg="white", bg="#222325")
                        name_name.place(relx=0.226, rely=0.10)


                        
                        # Correct
                        c_label = tkinter.Label(
                            master=app, text="Number of correct answers is", justify=tkinter.LEFT)
                        c_label.config(font=('calibri 55 italic bold'),
                                    fg="white", bg="#222325")
                        c_label.place(relx=0.05, rely=0.30)

                        c_label1 = tkinter.Label(
                            master=app, text=correct, justify=tkinter.RIGHT)
                        c_label1.config(font=('calibri 55 italic bold'),
                                        bg="#222325", fg="white")
                        c_label1.place(relx=0.365, rely=0.30)
                        #

                        # Wrong
                        w_label = tkinter.Label(
                            master=app, text="Number of wrong answers is", justify=tkinter.LEFT)
                        w_label.config(font=('calibri 55 italic bold'),
                                    bg="#222325", fg="white")
                        w_label.place(relx=0.05, rely=0.40)

                        w_label1 = tkinter.Label(
                            master=app, text=wrong, justify=tkinter.RIGHT)
                        w_label1.config(font=('calibri 55 italic bold'),
                                        bg="#222325", fg="white")
                        w_label1.place(relx=0.365, rely=0.40)
                        #

                        # Score
                        s_label = tkinter.Label(
                            master=app, text="Your total score is", justify=tkinter.LEFT)
                        s_label.config(font=('calibri 55 italic bold'),
                                    bg="#222325", fg="white")
                        s_label.place(relx=0.05, rely=0.50)

                        s_label1 = tkinter.Label(
                            master=app, text=score, justify=tkinter.RIGHT)
                        s_label1.config(font=('calibri 55 italic bold'),
                                        bg="#222325", fg="white")
                        s_label1.place(relx=0.248, rely=0.50)
                        #

                        image = Image.open('thankyou.jpg')
                        imgre = image.resize((800, 800))

                        img1 = ImageTk.PhotoImage(imgre)

                        img = customtkinter.CTkLabel(
                            app, image=img1, fg='black', bg='black')
                        img.place(relx=0.6, rely=0.24)

                        quit_button = customtkinter.CTkButton(
                            text="Quit", master=app, corner_radius=15, command=app.destroy)

                        quit_button.place(relx=0.1, rely=0.95, anchor=tkinter.CENTER)

                        app.mainloop()

                    def check_ans(self, q_no):
                        user_choice[q_no] = self.opt_selected.get()
                        if self.opt_selected.get() == answer[q_no]:
                            return True

                    def next_btn(self):

                        if self.q_no == len(question)-2:
                            self.next['text'] = 'Submit'

                        if self.check_ans(self.q_no):
                            self.correct += 1
                            result_ans[self.q_no] = 1
                        else:
                            result_ans[self.q_no] = 0
                        self.q_no += 1
                        if self.q_no == self.data_size:
                            self.display_result()

                        else:
                            self.display_question()
                            self.display_image()
                            self.display_options()

                    def add_textbox(self, x, y, placeholder="text"):
                        textbox = Entry(text=placeholder)
                        textbox.place(x=x, y=y)
                        return textbox

                    def buttons(self, place_next=True):
                        next_button = None
                        if place_next:
                            next_button = customtkinter.CTkButton(
                                text="Next", master=gui, corner_radius=15, command=self.next_btn)

                            next_button.place(relx=0.9, rely=0.95, anchor=tkinter.CENTER)

                        quit_button = customtkinter.CTkButton(
                            text="Quit", master=gui, corner_radius=15, command=gui.destroy)

                        quit_button.place(relx=0.1, rely=0.95, anchor=tkinter.CENTER)
                        return next_button, quit_button

                    def back_button(self):
                        back_btn = customtkinter.CTkButton(
                            text="Back", master=gui, corner_radius=15, command=self.go_back)
                        back_btn.place(relx=0.7, rely=0.95, anchor=tkinter.CENTER)

                    def go_back(self):
                        if self.q_no == 0:
                            return
                        self.q_no -= 1
                        self.display_question()
                        self.display_image()
                        self.display_options()

                    def entry_button(self):
                        entry_button = customtkinter.CTkButton(
                            text="Continue", master=gui, command=self.start, corner_radius=15)
                        entry_button.place(relx=0.9, rely=0.95, anchor=tkinter.CENTER)
                        return entry_button

                    def display_options(self):
                        val = 0

                        self.opt_selected.set(0)
                        for option in options[self.q_no]:
                            self.opts[val]['text'] = option
                            val += 1
                        for count in range(1, 5):
                            if user_choice[self.q_no] == count:
                                self.opt_selected.set(count)

                    def display_question(self):

                        q_no = Label(gui, text=question[self.q_no], width=100,
                                    font=('ariel', 40, 'bold'), fg='white', anchor='w', bg="#222325")

                        q_no.place(x=10, y=100)

                    def display_image(self):
                        url = imgs[self.q_no]

                        u = r.get(url)
                        raw_data = u._content
                        u.close()

                        im = Image.open(BytesIO(raw_data))
                        size = (800, 800)
                        im = im.resize(size)
                        image = ImageTk.PhotoImage(im)
                        self.img = image
                        img = Label(image=image, height=800, width=800)
                        img.place(x=1900, y=300)

                    def display_title(self):

                        # The title to be shown
                        title = Label(gui, text="Trivia Masters",
                                    width=90, bg="#0f0f61", fg="#64b9cc", font=("ariel", 40, "bold", ITALIC))

                        # place of the title
                        title.place(x=0, y=2)

                    def radio_buttons(self):

                        q_list = []

                        # position of the first option
                        y_pos = 400

                        # adding the options to the list
                        while len(q_list) < 4:
                            radio_btn = tkinter.Radiobutton(gui, text=" ", variable=self.opt_selected,
                                                            value=len(q_list)+1, font=("ariel", 40, 'bold'), fg='#b3bdb9', bg="#222325")

                            # adding the button to the list
                            q_list.append(radio_btn)

                            # placing the button
                            radio_btn.place(x=75, y=y_pos)

                            # incrementing the y-axis position by 40
                            y_pos += 150

                        # return the radio buttons
                        return q_list


                gui = customtkinter.CTk()
                # gui.geometry("800x600")
                # gui.attributes('-fullscreen', True)
                # gui.state('zoomed')
                gui.overrideredirect(True)
                gui.geometry("{0}x{1}+0+0".format(gui.winfo_screenwidth(),
                            gui.winfo_screenheight()))

                gui.title("PhotoEvaluate Quiz")


                with open('questions.csv', newline='') as f:
                    reader = csv.reader(f)
                    data = list(reader)
                options = []
                no_of_ques = 6  # no of total questions in quiz + 1
                for i in range(1, no_of_ques):
                    opt = data[i][3:7]
                    options.append(opt)

                data = read_csv("questions.csv", encoding="ISO-8859-1")

                question = data['question'].tolist()
                answer = data['answer'].tolist()
                imgs = data['imgs'].tolist()

                result_ans = {}
                user_choice = {item: 0 for item in range(len(question))}

                quiz = Quiz()

                gui.mainloop()

                ### 
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
    heading.config(font=('calibri 100 italic bold'))
    heading.place(relx=0.1, rely=0.15)
    
    # Image 
    image = Image.open('signup.png')
    imgre = image.resize((600, 600))
    img1 = ImageTk.PhotoImage(imgre)

    img = customtkinter.CTkLabel(
        sup, image=img1, fg='black', bg='black')
    img.place(relx=0.6, rely=0.3)
    
    #full name
    flabel = customtkinter.CTkLabel(
        sup, text="Full Name", fg='white', bg='black')
    flabel.place(relx=0.15, rely=0.4)
    fname1 = customtkinter.CTkEntry(sup, bg='black', fg='black',
                                   textvariable=fname)
    fname1.place(relx=0.28, rely=0.4)
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
