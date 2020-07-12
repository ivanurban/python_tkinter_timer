#!/usr/bin/python3


import time
import tkinter as tk
import sys




def timer(time_to_sleep, title, text_message):

    root=tk.Tk()

    time.sleep(time_to_sleep)

    root.title(title)

    label= tk.Label(root, text=text_message)
    label.pack(side="top", fill="both", expand="True", padx=20, pady=20)

    button = tk.Button(root, text="OK", command=lambda: root.destroy())
    button.pack(side="left", fill="none", expand="True")
    
    button = tk.Button(root, text="Stop", command=lambda: sys.exit())
    button.pack(side="right", fill="none", expand="True")

    
    #keep the popup above all other opened windows
    root.wm_attributes("-topmost", 1)

    root.mainloop()


while True:
    #Call function, pass the time and text that you want
    timer(2700, "Pause", "TIME TO MAKE PAUSE")

    timer(900, "Work", "BACK TO WORK")
