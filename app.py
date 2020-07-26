# -*- coding: utf-8 -*-

import os, shutil
import tkinter as tk

template_path = './00_PROJECT_FOLDER_TEMPLATE'
template_string = 'TEMPLATE'

song_title = input('Song Title:')

destination_path = f'./{song_title}'

print(song_title)

def copyTemplateToSong():
    shutil.copytree(template_path, destination_path)




def renameToSong():
    for folderName, subfolders, filenames in os.walk(destination_path):

        print(f'The current folder is {folderName}')
        
        for subfolder in subfolders:
            print(f'SUBFOLDER of {folderName}: {subfolder}') 

        for filename in filenames:
            print(f'FILE INSIDE {folderName}: {filename}')

            if(template_string in filename):
            
                new_filename = filename.replace(template_string, song_title)

                os.rename(f'{folderName}/{filename}', f'{folderName}/{new_filename}')
                print('Renamed successfully')
        
        
copyTemplateToSong()
renameToSong()





    