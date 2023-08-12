from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
#from Projectmenteeacademicinfo import *

root=Tk()
root.title("mentror report")
root.geometry("400x200")


def chart():
    #need to to do some file handling or just get the data as a bst and damn plot it
    #input needs to from our bst or files
    
    exp_vals=[20,78,2]
    colors=["r","g","b"]
    #exp_labels=["failurepercentage","passpercentage","absentees"]
    plt.pie(exp_vals,radius=1.5,autopct='%0.1f%%',shadow=True,explode=[0,0,0])
    plt.axis("equal")
    plt.show()

mybutton = Button(root,text="see report ",command=chart)
mybutton.pack()

root.mainloop()
    