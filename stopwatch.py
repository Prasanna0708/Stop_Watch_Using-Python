#import tkinter with alias name is tk
import tkinter as tk
#creating a Tkinter class
root = tk.Tk()
#creating a label
stopwatch = tk.Label(root,text = "Test",font = 'arial 100')
#packing the stopwatch label
stopwatch.pack()

#creating a global variable --->minutes and seconds initially value with 0

minutes = 0
seconds = 0

#defining a function with the name of stopwatch

def change_stopwatch():
    global minutes
    global seconds

    #using conditions
    if seconds < 59:
        seconds += 1
    elif seconds == 59:
        seconds = 0
        minutes += 1

    time_text = "{:02d}: {:2d}".format(minutes,seconds)
    stopwatch.config(text = time_text)
    root.after(1000,change_stopwatch)

change_stopwatch()


#closing the main loop
root.mainloop()