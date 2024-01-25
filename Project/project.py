import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import csv
import pandas as pd

#CSV file 
def read_csv_to_dict_of_dicts(file_path):
    result_dict = {}

    with open(file_path,'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')

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
file_path = 'test2.csv'

# Call the function to read the CSV file and create the dictionary of dictionaries
result = read_csv_to_dict_of_dicts(file_path)

#Creating the window
root = tk.Tk()
root.title("Schedule App")
#Seeting window to fullscreen
root.attributes('-fullscreen', True)

# Configure columns and rows to expand equally

cctb_number = "CCTB Number"

#FUNCTIONS
def clear():
    label_name.config(text = "")
    label_course.config(text = "")

def delete():
    entry_cctb_number.delete(0, END)

def validate_number():
    label_error_message.config(text="")
    clear()
    confirm_btn.grid_forget()
    number = entry_cctb_number.get()
    try:
        int(number)
        search_for_cctb_number()
        cctb_number = number

    except ValueError:
        label_error_message.config(text="Please type only numbers!")


def search_for_cctb_number():
    cctb_number = int(entry_cctb_number.get())
    show_name_and_course(cctb_number)


def show_name_and_course(cctb_number):
    try:
        key = f'{cctb_number}'
        row_select = result[key]
        name = row_select['name']
        course = row_select['course']
        label_name.config(text = f"{name}")
        label_course.config(text = f"{course}")  
        #confirm_btn.grid(row = 7, columnspan = 2, pady = 10)
        confirm_btn.place(anchor = CENTER, relx = .5, rely = .55)
    except ValueError:
        label_error_message.config(text="There is no such cctb number!")

#PLACEHOLDER FUNCTIONS
def on_focus_in(entry):
    if entry.cget('state') == 'disabled':
        entry.configure(state='normal')
        entry.delete(0, 'end')
        
