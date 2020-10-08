import tkinter as tk
from tkinter import ttk
import threading, time, os, subprocess

root= tk.Tk()
root.title("Nhap timesheet nhe'")
canvas1 = tk.Canvas(root, width = 350, height = 250) 
canvas1.pack()

# Run command in batch file
def start_batch_1():
    cwd = os.getcwd()
    subprocess.call([r'{}\\WindowVersionBat.bat'.format(cwd)])

def start_batch_2():
    cwd = os.getcwd()
    subprocess.call([r'{}\\IpconfigBat.bat'.format(cwd)])

# Threading function start_batch
def callback_threaded_1():
    threading.Thread(target=start_batch_1).start()
def callback_threaded_2():
    threading.Thread(target=start_batch_2).start()
           
button1 = tk.Button (root, text='Run The Bat file 1',command=callback_threaded_1)
button2 = tk.Button (root, text='Run The Bat file 2',command=callback_threaded_2)
canvas1.create_window(170, 130, window=button1)
canvas1.create_window(170, 160, window=button2)

root.mainloop()