import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import csv
import pandas as pd

#CSV file 
def read_csv_to_dict_of_dicts(file_path):
    result_dict = {}

    with open(file_path, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)

        # Assuming the first row contains headers
        headers = next(csv_reader)

        for row in csv_reader:
            # Use the value in the first column as the key
            key = row[0]

            # Create a dictionary for the current row using the headers as keys
            row_dict = {headers[i]: row[i] for i in range(1, len(headers))}

            # Add the row dictionary to the result dictionary using the key
            result_dict[key] = row_dict

    return result_dict

# Provide the path to your CSV file
file_path = 'test.csv'

# Call the function to read the CSV file and create the dictionary of dictionaries
result = read_csv_to_dict_of_dicts(file_path)

# Print the result
print(result)

cctb_number = ""
        
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
            # startpage, scheadule respectively with 
            # for loop
            self.frames[F] = frame 
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage, cctb_number)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont, cctb_number):
        frame = self.frames[cont]
        frame.tkraise()

    
class StartPage(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)

        #Functions

        def clear():
            label_name.config(text = "")
            label_course.config(text = "")

        def delete():
            entry_cctb_number.delete(0, END)

        def validate_number():
            label_error_message.config(text="")
            label_name.config(text = "")
            label_course.config(text = "")
            confirm_btn.grid_forget()
            try:
                int(entry_cctb_number.get())
                search_for_cctb_number()

            except ValueError:
                label_error_message.config(text="Please type only numbers!")


        def search_for_cctb_number():
            self.cctb_number = int(entry_cctb_number.get())
            show_name_and_course(cctb_number)


        def show_name_and_course(cctb_number):
            try:
              key = f'{self.cctb_number}'
              row_select = result[key]
              name = row_select['name']
              course = row_select['course']
              label_name.config(text = f"{name}")
              label_course.config(text = f"{course}")  
              confirm_btn.grid(row = 6, columnspan = 2, pady = 10)
            except ValueError:
              label_error_message.config(text="There is no such cctb number!")


        # label of frame Layout HomePage
        label_cctb_number = tk.Label(self, text="Enter student's CCTB number", pady = 10)
        entry_cctb_number = tk.Entry(self)
        delete_btn = tk.Button(self, text ="Delete",
                               command = delete)
        search_btn = tk.Button(self, text="Search", command = validate_number)
        label_name = tk.Label(self, text = "")
        label_course = tk.Label(self, text = "")
        label_error_message = tk.Label(self, text = "", font='Helvetica 10 bold', foreground = "red")

        confirm_btn = tk.Button(self, text = "Show scheadule",
                                command = lambda : 
                                [clear(), 
                                 controller.show_frame(Scheadule, self.cctb_number), 
                                 confirm_btn.grid_forget(),
                                 delete()]) 
        # putting the grid in its place by using
        # grid
        label_cctb_number.grid(row = 0, column = 0, columnspan = 2, pady = 10)
        entry_cctb_number.grid(row = 1, column = 0, columnspan = 2, pady = 10)
        delete_btn.grid(row = 2, column = 0, pady = 10)
        search_btn.grid(row = 2, column = 1, pady = 10)
        label_name.grid(row = 4, column = 0, columnspan = 2)
        label_course.grid(row = 5, column = 0, columnspan = 2)
        label_error_message.grid(row = 3, column = 0, columnspan = 2)

# second window frame page1 
class Scheadule(tk.Frame):

    def __init__(self, parent, controller):

      tk.Frame.__init__(self, parent)

      #key = f'{cctb_number}'
      #row_select = result[key]
      #name = row_select['name']
      #course = row_select['course']

      # label of frame Layout Scheadule
      label = tk.Label(self, text ="Scheadule", font = 'Helvetica 15 bold')
      label_name = tk.Label(self, text = f"{cctb_number}")
      label_course = tk.Label(self, text = f"course")
      new_btn = tk.Button(self, text ="Search a new scheadule",
                            command = lambda : controller.show_frame(StartPage))


      label_hours = tk.Label(self, text = "Hours")
      label_monday = tk.Label(self, text = "Monday")
      label_tuesday = tk.Label(self, text = "Tuesday")
      label_wednesday = tk.Label(self, text = "Wednesday")
      label_thursday = tk.Label(self, text = "Thursday")
      label_friday = tk.Label(self, text = "Friday")
      label_saturday = tk.Label(self, text = "Saturday")
      label_sunday = tk.Label(self, text = "Sunday")     

      #Hourly labels
      label_07am_08am = tk.Label(self, text = "07 am - 08 am")
      label_08am_09am = tk.Label(self, text = "08 am - 09 am")
      label_09am_10am = tk.Label(self, text = "09 am - 10 am")
      label_10am_11am = tk.Label(self, text = "10 am - 11 am")
      label_11am_12pm = tk.Label(self, text = "11 am - 12 am")
      label_12pm_01pm = tk.Label(self, text = "12 pm - 01 pm")
      label_01pm_02pm = tk.Label(self, text = "01 pm - 02 pm")
      label_02pm_03pm = tk.Label(self, text = "02 pm - 03 pm")
      label_03pm_04pm = tk.Label(self, text = "03 pm - 04 pm")
      label_04pm_05pm = tk.Label(self, text = "04 pm - 05 pm")
      label_05pm_06pm = tk.Label(self, text = "05 pm - 06 pm")
      label_06pm_07pm = tk.Label(self, text = "06 pm - 07 pm")
      label_07pm_08pm = tk.Label(self, text = "07 pm - 08 pm")
      label_08pm_09pm = tk.Label(self, text = "08 pm - 09 pm")
      label_09pm_10pm = tk.Label(self, text = "09 pm - 10 pm")

       
      # putting the button in its place 
      # by using grid
      label.grid(row = 0, columnspan = 7)
      label_name.grid(row = 1, columnspan = 7)
      label_course.grid(row = 2, columnspan = 7)
      label_hours.grid(row = 3, column = 0)
      label_monday.grid(row = 3, column = 1)
      label_tuesday.grid(row = 3, column = 2)
      label_wednesday.grid(row = 3, column = 3)
      label_thursday.grid(row = 3, column = 4)
      label_friday.grid(row = 3, column = 5)
      label_saturday.grid(row = 3, column = 6)
      label_sunday.grid(row = 3, column = 7)
      label_07am_08am.grid(row = 4, column = 0)
      label_08am_09am.grid(row = 5, column = 0)
      label_09am_10am.grid(row = 6, column = 0)
      label_10am_11am.grid(row = 7, column = 0)
      label_11am_12pm.grid(row = 8, column = 0)
      label_12pm_01pm.grid(row = 9, column = 0)
      label_01pm_02pm.grid(row = 10, column = 0)
      label_02pm_03pm.grid(row = 11, column = 0)
      label_03pm_04pm.grid(row = 12, column = 0)
      label_04pm_05pm.grid(row = 13, column = 0)
      label_05pm_06pm.grid(row = 14, column = 0)
      label_06pm_07pm.grid(row = 15, column = 0)
      label_07pm_08pm.grid(row = 16, column = 0)
      label_08pm_09pm.grid(row = 17, column = 0)
      label_09pm_10pm.grid(row = 18, column = 0)
      new_btn.grid(row = 19, columnspan = 7, padx = 10, pady = 10)

      print(f"print: {cctb_number}") 

# Driver Code
app = tkinterApp()
app.title("CCTB")
app.geometry('200x300')
app.mainloop()








