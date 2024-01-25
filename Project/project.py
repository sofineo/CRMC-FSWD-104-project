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
name = ""
course = ""

#FUNCTIONS
def close_root():
    root.destroy()

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
        global cctb_number
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
        global name
        name = row_select['name']
        global course
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

#---------------
#FUNCTIONS FOR MOUSE EVENT
def on_click(event):
    label_monday_07am.config(text='IST04-Class01')
def on_leave(event):
    label_monday_07am.config(text='')
#--------------

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
    label_hours.place_forget()
    label_monday.place_forget()
    label_tuesday.place_forget()
    label_wednesday.place_forget()
    label_thursday.place_forget()
    label_friday.place_forget()
    #label_saturday.grid_forget()
    #label_sunday.grid_forget()
    label_07am_08am.place_forget()
    label_08am_09am.place_forget()
    label_09am_10am.place_forget()
    label_10am_11am.place_forget()
    label_11am_12pm.place_forget()
    label_12pm_01pm.place_forget()
    label_01pm_02pm.place_forget()
    label_02pm_03pm.place_forget()
    label_03pm_04pm.place_forget()
    label_04pm_05pm.place_forget()
    label_05pm_06pm.place_forget()
    label_06pm_07pm.place_forget()
    label_07pm_08pm.place_forget()
    label_08pm_09pm.place_forget()
    label_09pm_10pm.place_forget()
    new_btn.place_forget()
    label_schedule.place_forget()
    label_name_schedule.place_forget()
    label_course_schedule.place_forget()

    #forgeting Monday labels
    label_monday_07am.place_forget() 
    label_monday_08am.place_forget()
    label_monday_09am.place_forget()  
    label_monday_10am.place_forget()
    label_monday_11am.place_forget()    
    label_monday_12pm.place_forget()   
    label_monday_01pm.place_forget()    
    label_monday_02pm.place_forget()
    label_monday_03pm.place_forget()   
    label_monday_04pm.place_forget()   
    label_monday_05pm.place_forget()    
    label_monday_06pm.place_forget()
    label_monday_07pm.place_forget()
    label_monday_08pm.place_forget()
    label_monday_09pm.place_forget()

    #forgeting Tuesday labels
    label_tuesday_07am.place_forget()  
    label_tuesday_08am.place_forget()  
    label_tuesday_09am.place_forget()  
    label_tuesday_10am.place_forget()
    label_tuesday_11am.place_forget()  
    label_tuesday_12pm.place_forget() 
    label_tuesday_01pm.place_forget() 
    label_tuesday_02pm.place_forget()
    label_tuesday_03pm.place_forget()  
    label_tuesday_04pm.place_forget()
    label_tuesday_05pm.place_forget()
    label_tuesday_06pm.place_forget()
    label_tuesday_07pm.place_forget()
    label_tuesday_08pm.place_forget()
    label_tuesday_09pm.place_forget()

    #forgeting Wednesday labels
    label_wednesday_07am.place_forget()
    label_wednesday_08am.place_forget()
    label_wednesday_09am.place_forget()
    label_wednesday_10am.place_forget()
    label_wednesday_11am.place_forget() 
    label_wednesday_12pm.place_forget()
    label_wednesday_01pm.place_forget()
    label_wednesday_02pm.place_forget()
    label_wednesday_03pm.place_forget()
    label_wednesday_04pm.place_forget()
    label_wednesday_05pm.place_forget()
    label_wednesday_06pm.place_forget()
    label_wednesday_07pm.place_forget()
    label_wednesday_08pm.place_forget()  
    label_wednesday_09pm.place_forget()

    #forgeting Thursday labels
    label_thursday_07am.place_forget()
    label_thursday_08am.place_forget() 
    label_thursday_09am.place_forget() 
    label_thursday_10am.place_forget()
    label_thursday_11am.place_forget() 
    label_thursday_12pm.place_forget()
    label_thursday_01pm.place_forget()
    label_thursday_02pm.place_forget()
    label_thursday_03pm.place_forget()
    label_thursday_04pm.place_forget()
    label_thursday_05pm.place_forget()
    label_thursday_06pm.place_forget()
    label_thursday_07pm.place_forget() 
    label_thursday_08pm.place_forget()  
    label_thursday_09pm.place_forget()

    #forgeting Friday labels
    label_friday_07am.place_forget()
    label_friday_08am.place_forget()
    label_friday_09am.place_forget() 
    label_friday_10am.place_forget()
    label_friday_11am.place_forget()
    label_friday_12pm.place_forget()
    label_friday_01pm.place_forget()
    label_friday_02pm.place_forget()
    label_friday_03pm.place_forget()
    label_friday_04pm.place_forget()
    label_friday_05pm.place_forget()
    label_friday_06pm.place_forget()
    label_friday_07pm.place_forget()
    label_friday_08pm.place_forget()
    label_friday_09pm.place_forget()
    
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

    label_name_schedule.config(text = name)
    label_course_schedule.config(text = course)
                              
    # putting the button in its place 
    # by using grid
    label_schedule.place(anchor = CENTER, relx = .5, rely = .1)
    label_name_schedule.place(anchor = CENTER, relx = .5, rely = .15)
    label_course_schedule.place(anchor = CENTER, relx = .5, rely = .2)
    label_hours.place(anchor = CENTER, relx = .2, rely = .245)
    label_monday.place(anchor = CENTER, relx = .3, rely = .245)
    label_tuesday.place(anchor = CENTER, relx = .4, rely = .245)
    label_wednesday.place(anchor = CENTER, relx = .5, rely = .245)
    label_thursday.place(anchor = CENTER, relx = .6, rely = .245)
    label_friday.place(anchor = CENTER, relx = .7, rely = .245)
    #label_saturday.grid(row = 3, column = 6)
    #label_sunday.grid(row = 3, column = 7)
    label_07am_08am.place(anchor = CENTER, relx = .2, rely = .275)
    label_08am_09am.place(anchor = CENTER, relx = .2, rely = .305)
    label_09am_10am.place(anchor = CENTER, relx = .2, rely = .335)
    label_10am_11am.place(anchor = CENTER, relx = .2, rely = .365)
    label_11am_12pm.place(anchor = CENTER, relx = .2, rely = .395)
    label_12pm_01pm.place(anchor = CENTER, relx = .2, rely = .425)
    label_01pm_02pm.place(anchor = CENTER, relx = .2, rely = .455)
    label_02pm_03pm.place(anchor = CENTER, relx = .2, rely = .485)
    label_03pm_04pm.place(anchor = CENTER, relx = .2, rely = .515)
    label_04pm_05pm.place(anchor = CENTER, relx = .2, rely = .545)
    label_05pm_06pm.place(anchor = CENTER, relx = .2, rely = .575)
    label_06pm_07pm.place(anchor = CENTER, relx = .2, rely = .605)
    label_07pm_08pm.place(anchor = CENTER, relx = .2, rely = .635)
    label_08pm_09pm.place(anchor = CENTER, relx = .2, rely = .665)
    label_09pm_10pm.place(anchor = CENTER, relx = .2, rely = .695)
    new_btn.place(anchor = CENTER, relx = .5, rely = .8)


    #grid for Monday
    label_monday_07am.place(anchor = CENTER, relx = .3, rely = .275)  
    label_monday_08am.place(anchor = CENTER, relx = .3, rely = .305)  
    label_monday_09am.place(anchor = CENTER, relx = .3, rely = .335)     
    label_monday_10am.place(anchor = CENTER, relx = .3, rely = .365)  
    label_monday_11am.place(anchor = CENTER, relx = .3, rely = .395)  
    label_monday_12pm.place(anchor = CENTER, relx = .3, rely = .425)  
    label_monday_01pm.place(anchor = CENTER, relx = .3, rely = .455)  
    label_monday_02pm.place(anchor = CENTER, relx = .3, rely = .485)  
    label_monday_03pm.place(anchor = CENTER, relx = .3, rely = .515)  
    label_monday_04pm.place(anchor = CENTER, relx = .3, rely = .545)  
    label_monday_05pm.place(anchor = CENTER, relx = .3, rely = .575)  
    label_monday_06pm.place(anchor = CENTER, relx = .3, rely = .605)  
    label_monday_07pm.place(anchor = CENTER, relx = .3, rely = .635)  
    label_monday_08pm.place(anchor = CENTER, relx = .3, rely = .665)  
    label_monday_09pm.place(anchor = CENTER, relx = .3, rely = .695)  

    #grid for Tuesday
    label_tuesday_07am.place(anchor = CENTER, relx = .4, rely = .275) 
    label_tuesday_08am.place(anchor = CENTER, relx = .4, rely = .305) 
    label_tuesday_09am.place(anchor = CENTER, relx = .4, rely = .335) 
    label_tuesday_10am.place(anchor = CENTER, relx = .4, rely = .365)  
    label_tuesday_11am.place(anchor = CENTER, relx = .4, rely = .395)   
    label_tuesday_12pm.place(anchor = CENTER, relx = .4, rely = .425)  
    label_tuesday_01pm.place(anchor = CENTER, relx = .4, rely = .455) 
    label_tuesday_02pm.place(anchor = CENTER, relx = .4, rely = .485) 
    label_tuesday_03pm.place(anchor = CENTER, relx = .4, rely = .515) 
    label_tuesday_04pm.place(anchor = CENTER, relx = .4, rely = .545)  
    label_tuesday_05pm.place(anchor = CENTER, relx = .4, rely = .575)     
    label_tuesday_06pm.place(anchor = CENTER, relx = .4, rely = .605) 
    label_tuesday_07pm.place(anchor = CENTER, relx = .4, rely = .635) 
    label_tuesday_08pm.place(anchor = CENTER, relx = .4, rely = .665) 
    label_tuesday_09pm.place(anchor = CENTER, relx = .4, rely = .695) 

    #grid for Wednesday
    label_wednesday_07am.place(anchor = CENTER, relx = .5, rely = .275) 
    label_wednesday_08am.place(anchor = CENTER, relx = .5, rely = .305)  
    label_wednesday_09am.place(anchor = CENTER, relx = .5, rely = .335) 
    label_wednesday_10am.place(anchor = CENTER, relx = .5, rely = .365) 
    label_wednesday_11am.place(anchor = CENTER, relx = .5, rely = .395) 
    label_wednesday_12pm.place(anchor = CENTER, relx = .5, rely = .425) 
    label_wednesday_01pm.place(anchor = CENTER, relx = .5, rely = .455)     
    label_wednesday_02pm.place(anchor = CENTER, relx = .5, rely = .485)  
    label_wednesday_03pm.place(anchor = CENTER, relx = .5, rely = .515) 
    label_wednesday_04pm.place(anchor = CENTER, relx = .5, rely = .545) 
    label_wednesday_05pm.place(anchor = CENTER, relx = .5, rely = .575) 
    label_wednesday_06pm.place(anchor = CENTER, relx = .5, rely = .605) 
    label_wednesday_07pm.place(anchor = CENTER, relx = .5, rely = .635)   
    label_wednesday_08pm.place(anchor = CENTER, relx = .5, rely = .665)    
    label_wednesday_09pm.place(anchor = CENTER, relx = .5, rely = .695) 

    #grid for Thursday
    label_thursday_07am.place(anchor = CENTER, relx = .6, rely = .275)
    label_thursday_08am.place(anchor = CENTER, relx = .6, rely = .305)
    label_thursday_09am.place(anchor = CENTER, relx = .6, rely = .335)
    label_thursday_10am.place(anchor = CENTER, relx = .6, rely = .365)
    label_thursday_11am.place(anchor = CENTER, relx = .6, rely = .395)
    label_thursday_12pm.place(anchor = CENTER, relx = .6, rely = .425)
    label_thursday_01pm.place(anchor = CENTER, relx = .6, rely = .455)
    label_thursday_02pm.place(anchor = CENTER, relx = .6, rely = .485)
    label_thursday_03pm.place(anchor = CENTER, relx = .6, rely = .515)
    label_thursday_04pm.place(anchor = CENTER, relx = .6, rely = .545)
    label_thursday_05pm.place(anchor = CENTER, relx = .6, rely = .575)
    label_thursday_06pm.place(anchor = CENTER, relx = .6, rely = .605)
    label_thursday_07pm.place(anchor = CENTER, relx = .6, rely = .635)
    label_thursday_08pm.place(anchor = CENTER, relx = .6, rely = .665)
    label_thursday_09pm.place(anchor = CENTER, relx = .6, rely = .695)
    #grid for Friday
    label_friday_07am.place(anchor = CENTER, relx = .7, rely = .275)    
    label_friday_08am.place(anchor = CENTER, relx = .7, rely = .305) 
    label_friday_09am.place(anchor = CENTER, relx = .7, rely = .335)
    label_friday_10am.place(anchor = CENTER, relx = .7, rely = .365)
    label_friday_11am.place(anchor = CENTER, relx = .7, rely = .395) 
    label_friday_12pm.place(anchor = CENTER, relx = .7, rely = .425) 
    label_friday_01pm.place(anchor = CENTER, relx = .7, rely = .455)
    label_friday_02pm.place(anchor = CENTER, relx = .7, rely = .485)
    label_friday_03pm.place(anchor = CENTER, relx = .7, rely = .515)
    label_friday_04pm.place(anchor = CENTER, relx = .7, rely = .545)   
    label_friday_05pm.place(anchor = CENTER, relx = .7, rely = .575)  
    label_friday_06pm.place(anchor = CENTER, relx = .7, rely = .605)
    label_friday_07pm.place(anchor = CENTER, relx = .7, rely = .635)
    label_friday_08pm.place(anchor = CENTER, relx = .7, rely = .665)
    label_friday_09pm.place(anchor = CENTER, relx = .7, rely = .695)
    