def on_focus_out(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.configure(state='disabled')

def recreate_home():
    label_home_page.place(anchor = CENTER, relx = .5, rely = .2)
    label_cctb_number.place(anchor = CENTER, relx = .5, rely = .25)
    entry_cctb_number.place(anchor = CENTER, relx = .5, rely = .3)
    delete_btn.place(anchor = CENTER, relx = .47, rely = .35)
    search_btn.place(anchor = CENTER, relx = .53, rely = .35)
    label_error_message.place(anchor = CENTER, relx = .5, rely = .4)
    label_name.place(anchor = CENTER, relx = .5, rely = .45)
    label_course.place(anchor = CENTER, relx = .5, rely = .5)
    delete()
    

    #Using grid_forget to hide widgets from the Schedule page
    label_hours.grid_forget()
    label_monday.grid_forget()
    label_tuesday.grid_forget()
    label_wednesday.grid_forget()
    label_thursday.grid_forget()
    label_friday.grid_forget()
    label_saturday.grid_forget()
    label_sunday.grid_forget()
    label_07am_08am.grid_forget()
    label_08am_09am.grid_forget()
    label_09am_10am.grid_forget()
    label_10am_11am.grid_forget()
    label_11am_12pm.grid_forget()
    label_12pm_01pm.grid_forget()
    label_01pm_02pm.grid_forget()
    label_02pm_03pm.grid_forget()
    label_03pm_04pm.grid_forget()
    label_04pm_05pm.grid_forget()
    label_05pm_06pm.grid_forget()
    label_06pm_07pm.grid_forget()
    label_07pm_08pm.grid_forget()
    label_08pm_09pm.grid_forget()
    label_09pm_10pm.grid_forget()
    new_btn.grid_forget()
    label_schedule.grid_forget()
    label_name_schedule.grid_forget()
    label_course_schedule.grid_forget()

    #forgeting Monday labels
    label_monday_07am.grid_forget()    
    label_monday_08am.grid_forget()   
    label_monday_09am.grid_forget()    
    label_monday_10am.grid_forget() 
    label_monday_11am.grid_forget()    
    label_monday_12pm.grid_forget()   
    label_monday_01pm.grid_forget()    
    label_monday_02pm.grid_forget() 
    label_monday_03pm.grid_forget()   
    label_monday_04pm.grid_forget()   
    label_monday_05pm.grid_forget()    
    label_monday_06pm.grid_forget()
    label_monday_07pm.grid_forget()
    label_monday_08pm.grid_forget()
    label_monday_09pm.grid_forget()

    #forgeting Tuesday labels
    label_tuesday_07am.grid_forget()  
    label_tuesday_08am.grid_forget()  
    label_tuesday_09am.grid_forget()  
    label_tuesday_10am.grid_forget()
    label_tuesday_11am.grid_forget()  
    label_tuesday_12pm.grid_forget() 
    label_tuesday_01pm.grid_forget()  
    label_tuesday_02pm.grid_forget()
    label_tuesday_03pm.grid_forget()   
    label_tuesday_04pm.grid_forget()  
    label_tuesday_05pm.grid_forget() 
    label_tuesday_06pm.grid_forget() 
    label_tuesday_07pm.grid_forget()   
    label_tuesday_08pm.grid_forget()   
    label_tuesday_09pm.grid_forget()

    #forgeting Wednesday labels
    label_wednesday_07am.grid_forget()  
    label_wednesday_08am.grid_forget()  
    label_wednesday_09am.grid_forget()  
    label_wednesday_10am.grid_forget()
    label_wednesday_11am.grid_forget()  
    label_wednesday_12pm.grid_forget() 
    label_wednesday_01pm.grid_forget()  
    label_wednesday_02pm.grid_forget()
    label_wednesday_03pm.grid_forget()   
    label_wednesday_04pm.grid_forget()  
    label_wednesday_05pm.grid_forget() 
    label_wednesday_06pm.grid_forget() 
    label_wednesday_07pm.grid_forget()   
    label_wednesday_08pm.grid_forget()   
    label_wednesday_09pm.grid_forget()

def create_schedule_table():

    #Using grid_forget to hide the labels from the Home Page
    label_home_page.place_forget()
    label_cctb_number.place_forget()
    entry_cctb_number.place_forget()
    delete_btn.place_forget()
    search_btn.place_forget()
    label_error_message.place_forget()
    confirm_btn.place_forget()
    clear()
        
                              
    # putting the button in its place 
    # by using grid
    label_schedule.grid(row = 0, columnspan = 7)
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
    label_name_schedule.grid(row = 1, columnspan = 7)
    label_course_schedule.grid(row = 2, columnspan = 7)

    #grid for Monday
    label_monday_07am.grid(row = 4, column = 1)    
    label_monday_08am.grid(row = 5, column = 1)   
    label_monday_09am.grid(row = 6, column = 1)    
    label_monday_10am.grid(row = 7, column = 1) 
    label_monday_11am.grid(row = 8, column = 1)    
    label_monday_12pm.grid(row = 9, column = 1)   
    label_monday_01pm.grid(row = 10, column = 1)    
    label_monday_02pm.grid(row = 11, column = 1) 
    label_monday_03pm.grid(row = 12, column = 1)    
    label_monday_04pm.grid(row = 13, column = 1)   
    label_monday_05pm.grid(row = 14, column = 1)    
    label_monday_06pm.grid(row = 15, column = 1) 
    label_monday_07pm.grid(row = 16, column = 1)    
    label_monday_08pm.grid(row = 17, column = 1)   
    label_monday_09pm.grid(row = 18, column = 1)    

    #grid for Tuesday
    label_tuesday_07am.grid(row = 4, column = 2)    
    label_tuesday_08am.grid(row = 5, column = 2)   
    label_tuesday_09am.grid(row = 6, column = 2)    
    label_tuesday_10am.grid(row = 7, column = 2) 
    label_tuesday_11am.grid(row = 8, column = 2)    
    label_tuesday_12pm.grid(row = 9, column = 2)   
    label_tuesday_01pm.grid(row = 10, column = 2)    
    label_tuesday_02pm.grid(row = 11, column = 2) 
    label_tuesday_03pm.grid(row = 12, column = 2)    
    label_tuesday_04pm.grid(row = 13, column = 2)   
    label_tuesday_05pm.grid(row = 14, column = 2)    
    label_tuesday_06pm.grid(row = 15, column = 2) 
    label_tuesday_07pm.grid(row = 16, column = 2)    
    label_tuesday_08pm.grid(row = 17, column = 2)   
    label_tuesday_09pm.grid(row = 18, column = 2)

    #grid for Wednesday
    label_wednesday_07am.grid(row = 4, column = 3)    
    label_wednesday_08am.grid(row = 5, column = 3)   
    label_wednesday_09am.grid(row = 6, column = 3)    
    label_wednesday_10am.grid(row = 7, column = 3) 
    label_wednesday_11am.grid(row = 8, column = 3)    
    label_wednesday_12pm.grid(row = 9, column = 3)   
    label_wednesday_01pm.grid(row = 10, column = 3)    
    label_wednesday_02pm.grid(row = 11, column = 3) 
    label_wednesday_03pm.grid(row = 12, column = 3)    
    label_wednesday_04pm.grid(row = 13, column = 3)   
    label_wednesday_05pm.grid(row = 14, column = 3)    
    label_wednesday_06pm.grid(row = 15, column = 3) 
    label_wednesday_07pm.grid(row = 16, column = 3)    
    label_wednesday_08pm.grid(row = 17, column = 3)   
    label_wednesday_09pm.grid(row = 18, column = 3)
    
# label of frame Layout Scheadule
label_schedule = tk.Label(root, text ="Schedule", font = 'Helvetica 15 bold')
label_name_schedule = tk.Label(root, text = f"{cctb_number}")
label_course_schedule = tk.Label(root, text = f"{cctb_number}")
new_btn = tk.Button(root, text ="Search a new scheadule",
                            command = recreate_home)
        
label_hours = tk.Label(root, text = "Hours",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)
label_monday = tk.Label(root, text = "Monday \t",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)
label_tuesday = tk.Label(root, text = "Tuesday \t", 
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)
label_wednesday = tk.Label(root, text = "Wednesday \t",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)
label_thursday = tk.Label(root, text = "Thursday \t",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)
label_friday = tk.Label(root, text = "Friday \t", 
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)
label_saturday = tk.Label(root, text = "Saturday \t",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)
label_sunday = tk.Label(root, text = "Sunday \t", 
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)     
         

        
#Hourly labels
label_07am_08am = tk.Label(root, text = "07 am - 08 am",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_08am_09am = tk.Label(root, text = "08 am - 09 am",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "black", fg = "white")
label_09am_10am = tk.Label(root, text = "09 am - 10 am",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")    
label_10am_11am = tk.Label(root, text = "10 am - 11 am",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "black", fg = "white")
label_11am_12pm = tk.Label(root, text = "11 am - 12 am",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_12pm_01pm = tk.Label(root, text = "12 pm - 01 pm",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "black", fg = "white")
label_01pm_02pm = tk.Label(root, text = "01 pm - 02 pm",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_02pm_03pm = tk.Label(root, text = "02 pm - 03 pm",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "black", fg = "white")
label_03pm_04pm = tk.Label(root, text = "03 pm - 04 pm",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_04pm_05pm = tk.Label(root, text = "04 pm - 05 pm",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "black", fg = "white")
label_05pm_06pm = tk.Label(root, text = "05 pm - 06 pm",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_06pm_07pm = tk.Label(root, text = "06 pm - 07 pm",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "black", fg = "white")
label_07pm_08pm = tk.Label(root, text = "07 pm - 08 pm",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_08pm_09pm = tk.Label(root, text = "08 pm - 09 pm",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "black", fg = "white")
label_09pm_10pm = tk.Label(root, text = "09 pm - 10 pm",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")

#Monday labels
label_monday_07am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_monday_08am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "black", fg = "white")
label_monday_09am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_monday_10am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "black", fg = "white")
label_monday_11am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_monday_12pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "black", fg = "white")
label_monday_01pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_monday_02pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "black", fg = "white")
label_monday_03pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_monday_04pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "black", fg = "white")
label_monday_05pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_monday_06pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "black", fg = "white")
label_monday_07pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_monday_08pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "black", fg = "white")
label_monday_09pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")   


#Tuesday labels
label_tuesday_07am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_tuesday_08am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "black", fg = "white")
label_tuesday_09am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_tuesday_10am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "black", fg = "white")
label_tuesday_11am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_tuesday_12pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "black", fg = "white")
label_tuesday_01pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_tuesday_02pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "black", fg = "white")
label_tuesday_03pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_tuesday_04pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "black", fg = "white")
label_tuesday_05pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_tuesday_06pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "black", fg = "white")
label_tuesday_07pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_tuesday_08pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "black", fg = "white")
label_tuesday_09pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")  

