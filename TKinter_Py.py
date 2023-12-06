import time
import tkinter as tk
from tkinter import Button, Label, Entry
import time
from threading import Thread
from pygame import mixer
number = 0

class Microwave():
    global song
    '''a microwave button layout used to emulate real world microwave functionality'''
    def __init__(self):
        global number
        #Window setup attributes
        self.root = tk.Tk()
        self.root.geometry("500x700+860+30")
        self.root.title("Microwave")
        self.root.config(bg="black")
        self.g_number = number
        mixer.init()

        mixer.music.load("C:\\Users\\zebdu\\Downloads\\Microwave Touch Key Tone Beep - QuickSounds.com.mp3")

        #Widget setups
        self.screen = Label(self.root, bg="black", font=("DS-Digital Bold", 50), fg="green", width=10)
        self.button_1 = Button(self.root, text="1", font=("Helvetica", 15), bg="grey", fg="black",width=5, height=3,  command= lambda: self.number_press(num=1))
        self.button_2 = Button(self.root, text="2", font=("Helvetica", 15), bg="grey", fg="black", width=5, height=3,  command= lambda: self.number_press(num=2))
        self.button_3 = Button(self.root, text="3", font=("Helvetica", 15), bg="grey", fg="black", width=5, height=3,  command= lambda: self.number_press(num=3))
        self.button_4 = Button(self.root, text="4", font=("Helvetica", 15), bg="grey", fg="black",width=5, height=3,  command= lambda: self.number_press(num=4))
        self.button_5 = Button(self.root, text="5", font=("Helvetica", 15), bg="grey", fg="black", width=5, height=3,  command= lambda: self.number_press(num=5))
        self.button_6 = Button(self.root, text="6", font=("Helvetica", 15), bg="grey", fg="black", width=5, height=3,  command= lambda: self.number_press(num=6))
        self.button_7 = Button(self.root, text="7", font=("Helvetica", 15), bg="grey", fg="black",width=5, height=3,  command= lambda: self.number_press(num=7))
        self.button_8 = Button(self.root, text="8", font=("Helvetica", 15), bg="grey", fg="black", width=5, height=3, command= lambda: self.number_press(num=8))
        self.button_9 = Button(self.root, text="9", font=("Helvetica", 15), bg="grey", fg="black", width=5, height=3,  command= lambda: self.number_press(num=9))
        self.button_more = Button(self.root, text="less-", font=("Helvetica", 15), bg="grey", fg="black", width=5, height=3)
        self.button_0 = Button(self.root, text="0", font=("Helvetica", 15), bg="grey", fg="black", width=5, height=3, command= lambda: self.number_press(num=0))
        self.button_less = Button(self.root, text="more+", font=("Helvetica", 15), bg="grey", fg="black", width=5, height=3, )
        self.button_clear = Button(self.root, text="CLR", font=("Helvetica", 15), bg="grey", fg="red", width=5, height=3,command=self.clear_entry)
        self.button_start = Button(self.root, text="ENTER", font=("Helvetica", 15), bg="grey", fg="green", width=5, height=3, command=self.enter_button)

        #Widget placement
        self.screen.place(x=100, y=40)
        self.button_1.place(x=150, y=120)
        self.button_2.place(x=220, y=120)
        self.button_3.place(x=290, y=120)
        self.button_4.place(x=150, y=210)
        self.button_5.place(x=220, y=210)
        self.button_6.place(x=290, y=210)
        self.button_7.place(x=150, y=300)
        self.button_8.place(x=220, y=300)
        self.button_9.place(x=290, y=300)
        self.button_more.place(x=150, y=390)
        self.button_0.place(x=220, y=390)
        self.button_less.place(x=290, y=390)
        self.button_clear.place(x=360, y=390)
        self.button_start.place(x=360, y=300)

    def number_press(self, num):
        mixer.music.load("C:\\Users\\zebdu\\Downloads\\Microwave Touch Key Tone Beep - QuickSounds.com.mp3")
        mixer.music.play()
        old_value = self.screen.cget(("text"))
        self.screen.config(text=int(f"{old_value}{num}"))

    def clear_entry(self):
        mixer.music.load("C:\\Users\\zebdu\\Downloads\\Microwave Touch Key Tone Beep - QuickSounds.com.mp3")
        mixer.music.play()
        self.screen.config(text="")

    def timer(self):
        is_true = True
        self.g_number = int(self.screen.cget("text"))
        while is_true:
            if self.g_number > 0:
                print(self.g_number)
                time.sleep(1)
                self.g_number -= 1
                self.screen.config(text=self.g_number)
            else:
                mixer.music.load("C:\\Users\\zebdu\\PycharmProjects\\microwave\\Microwave Bing - QuickSounds.com.mp3")
                mixer.music.play()
                self.screen.config(text="DONE")
                time.sleep(2)
                self.screen.config(text="")
                is_true = False

    def enter_button(self):
        mixer.music.load("C:\\Users\\zebdu\\Downloads\\Microwave Touch Key Tone Beep - QuickSounds.com.mp3")
        mixer.music.play()
        time.sleep(.25)
        t1 = Thread(target=self.timer)
        t1.start()

    def mainloop(self):
        self.root.mainloop()