# label of frame Layout Scheadule
label_schedule = tk.Label(root, text ="Schedule", font = 'Helvetica 20 bold')
label_name_schedule = tk.Label(root, text = "", font='Helvetica 15 bold', fg = "#4A2559")
label_course_schedule = tk.Label(root, text = "", font='Helvetica 15 bold', fg = "#4A2559")
new_btn = tk.Button(root, text ="Search a new scheadule",
                            command = recreate_home)
        
label_hours = tk.Label(root, text = "Hours", bg = "#4A2559", fg = "white",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)
label_monday = tk.Label(root, text = "Monday \t", bg = "#4A2559", fg = "white",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)
label_tuesday = tk.Label(root, text = "Tuesday \t", bg = "#4A2559", fg = "white", 
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)
label_wednesday = tk.Label(root, text = "Wednesday \t", bg = "#4A2559", fg = "white",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)
label_thursday = tk.Label(root, text = "Thursday \t", bg = "#4A2559", fg = "white",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)
label_friday = tk.Label(root, text = "Friday \t", bg = "#4A2559", fg = "white", 
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)
#label_saturday = tk.Label(root, text = "Saturday \t",
#    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)
#label_sunday = tk.Label(root, text = "Sunday \t", 
#    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)     
         

        
#Hourly labels
label_07am_08am = tk.Label(root, text = "07 am - 08 am", bg = "#4A2559", fg = "white",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)
label_08am_09am = tk.Label(root, text = "08 am - 09 am", bg = "#4A2559", fg = "white",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)
label_09am_10am = tk.Label(root, text = "09 am - 10 am", bg = "#4A2559", fg = "white",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)  
label_10am_11am = tk.Label(root, text = "10 am - 11 am", bg = "#4A2559", fg = "white",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)
label_11am_12pm = tk.Label(root, text = "11 am - 12 am", bg = "#4A2559", fg = "white",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)
label_12pm_01pm = tk.Label(root, text = "12 pm - 01 pm", bg = "#4A2559", fg = "white",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)
label_01pm_02pm = tk.Label(root, text = "01 pm - 02 pm", bg = "#4A2559", fg = "white",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)
label_02pm_03pm = tk.Label(root, text = "02 pm - 03 pm", bg = "#4A2559", fg = "white",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)
label_03pm_04pm = tk.Label(root, text = "03 pm - 04 pm", bg = "#4A2559", fg = "white",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)
label_04pm_05pm = tk.Label(root, text = "04 pm - 05 pm", bg = "#4A2559", fg = "white",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)
label_05pm_06pm = tk.Label(root, text = "05 pm - 06 pm", bg = "#4A2559", fg = "white",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)
label_06pm_07pm = tk.Label(root, text = "06 pm - 07 pm", bg = "#4A2559", fg = "white",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)
label_07pm_08pm = tk.Label(root, text = "07 pm - 08 pm", bg = "#4A2559", fg = "white",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)
label_08pm_09pm = tk.Label(root, text = "08 pm - 09 pm", bg = "#4A2559", fg = "white",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)
label_09pm_10pm = tk.Label(root, text = "09 pm - 10 pm", bg = "#4A2559", fg = "white",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17)

