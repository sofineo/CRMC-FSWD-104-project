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

#photo = PhotoImage(file='cctb.png')

label_test = tk.Label(window,
                       text='Enter Your CCTB number :',
                        fg = 'black', bg = '#AED2A6',
                        font =('Arial', 30, 'bold'),
                        bd = 10,
                        relief = RAISED,
                        padx = 20,
                        pady = 20,
                        #image = photo,
                        #compound ='bottom'
                        )
label_test.pack()
#label_test.place(x= 0, y = 0)
window.mainloop()

