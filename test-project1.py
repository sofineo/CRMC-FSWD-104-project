import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry('420x420')
window.title('IST04-Project')
#icon = PhotoImage(file='OIP.jpg')
#window.iconphoto(True, icon)
window.config(background='#EBEDE2')

icon = PhotoImage(file='cctb.png')
window.iconphoto(True, icon)
img1 = icon.subsample(4, 4)
#photo = PhotoImage(file='cctb.png')
count = 0
def submit():
    user_ct = entry_ct.get()
    print(f'Hello, {user_ct}')
    entry_ct.config(state =DISABLED)
def delete():
    entry_ct.delete(0, END)
def backspace():
    entry_ct.delete(len(entry_ct.get())-1, END)

def click():
    global count
    count +=1
    print(f'You clicked the button {count} times')

label_test = tk.Label(window,
                       text='Enter Your CCTB number :',
                        fg = 'black', bg = '#AED2A6',
                        font =('Arial', 30, 'bold'),
                        bd = 10,
                        relief = RAISED,
                        #padx = 20,
                       # pady = 20,
                        #image = photo,
                        #compound ='bottom'
                        )
#button = tk.Button(window, 
               # text= 'Search',
               # command= click,
               # font=('Comic Sans', 20),
               # fg= '#00FF00',
               # bg = 'black',
               # activeforeground='#00FF00',
               # activebackground='white',
               # state = ACTIVE,
               # image =icon,
               # compound = 'top',)
entry_ct = tk.Entry(window,
                    font=('Arial', 20),
                    fg='#00FF00',
                    bg = 'white',
                    )
entry_ct.insert(0, 'CT')
submit_btn = tk.Button(window, text ='Submit', command = submit)

delete_btn = tk.Button(window, text ='Delete', command = delete,)

backspace_btn = tk.Button(window, text ='Backspace', command = backspace,)

label_test.pack()
entry_ct.pack()
#button.pack()
delete_btn.pack(), backspace_btn.pack(), submit_btn.pack()
#label_test.place(x= 0, y = 0)
window.mainloop()