#Monday labels
label_monday_07am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_monday_08am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_monday_09am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_monday_10am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_monday_11am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_monday_12pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_monday_01pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_monday_02pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_monday_03pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_monday_04pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_monday_05pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_monday_06pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_monday_07pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_monday_08pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_monday_09pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")   


#Tuesday labels
label_tuesday_07am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_tuesday_08am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_tuesday_09am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_tuesday_10am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_tuesday_11am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_tuesday_12pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_tuesday_01pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_tuesday_02pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_tuesday_03pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_tuesday_04pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_tuesday_05pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_tuesday_06pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_tuesday_07pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_tuesday_08pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_tuesday_09pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")  

#Wednesday labels
label_wednesday_07am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_wednesday_08am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_wednesday_09am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_wednesday_10am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_wednesday_11am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_wednesday_12pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_wednesday_01pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_wednesday_02pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_wednesday_03pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_wednesday_04pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_wednesday_05pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_wednesday_06pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_wednesday_07pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_wednesday_08pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_wednesday_09pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white") 

#Thursday labels
label_thursday_07am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_thursday_08am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_thursday_09am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_thursday_10am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_thursday_11am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_thursday_12pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_thursday_01pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_thursday_02pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_thursday_03pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_thursday_04pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_thursday_05pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_thursday_06pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_thursday_07pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_thursday_08pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_thursday_09pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")   

