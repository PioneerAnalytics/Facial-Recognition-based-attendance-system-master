#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 14:54:11 2019

@author: manmeet
"""


def fun():
    text1.delete(0,END)
    text.delete(0,END)
from tkinter import *
window = Tk()
window.title("Student Login")
window.configure(background='black')
label=Label(window, text="Roll_Number", font=("Times New Roman",20),bg="black",fg='white')
label1=Label(window, text="password", font=("Times New Roman",20),bg="black",fg='white')
label1.grid(column=0, row=2,padx=10,pady=10)
text1=Entry(window, width=20,show='*',bg='white')
text1.grid(column=1, row=2)

btn=Button(window, text="Submit",font=("Arial",15),bg='white')
btn1=Button(window, text="Reset",font=("Arial",15),bg='white',command=fun)
text=Entry(window, width=20,bg='white')
text.grid(column=1, row=0,padx=10,pady=10)
text.focus()
btn.grid(column=3, row=5)
btn1.grid(column=1, row=5)

label.grid(column=0, row=0)

window.geometry('400x200')
window.mainloop()