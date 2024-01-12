import tkinter as tk

#Functions

def search_for_cctb_number():
    cctb_number = entry_cctb_number.get()

window = tk.Tk()
window.title('CCTB Scheadule')
label_cctb_number = tk.Label(window, text="Enter student's CCTB number")
entry_cctb_number = tk.Entry(window)
search_button = tk.Button(window, text="Search", command=search_for_cctb_number)

#Containers packing
label_cctb_number.pack()
entry_cctb_number.pack()
search_button.pack()

window.mainloop()