#Friday labels
label_friday_07am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_friday_08am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_friday_09am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_friday_10am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_friday_11am = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_friday_12pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_friday_01pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_friday_02pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_friday_03pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_friday_04pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_friday_05pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_friday_06pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_friday_07pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")
label_friday_08pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "lightgrey", fg = "white")
label_friday_09pm = tk.Label(root, text = "--",
    font=('Arial', 11), borderwidth=1, relief=RAISED,padx=10, pady=5, width=17, bg = "white")  

#--------------
#labels mouse click events
label_monday_07am.bind('<Button-1>', on_click)
label_monday_07am.bind('<Leave>', on_leave)
#--------------

        
# label of frame Layout HomePage
label_home_page = tk.Label(root, text = "Welcome to Schedule APP!", font="Helvetica 20 bold")
label_cctb_number = tk.Label(root, text="Enter student's CCTB number", pady = 10)
entry_cctb_number = tk.Entry(root)
delete_btn = tk.Button(root, text ="Delete",
                               command = delete)
search_btn = tk.Button(root, text="Search", command = validate_number)
label_name = tk.Label(root, text = "", font='Helvetica 15 bold', fg = "#4A2559")
label_course = tk.Label(root, text = "", font='Helvetica 15 bold', fg = "#4A2559")
label_error_message = tk.Label(root, text = "", font='Helvetica 15 bold', foreground = "red")
confirm_btn = tk.Button(root, text = "Show scheadule",
                                command = create_schedule_table)

