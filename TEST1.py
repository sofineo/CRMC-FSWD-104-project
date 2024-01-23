import tkinter as tk 
from tkinter import *
from tkinter import ttk
import csv
from tkinter.ttk import *
#CSV FILE
with open('test.csv', encoding='utf-8-sig',  newline='') as csvfile:
    csvData = csv.reader(csvfile) 
    headers = next(csvData)
    for row in csvData:
        data_dict = {}
        for i, value in enumerate(row):
            data_dict[headers[i]] = value 
        print(data_dict)
#Functions
def delete():
    entry_ct_number.delete(0, END)

def search():
    cctb_number = entry_ct_number.get()
#PLACEHOLDER
def on_focus_in(entry):
    if entry.cget('state') == 'disabled':
        entry.configure(state='normal')
        entry.delete(0, 'end')

def on_focus_out(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.configure(state='disabled')
#VALIDATION
def validation():  
    label_error_message.config(text='')
    try:
        int(entry_ct_number.get())
        
        print('IT WORKING')
    except ValueError:
        label_error_message.config(text='Please type only numbers!')
        entry_ct_number.delete(0, 'end')
#NEW WINDOW
def NewWindow():
    new_window = Toplevel()
    Label(new_window, text='Some text').pack()

#notebook =ttk.Notebook(window)
#
#tab1 = Frame(notebook)
#tab2 = Frame(notebook)
#
#notebook.add(tab1, text= 'Text on Top')
#notebook.pack()
#
#notebook.add(tab2, text= 'Text on 2nd Page')
#notebook.pack()
#Label(tab2, text = '?').pack()

window =tk.Tk()

label_ct_number = Label(window, text='Enter student\'t CCTB number')
label_ct_number.pack()

entry_ct_number = tk.Entry(window, )
entry_ct_number.pack(pady=10)
entry_ct_number.insert(0, 'CT:')
entry_ct_number.config(state='disabled')

x_focus_in = entry_ct_number.bind('<Button-1>', lambda x: on_focus_in(entry_ct_number))
x_focus_out = entry_ct_number.bind('<FocusOut>', lambda x: on_focus_out(entry_ct_number, 'CT:'))

button_delete = Button(window, text='Delete',command=delete)
button_delete.pack()

button_search = Button(window, text='Search',command = validation)
button_search.pack()

label_error_message = tk.Label(window, text='')
label_error_message.pack()
window.mainloop()