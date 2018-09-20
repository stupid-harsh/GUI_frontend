from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os


folder_path=""
folder_counter=0

epoch=0
batch_size=0
num_class=0








def train():
    mmWindow = tk.Tk()
    mmWindow.geometry('500x500')
    mmtitle = tk.Label(mmWindow, text="Train", fg='blue')
    mmtitle.place(x=10, y=10)

    

    
    
    def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
        global folder_path
        global folder_counter
        global num_class

        folder_path = filedialog.askdirectory(title='Select your pictures folder')
        print(folder_path)

        files =os.listdir(folder_path)
        for fn in files:
            folder_counter+=1
         
        if folder_counter==0:
            print("this is an empty directory, pls try again")
        else:    
            num_class=folder_counter    
            print(folder_counter)
        
        Label(mmWindow, text=folder_path).place(x=10,y=100)
        
        Label(mmWindow, text=folder_counter).place(x=10,y=115)

    def show_entry_fields():
        global num_class
        print("Epochs: %s\nBatch Size: %s\nNum Classes: %s" % (e1.get(), e2.get(), e3.get()))
        
       
        Label(mmWindow, text=e1.get()).place(x=10,y=250)
        Label(mmWindow, text=e1.get()).place(x=10,y=275)
        Label(mmWindow, text=num_class).place(x=10,y=300)
        Label(mmWindow, text="Epochs").place(x=100,y=250)
        Label(mmWindow, text="Batch Size").place(x=100,y=275)
        Label(mmWindow, text="Num Classes").place(x=100,y=300)
        e3.delete(0,END)
        e1.delete(0,END)
        e2.delete(0,END)

    button2 = Button(mmWindow,text="Browse", command=browse_button)
    button2.place(x=30, y=50)

    lbl1 = Label(mmWindow,textvariable=folder_path)
    lbl1.place(x=40, y=100)


    Label(mmWindow, text="Epochs").place(x=10,y=150)
    Label(mmWindow, text="Batch Size").place(x=10,y=175)
    Label(mmWindow, text="Num Classes").place(x=10,y=200)

    e1 = Entry(mmWindow)
    e2 = Entry(mmWindow)
    e3 = Entry(mmWindow)

    


    e1.insert(10,"10")
    e2.insert(10,"12")
    e3.insert(10,num_class)

    e1.place(x=100, y=150)
    e2.place(x=100, y=175)
    e3.place(x=100, y=200)

    
    Button(mmWindow, text='Submit', command=show_entry_fields).place(x=50, y=225)    

    
    
    
    
    
    lbl1 = Label(mmWindow,textvariable=folder_path)
    lbl1.place(x=40, y=100)
    mmWindow.title('Training')
    mmWindow.iconbitmap("C:/Users/harsh/Desktop/logo/logo_small.ico")
    
    
    

    mmWindow.mainloop()
    
    
def classify():
    classifyWindow = tk.Tk()
    classifyWindow.geometry('500x500')



mWindow = tk.Tk()

# You can set any size you want
mWindow.geometry('600x500')
mWindow.title('Animal Classifier')
wtitle = tk.Label(mWindow, text="Please click the following option:", fg='blue')
wtitle.place(x=10, y=50)



# You can set any height and width you want
mmbutton = tk.Button(mWindow, height=5, width=20, text="Training", command=train)
mmbutton.place(x=100, y=140) 
classifybutton = tk.Button(mWindow, height=5, width=20, text="Classify", command=classify)
classifybutton.place(x=300, y=140) 



image = tk.PhotoImage(file="C:/Users/harsh/Desktop/logo/logo.png")
panel = tk.Label(mWindow, image=image)
panel.pack(side='top', fill='both', expand='yes')
panel.image = image
panel.place(x=50, y=350) 
mWindow.iconbitmap("C:/Users/harsh/Desktop/logo/logo_small.ico")

mWindow.mainloop()


