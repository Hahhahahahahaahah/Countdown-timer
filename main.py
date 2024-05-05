import tkinter as tk
from tkinter import Tk , StringVar , Entry , Button , messagebox 
import time
#Countdown 
def countdowntimer():
    try:
        user_input = int(Hour.get()) * 3600 + int(Minute.get()) * 60 + int(Second.get())
    except:
        messagebox.showwarning("Error", "Invalid Input")
        return
    while user_input > -1:
        mins, secs = divmod(user_input , 60)
        hours = 0
        if mins > 60:
            hours, mins = divmod(mins , 60)
        Hour.set("{0:2d}".format(hours))
        Minute.set("{0:2d}".format(mins))
        Second.set("{0:2d}".format(secs))
        root.update()
        time.sleep(1)
    
        if user_input == 0:
            messagebox.showinfo("Time Countdown", "Time Over")
            
        user_input -= 1

#Setup
root = Tk()
root.geometry("400x300")
root.title("Countdown Timer")
root.config(background = "#345")

#Time
Hour = StringVar()
Minute = StringVar()
Second =StringVar()
Hour.set("00")
Minute.set("00")
Second.set("00")
#Title
root.title("Cowndown Timer")
#Entry 1 
Hour_Box = Entry(root, width = 3 , font = ("Arial", 18, "") ,textvariable = Hour)
#Entry 2
Min_Box = Entry(root, width = 3 , font = ("Arial", 18, "") ,textvariable = Minute)
#Entry 3
Second_Box = Entry(root, width = 3 , font = ("Arial", 18, "") ,textvariable = Second)
#Placing 1
Hour_Box.place(x = 80, y = 20)
Min_Box.place(x = 130 , y =20)
Second_Box.place (x = 180 , y = 20)
#Button
btn = Button(root , text = "Start Countdown" , command = countdowntimer)
btn.place(x = 80, y = 120)
root.mainloop()