from cgitb import text
from tkinter import *       
from tkinter.ttk import *
from tkinter import messagebox
import os
 
## opening any folder 
#def openFolder(path):
#    path='C:/Users/jerri/Documents'
#    command = 'explorer.exe ' + path
#    os.system(command)
#
## opening files
#file = 'calculator.py'
#command = 'start ' + file
#path = "C:/Users/jerri/Pictures/"
##os.path.
#os.system(command)
#
## opening current folder 
#command = 'explorer.exe .'
#os.system(command)
#
## opening any folder 
#path='C:/Users/jerri/'
#command = 'explorer.exe ' + path
#os.system(command)
#
#
#root = Tk()         
#root.geometry('100x100')    
#btn = Button(root, text = 'Click me !',command = openFolder())
#btn.pack(side = 'top')    
#root.mainloop()
#
#print(os.times())

##### WARNING: THIS CAN AND WILL RENAME ALL FILES IN THE DIRECTORY #####
##### PLEASE MAKE A BACK UP OR BE SURE ABOUT WHAT YOU ARE DOING #####
# # Function to rename multiple files
# def main():
#     #i = 0
#     #path="D:/git/"
#     path = "C:/"
#     for filename in os.listdir(path):
#         if " (2022_02_14 10_35_21 UTC)" in filename:
#             os.rename(os.path.join(path, filename), os.path.join(path, filename.replace(" (2022_02_14 10_35_21 UTC)", "")))
# 
#         #my_dest ="soul" + str(i) + ".jpg"
#         #my_source = path + filename
#         #my_dest = path + my_dest
#         # rename() function will
#         # rename all the files
#         #os.rename(my_source, my_dest)
#         #i += 1
# # Driver Code
# if __name__ == '__main__':
#    # Calling main() function
#    main()


##Renaming only a list of files in a folder
#files_to_rename = ['sales_1.txt', 'sales_4.txt']
#folder = r"E:\demos\files\reports\\"
#
## Iterate through the folder
#for file in os.listdir(folder):
#    # Checking if the file is present in the list
#    if file in files_to_rename:
#        # construct current name using file name and path
#        old_name = os.path.join(folder, file)
#        # get file name without extension
#        only_name = os.path.splitext(file)[0]
#
#        # Adding the new name with extension
#        new_base = only_name + '_new' + '.txt'
#        # construct full file path
#        new_name = os.path.join(folder, new_base)
#
#        # Renaming the file
#        os.rename(old_name, new_name)
#
## verify the result
#res = os.listdir(folder)
#print(res)




# Python program to create
# a file explorer in Tkinter
  
# import all components
# from the tkinter library
from tkinter import *
  
# import filedialog module
from tkinter import filedialog
from turtle import bgcolor
  
# Functions for opening the
# file explorer window
def browseFolder():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    foldername = filedialog.askdirectory(title = "Select a Folder")
    folder_path.set(foldername)
    os.chdir(folder_path.get())
    print(foldername)
    return

def browseFiles():
    global folder_path
    filename = filedialog.askopenfilename(initialdir = folder_path, title = "Select a File", filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py"),("Executables","*.exe")))

    # Change label contents
    removal_entry.delete(0, END)
    
    reverse_filename = filename[::-1]
    slash_index = (len(filename) - reverse_filename.index("/") - 1)
    period_index = (len(filename) - reverse_filename.index(".") - 1)

    foldername = filename[:slash_index]
    filename = filename[slash_index + 1:period_index]
    removal_entry.insert(0, filename)
    folder_path.set(foldername)
    os.chdir(folder_path.get())
    return

def remove():
    global folder_path
    input = removal_entry.get()
    messagebox.showwarning("WARNING!","WARNING: THIS CAN AND WILL RENAME ALL FILES IN THE DIRECTORY, CLICK OK TO PROCEED")
    # Delete label contents
    removal_entry.delete(0, END)
    print("Removing  all instances of '" + input + "' from the directory")
    os.chdir(folder_path.get())
    current_path = os.getcwd()
    for filename in os.listdir(current_path):
        if input in filename:
            try:
                print("Old: " + filename)
                os.rename(os.path.join(current_path, filename), os.path.join(current_path, filename.replace(input, "")))
            except FileExistsError:
                print("File already exists")
                continue
    return

def exit():
    window.destroy()
    return
    
# Create the root window
window = Tk()
  
# Set window title
window.title("File Renamer/Remover")
  
# Set window size
window.geometry("500x500")
  
#Set window background color
window.config(background = "black")

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)

# Create a File Explorer label
#label_file_explorer = Label(window,
#                            text = "Select a file:",
#                            #width = 100, height = 1,
#                            fg = "blue")

folder_path = StringVar()
label_file_explorer = Label(window, textvariable=folder_path, text = "Directory to Search:")
#lbl1.grid(row=1, column=0, sticky=NSEW)
      
file_explore = Button(window, text = "Browse for a File", command = browseFiles)

folder_explore = Button(window, text="Browse for a Folder", command=browseFolder)  

button_exit = Button(window, text = "Exit", command = exit, bg = 'green')

removal_entry = Entry(window, text= "Enter file name or phrase to remove")

removal_button = Button(window,
                        text = "Remove Input",
                        command = remove,
                        bg = 'red')

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 0, row = 0, sticky = NSEW, columnspan = 2, padx=5, pady=5)
  
file_explore.grid(column = 2, row = 1, sticky = NSEW, padx=5, pady=5)

folder_explore.grid(row=0, column=2, sticky = NSEW, padx=5, pady=5)  

button_exit.grid(column = 0,row = 3, sticky = NSEW, columnspan=3, padx=5, pady=5)
  
removal_entry.grid(column = 0, row = 1, sticky = NSEW, columnspan = 2, padx=5, pady=5)

removal_button.grid(column = 0, row = 2, sticky = NSEW, columnspan = 3, padx=5, pady=5)







# Let the window wait for any events
window.mainloop()