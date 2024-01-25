
#def y(event):
#    print('Scroll-Wheel')
#def q(event):
#    print('Right-Click')
#
#def Enter(event):
#    #Label(window, text='You entered the window').pack()
#    print('You entered the window')
#
#def Leave(event):
#    print('You left the page')
#
#def ConstCord(event):
#    print(str(event.x)+','+str(event.y))
#
#def Hold(event):
#    print('Your mouse was at '+str(event.x)+','+str(event.y))
#
#window.bind('<Button-1>', x)
#window.bind('<Button-2>', y)
#window.bind('<Button-3>', q)
#window.bind("<Enter>", Enter)
#window.bind('<Leave>', Leave)
##window.bind('<Motion>', ConstCord)
#window.bind('<ButtonRelease>', Hold)
#window.mainloop()
import tkinter as tk

def on_motion(event):
    label.config(text=f"Mouse coordinates: ({event.x}, {event.y})")

# Create the main window
root = tk.Tk()
root.title("Mouse Motion Example")

# Create a label widget
label = tk.Label(root, text="Move the mouse over this label", font=("Helvetica", 14))
label.pack(padx=20, pady=20)

# Bind motion event to label
label.bind("<Motion>", on_motion)

# Start the main loop
root.mainloop()