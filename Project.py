import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import csv


#CSV file 
with open('test.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))

#Class
class tkinterApp(tk.Tk):
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)  
        container.pack(side = "top", fill = "both", expand = True) 
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

          
        # initializing frames to an empty array
        self.frames = {}  

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Scheadule):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, pscheadule respectively with 
            # for loop
            self.frames[F] = frame 
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
         
        # label of frame Layout HomePage
        label_cctb_number = tk.Label(window, text="Enter student's CCTB number", pady = 10)
        entry_cctb_number = tk.Entry(window)
        delete_btn = tk.Button(window, text ="Delete", command = delete)
        search_btn = tk.Button(window, text="Search", command=search_for_cctb_number)
         
        # putting the grid in its place by using
        # grid
        #label.grid(row = 0, column = 4, padx = 10, pady = 10) 
        label_cctb_number.grid(row = 0, columnspan = 2)
        entry_cctb_number.grid(row = 1, columnspan = 2)
        delete_btn.grid(row = 2, column = 0)
        search_btn.grid(row = 2, column = 1)
  
        button1 = ttk.Button(self, text ="Page 1",
        command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Page 2",
        command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

#Functions
#def search_for_cctb_number():
#    cctb_number = entry_cctb_number.get()
#    show_name_and_course()

#def delete():
#    entry_cctb_number.delete(0, END)

#def show_name_and_course():
#    label_name = tk.Label(window, text = f"Name")
#    label_course = tk.Label(window, text = f"Course")
#    confirm_btn = tk.Button(window, text = "Show scheadule")
#    confirm_btn.grid(row = 6, column = 2)
#    label_name.grid(row = 4, columnspan = 2)
#    label_course.grid(row = 5, columnspan = 2)
    
    
#window = tk.Tk()
#window.geometry('420x420')
#window.title('CCTB Scheadule')
#label_cctb_number = tk.Label(window, text="Enter student's CCTB number", pady = 10)
#entry_cctb_number = tk.Entry(window)
#delete_btn = tk.Button(window, text ="Delete", command = delete)
#search_btn = tk.Button(window, text="Search", command=search_for_cctb_number)



#Containers grid
#label_cctb_number.grid(row = 1, columnspan = 2)
#entry_cctb_number.grid(row = 2, columnspan = 2)
#delete_btn.grid(row = 3, column = 0)
#search_btn.grid(row = 3, column = 1)


# Driver Code
window = tkinterApp()
window.mainloop()
#window.mainloop()




