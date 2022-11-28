### Ignore this file. Use mainlogreg.py ###

from tkinter import *
from turtle import width
import PIL
import tkinter.messagebox
from doctest import master
from email.mime import image
from gettext import install
from io import BytesIO
from multiprocessing.sharedctypes import Value
import tkinter as tk
from tkinter.font import ITALIC
from tracemalloc import start
from unittest import result
from cv2 import destroyAllWindows
from matplotlib.ft2font import BOLD
import requests as r
import pandas as pd
from re import A, I
from tkinter.messagebox import QUESTION
import numpy
from pandas import *
import csv
import customtkinter
# import required classes from tkinter
from tkinter import LEFT, IntVar,Button, Label, PhotoImage, Radiobutton, Tk, Entry
from PIL import Image, ImageTk
# and import messagebox as mb from tkinter
from tkinter import messagebox as mb
from itertools import count, cycle

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
        self.title_label = Label(gui, text="Instructions for the quiz",
                        fg="cyan", bg="#212325")
        self.title_label.config(font=('calibri 80 italic bold'))
        self.title_label.place(relx=0.03, rely=0.05)

        self.info_label=Label(gui, text="Press Continue to Start the Quiz:",bg="#212325")
        self.info_label.config(font=('calibri 69 italic bold'))
        self.info_label.place(relx=0.03, rely=0.25)

        self.info_label1 = Label(gui, text="1. There are a total of 10 questions.\n2. The quiz is in the form of a MCQ\
        \n3. There is no negative marking.\n 4. The quiz is based on current affairs.\n\n\n\n\
        Press continue to start the quiz now.", fg="white", bg="#212325", justify=LEFT)
        self.info_label1.config(font=('calibri 60 italic bold'))
        self.info_label1.place(relx=0.03, rely=0.25)


        self.lbl = ImageLabel(gui)
        self.lbl.pack()
        self.lbl.load('brainisback.png')
        self.lbl.place(relx=0.7,rely=0.3)


    ###
    ###
        self.buttons(place_next=False)
        self.entr = self.entry_button()
    ###

    def add_label(self, display_text,x,y):
        label= Label(gui, text=display_text, width=20,
        font=( 'ariel' ,12, 'bold' ), anchor= 'w' )
        label.place(x=x,y=y)
        return label

    def start(self):
        self.title_label.destroy()
        self.info_label.destroy()
        self.info_label1.destroy()
        self.lbl.destroy()
        self.info_label
        self.entr.destroy()
        self.q_no=0
        self.img = None
        self.display_image()
        self.display_title()
        self.display_question()
        self.back_button()
        self.opt_selected=IntVar()
        self.opts=self.radio_buttons()
        self.display_options()
        self.next,self.quit = self.buttons()
        self.data_size=len(question)
        self.correct=0


    def show_msg(self,msg):
        mb.showinfo(msg)

    def display_result(self):

        wrong_count = self.data_size - self.correct
        sum = 0
        for value in result_ans.values():
            sum+=value
        wrong_count = self.data_size-sum
        correct = f"{sum}"
        wrong = f"{wrong_count}"
        score = int(sum / self.data_size * 100)
        result = f"Score: {score}%"
        #mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")
        gui.destroy()
        app = customtkinter.CTk()
        app.overrideredirect(True)
        app.geometry("{0}x{1}+0+0".format(app.winfo_screenwidth(), app.winfo_screenheight()))

        app.title("Result")

        #Correct
        c_label = tkinter.Label(
            master=app, text="Number of correct answers is", justify=tkinter.LEFT)
        c_label.config(font=('calibri 55 italic bold'), fg="white", bg="#222325")
        c_label.place(relx=0.05, rely=0.30)

        c_label1 = tkinter.Label(
            master=app, text=correct, justify=tkinter.RIGHT)
        c_label1.config(font=('calibri 55 italic bold'),
                        bg="#222325", fg="white")
        c_label1.place(relx=0.365, rely=0.30)
        #

        #Wrong
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

        #Score
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
            self.next['text']='Submit'

        if self.check_ans(self.q_no):
            self.correct += 1
            result_ans[self.q_no]=1
        else:
            result_ans[self.q_no]=0
        self.q_no += 1
        if self.q_no==self.data_size:
            self.display_result()


        else:
            self.display_question()
            self.display_image()
            self.display_options()


    def add_textbox(self,x,y,placeholder="text"):
        textbox = Entry(text=placeholder)
        textbox.place(x=x,y=y)
        return textbox


    def buttons(self,place_next=True):
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
        if self.q_no==0:
            return
        self.q_no-=1
        self.display_question()
        self.display_image()
        self.display_options()


    def entry_button(self):
        entry_button = customtkinter.CTkButton(
            text="Continue", master=gui, command=self.start, corner_radius=15)
        entry_button.place(relx=0.9, rely=0.95, anchor=tkinter.CENTER)
        return entry_button


    def display_options(self):
        val=0


        self.opt_selected.set(0)
        for option in options[self.q_no]:
            self.opts[val]['text']=option
            val+=1
        for count in range(1,5):
            if user_choice[self.q_no] == count:
                self.opt_selected.set(count)



    def display_question(self):

        q_no = Label(gui, text=question[self.q_no], width=100,
        font=( 'ariel' ,40, 'bold' ),fg='white', anchor= 'w',bg="#222325" )

        q_no.place(x=10, y=100)

    def display_image(self):
        url = imgs[self.q_no]

        u = r.get(url)
        raw_data = u._content
        u.close()

        im = Image.open(BytesIO(raw_data))
        size = (800,800)
        im = im.resize(size)
        image = ImageTk.PhotoImage(im)
        self.img = image
        img = Label(image=image,height=800,width=800)
        img.place(x=1900,y=300)


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
            radio_btn = tkinter.Radiobutton(gui,text=" ",variable=self.opt_selected,
                                    value=len(q_list)+1, font=("ariel", 40,'bold'), fg='grey', bg="#222325")


            # adding the button to the list
            q_list.append(radio_btn)

            # placing the button
            radio_btn.place(x = 75, y = y_pos)

            # incrementing the y-axis position by 40
            y_pos += 150

        # return the radio buttons
        return q_list


gui = customtkinter.CTk()
#gui.geometry("800x600")
#gui.attributes('-fullscreen', True)
#gui.state('zoomed')
gui.overrideredirect(True)
gui.geometry("{0}x{1}+0+0".format(gui.winfo_screenwidth(), gui.winfo_screenheight()))

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

result_ans={}
user_choice = {item:0 for item in range(len(question))}

quiz = Quiz()

gui.mainloop()

