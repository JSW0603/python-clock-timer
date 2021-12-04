#import modules
import time
import tkinter as tk

#making window
window = tk.Tk()

#function for timer
def update_time():
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_pm = time.strftime("%p")
    time_text = hours + ":" + minutes + ":" + seconds + ":" + am_pm
    digit_clock.config(text=time_text)
    digit_clock.after(1000, update_time)

#make timer box and layout
digit_clock = tk.Label(window, text="00:00:00", font="helvetica 72 bold")
digit_clock.pack()

#update timer on the window
update_time()

#loop for make window
window.mainloop()

