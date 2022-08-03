#!/usr/bin/python


from logging import exception

from tkinter import *
import tkinter as tk
from tkinter import END, ttk;
from tkinter import Text
from tkinter.messagebox import showerror
from bs4 import BeautifulSoup
from more_itertools import side_effect
from numpy import pad
import requests
from tkinter.ttk import Label
import pandas as pd
from sqlalchemy import column

def search_url():
    listbox_result.delete(0,END)
    keyword = text_keyword.get("1.0",END)
    keyword = keyword.strip()
    url_error = []
    for i in range(0,listbox.size()):
        url = listbox.get(i)
        url = url.strip()
        try:
            r = requests.get(url)
        
            data = r.text
            soup = BeautifulSoup(data,"html.parser")
            html_text = soup.get_text()
        except:
            url_error.append(url)
        
        if(html_text.lower().find(keyword.lower()) > 0):
            listbox_result.insert(END,url)
    listbox_result.insert(END,"Search ended")
    if(len(url_error) > 0):
        error_msg = "Following websites can not be opend : \n"
        for item in url_error:
            error_msg += item + "\n"
        showerror("Error occured while opening website",error_msg)    
        

def refresh_url():
    text_keyword.delete("1.0",END)
    listbox.delete(0,END)
    listbox_result.delete(0,END)    

def return_pressed(event):
    url = text.get("1.0",END)
    text.delete("1.0",END)
    text.index("insert")
    listbox.insert(END,url)

root = tk.Tk()
root.title("Search websites with keywords")
root.columnconfigure(0, weight=2)
root.rowconfigure(0, weight=7)


label = Label(root, text='Insert Websites here')
label.grid(row=0,column=0,columnspan=2,padx=(10,10))
text = Text(root, height=1)
text.grid(row=1,column=0,columnspan=2 ,padx=(10,10),pady=(5))
text.bind('<Return>', return_pressed)

listbox = tk.Listbox(
    root,
    width=100,
    height=10,
    selectmode='extended')
sb = Scrollbar(
    root,
    orient=VERTICAL,
    )

sb.grid(row=2,column=2,sticky=NS)
listbox.config(yscrollcommand=sb.set)
sb.config(command=listbox.yview)
listbox.grid(row=2,column=0,columnspan=2,padx=(10,10),pady=(5))
text_keyword = Text(root, height=1)
text_keyword.grid(row=3,column=0,columnspan=2,padx=(10,10),pady=(5))

btn = ttk.Button(root, text='Search',command = search_url)
btn.grid(row=4,column=0,columnspan=1,padx=(200,20),pady=(5))
#btn.place(relx=0.25,anchor='c')
btn_refresh = ttk.Button(root, text='Refresh',command = refresh_url)
btn_refresh.grid(row=4,column=1,columnspan=1,padx=(20,200),pady=(5))
#btn_refresh.place(relx=0.75,anchor='c')

label = Label(root, text='Result')
label.grid(row=5,column=0,columnspan=2,padx=(10,10),pady=(5))


listbox_result = tk.Listbox(
    root,
    width=100,
    height=10,
    selectmode='extended')
sb_result = Scrollbar(
    root,
    orient=VERTICAL,
    )
sb_result.grid(row=6,column=2, sticky=NS)
listbox_result.config(yscrollcommand=sb_result.set)
sb_result.config(command=listbox_result.yview)
listbox_result.grid(row=6,column=0,columnspan=2,padx=(10,10),pady=(5))
root.mainloop()
# Code to add widgets will go here...