# putting the grid in its place by using grid in HomePage
label_home_page.place(anchor = CENTER, relx = .5, rely = .2)
label_cctb_number.place(anchor = CENTER, relx = .5, rely = .25)
entry_cctb_number.place(anchor = CENTER, relx = .5, rely = .3)
delete_btn.place(anchor = CENTER, relx = .47, rely = .35)
search_btn.place(anchor = CENTER, relx = .53, rely = .35)
label_error_message.place(anchor = CENTER, relx = .5, rely = .4)
label_name.place(anchor = CENTER, relx = .5, rely = .45)
label_course.place(anchor = CENTER, relx = .5, rely = .5)

btn_exit = tk.Button(root, text = "CLOSE APP", command = close_root,
     font='Helvetica 10 bold', fg = "red")
btn_exit.place(anchor = CENTER, relx = 0.9, rely = 0.1)

#PLACEHOLDER 
entry_cctb_number.insert(0, 'CT:')
entry_cctb_number.config(state='disabled')
        
x_focus_in = entry_cctb_number.bind('<Button-1>', 
    lambda x: on_focus_in(entry_cctb_number))
x_focus_out = entry_cctb_number.bind('<FocusOut>', 
    lambda x: on_focus_out(entry_cctb_number, 'CT:'))
        
                                

root.mainloop()
