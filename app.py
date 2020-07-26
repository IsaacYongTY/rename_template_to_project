# -*- coding: utf-8 -*-

import os, shutil
import tkinter as tk
from tkinter import filedialog, Text

input_path = ''

if os.path.isfile('save.txt'):

    with open('save.txt','r') as f:
        input_path = f.read()
        input_path = input_path.strip()
       
print(input_path)

def selectDirectory():
    file_path = filedialog.askdirectory(initialdir='./')
    print(file_path)

    for widget in directory_frame.winfo_children():
        widget.destroy()

    label = tk.Label(directory_frame, text=file_path, wraplength = 600, justify="center", bg="gray")
    label.pack()
    global input_path 
    input_path= file_path


def startProcess():
    print(input_path)
    song_title = song_title_frame.get("1.0","end")
    song_title = song_title.strip()

   
    template_path = input_path
    template_string = 'TEMPLATE'

    destination_path = f'{input_path}/../{song_title}'

    shutil.copytree(template_path, destination_path)
    print(destination_path)
    for folderName, subfolders, filenames in os.walk(destination_path):

        print(f'The current folder is {folderName}')
        
        for subfolder in subfolders:
            print(f'SUBFOLDER of {folderName}: {subfolder}') 

        for filename in filenames:
            print(f'FILE INSIDE {folderName}: {filename}')

            if(template_string in filename):
                print(template_string)
                new_filename = filename.replace(template_string, song_title)
                print(f'{folderName}/{filename}')
                os.rename(f'{folderName}/{filename}', f'{folderName}/{new_filename}')
                print('Renamed successfully')



root = tk.Tk()

canvas = tk.Canvas(root, height = 500, width = 600, bg = '#07c2cc')
canvas.pack()


directory_frame = tk.Text(root)
directory_frame.place(relwidth = 0.9, height = 80, relx = 0.05, rely = 0.05)

song_title_frame = tk.Text(root)
song_title_frame.place(relwidth = 0.9, height = 20, relx = 0.05, rely = 0.2)


label = tk.Label(directory_frame, text=input_path, wraplength = 600, justify='center', bg='gray')
label.pack()

setDirectory = tk.Button(root, text = "Choose Path", command = selectDirectory)
setDirectory.pack()

createFolder = tk.Button(root, text = "Create Folder", command = startProcess)
createFolder.pack()

root.mainloop()


    
with open('save.txt', 'w') as f:
    f.write(input_path)