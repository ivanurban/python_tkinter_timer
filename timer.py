#!/usr/bin/python3


import time
import tkinter as tk




def timer(time_to_sleep, title, text_message):

    root=tk.Tk()

    time.sleep(time_to_sleep)

    root.title(title)

    label= tk.Label(root, text=text_message)
    label.pack(side="top", fill="both", expand="True", padx=20, pady=20)

    button = tk.Button(root, text="OK", command=lambda: root.destroy())
    button.pack(side="bottom", fill="none", expand="True")

    
    #keep the popup above all other opened windows
    root.wm_attributes("-topmost", 1)

    root.mainloop()


    
#Call function, pass the time and text that you want
timer(2700, "Pause", "TIME TO MAKE PAUSE")

timer(900, "Work", "BACK TO WORK")