#Wednesday labels
label_wednesday_07am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_wednesday_08am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "black", fg = "white")
label_wednesday_09am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_wednesday_10am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "black", fg = "white")
label_wednesday_11am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_wednesday_12pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "black", fg = "white")
label_wednesday_01pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_wednesday_02pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "black", fg = "white")
label_wednesday_03pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_wednesday_04pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "black", fg = "white")
label_wednesday_05pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_wednesday_06pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "black", fg = "white")
label_wednesday_07pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_wednesday_08pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "black", fg = "white")
label_wednesday_09pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")  
        
# label of frame Layout HomePage
label_home_page = tk.Label(root, text = "Welcome to Schedule APP!", font="Helvetica 20 bold")
label_cctb_number = tk.Label(root, text="Enter student's CCTB number", pady = 10)
entry_cctb_number = tk.Entry(root)
delete_btn = tk.Button(root, text ="Delete",
                               command = delete)
search_btn = tk.Button(root, text="Search", command = validate_number)
label_name = tk.Label(root, text = "")
label_course = tk.Label(root, text = "")
label_error_message = tk.Label(root, text = "", font='Helvetica 15 bold', foreground = "red")
confirm_btn = tk.Button(root, text = "Show scheadule",
                                command = create_schedule_table)

# putting the grid in its place by using grid in HomePage
#label_home_page.grid(row = 0, column = 0, columnspan = 2, pady = 20)
label_home_page.place(anchor = CENTER, relx = .5, rely = .2)
#label_cctb_number.grid(row = 1, column = 0, columnspan = 2, pady = 10)
label_cctb_number.place(anchor = CENTER, relx = .5, rely = .25)
#entry_cctb_number.grid(row = 2, column = 0, columnspan = 2, pady = 10)
entry_cctb_number.place(anchor = CENTER, relx = .5, rely = .3)
#delete_btn.grid(row = 3, column = 0, pady = 10)
delete_btn.place(anchor = CENTER, relx = .47, rely = .35)
#search_btn.grid(row = 3, column = 1, pady = 10)
search_btn.place(anchor = CENTER, relx = .53, rely = .35)
#label_error_message.grid(row = 4, column = 0, columnspan = 2)
label_error_message.place(anchor = CENTER, relx = .5, rely = .4)
#label_name.grid(row = 5, column = 0, columnspan = 2)
label_name.place(anchor = CENTER, relx = .5, rely = .45)
#label_course.grid(row = 6, column = 0, columnspan = 2)
label_course.place(anchor = CENTER, relx = .5, rely = .5)

#PLACEHOLDER 
entry_cctb_number.insert(0, 'CT:')
entry_cctb_number.config(state='disabled')
        
x_focus_in = entry_cctb_number.bind('<Button-1>', 
    lambda x: on_focus_in(entry_cctb_number))
x_focus_out = entry_cctb_number.bind('<FocusOut>', 
    lambda x: on_focus_out(entry_cctb_number, 'CT:'))
        
                                

root.mainloop()
