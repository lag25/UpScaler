import argparse
from gooey import Gooey, GooeyParser
import tkinter as tk   # In Python 3.x
from tkinter import *
from argparse import ArgumentParser
import subprocess
import os

class App:
    @Gooey(advanced=True, program_name="UpScaler", default_size=(900, 600), required_cols=1, optional_cols=2, monospace_display=False)
    def main(self):
        parser = GooeyParser(description="Calculate steering parameters") 
        parser.add_argument('foldername', help="Process Folder", widget='DirChooser')
        #parser.add_argument('filename', help='Process Image', widget='FileChooser')
        args = parser.parse_args()
       
        self.apply_transformation_folder(args.foldername)
        
        
    def apply_transformation_file(self,PATH):
        
             # Apply your custom transformation function here
        file_name = PATH.split('/')[-1]
        print(file_name)
        current_directory = os.getcwd().split(os.sep)
        base_directory = current_directory.pop()
        current_directory[-1] = 'models'
        base_directory = os.sep.join(base_directory)
        current_directory = os.sep.join(current_directory)
        


# Print the current working directory
        print("Current Directory:", current_directory)
        bash_cmd = f"{os.path.join(base_directory,realesrgan-ncnn-vulkan.exe)} -i {PATH} -o {file_name}_output.png -g 0 -m {current_directory} -n realesrgan-x4plus"
        
        result = subprocess.run(bash_cmd, shell=True, check=True, text=True)  
        print(f'Completed Processing {file_name}')
        
        
    def apply_transformation_folder(self,PATH):
        for file in os.listdir(PATH):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                self.apply_transformation_file(os.path.join(PATH,file))
            
    
    
        
    
    
if __name__ == "__main__":
    obj = App()
    obj.main()