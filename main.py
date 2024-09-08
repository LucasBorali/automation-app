from tkinter import *
from tkinter import ttk
import pyautogui
import time
import threading
from command_thread import Command_thread

actions_list = []

def define_new_action():
    entry = ttk.Entry(frm)
    entry.grid(column=1,row=1)
    
    def confirm_action():
        action_name = entry.get()
        new_action = Command_thread(action_name)
        actions_list.append(new_action)
        
    ttk.Button(frm,text='Criar', command=confirm_action).grid(column=2,row=2)
    # actions_list.append(new_action)

def find_coordinates(label):
    for i in range(5,0,-1):
        label.config(text=f'{i} seconds left! Go to the position!')
        time.sleep(1)
    currentMouseX, currentMouseY = pyautogui.position()
    label.config(text=f'Coordinates: {currentMouseX}, {currentMouseY}')

def start_find_coordinates(label):
    threading.Thread(target=find_coordinates, args=(label,)).start()


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
coordinate_label = ttk.Label(frm, text=f'5 seconds left!Go to the position!')
coordinate_label.grid(column=1, row=0)
# ttk.Button(frm, text='Find coordinates', command=lambda: start_find_coordinates(coordinate_label)).grid(column=0, row=0)
ttk.Button(frm, text='Criar nova sequência de comandos', command=define_new_action).grid(column=0, row=0)





root.mainloop()