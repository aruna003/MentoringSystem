import csv
import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import avl
# import linkedlist
#file names should be changed
import ctypes
class Arr:
    __slots__="size","capacity","array"
    def __init__(self):
        self.capacity=2
        self.array=(ctypes.py_object*self.capacity)()
        self.array[0]=None
        self.size=1

    def append(self,data):
        if self.size==self.capacity:
            self.resize(2*self.capacity)
        self.array[self.size]=data
        self.size+=1
    
    def __len__(self):
        return self.size

    def resize(self,newcap):
        newarray=(ctypes.py_object*newcap)()
        for i in range(self.size):
            newarray[i]=self.array[i]
        self.array=newarray
        self.capacity=newcap
    
    def is_empty(self):
        return self.size==0

    def __getitem__(self,index):
        if not self.is_empty():
            if 0<=index<self.size:
                return self.array[index]
            raise IndexError('invalis index')
        return "Array is empty"
    
    def __str__(self):
        s="["
        for i in range(self.size):
            s+=str(self.array[i])+","
        s=s.rstrip(",")+"]"
        return s
    
    def __iter__(self):
        for i in range(1,self.size):
            yield self.array[i]
f5=open(r"C:\Users\enter\OneDrive\arshat ssn files\PROJECT COMPONENT\sem 2 Final Project\GIT FILES\SSN-mentoring-system-project\CAT-1results.txt","r")
r5=csv.reader(f5)
no=next(csv.reader(f5))
cat1=Arr()
for i in csv.reader(f5):
    cat1.append(i)
f5.close()
#reading cat2.txt file. lines:77-83
f6=open(r"C:\Users\enter\OneDrive\arshat ssn files\PROJECT COMPONENT\sem 2 Final Project\GIT FILES\SSN-mentoring-system-project\CAT-2 results.txt","r")
r6=csv.reader(f6)
no=next(csv.reader(f6))
cat2=Arr()
for i in csv.reader(f6):
    cat2.append(i)
f6.close()
def math(arr,n=3):
    marks=Arr()
    for i in arr:
        marks.append([i[0],i[1],i[n]])
    return marks
def beee(arr,n=4):
    marks=Arr()
    for i in arr:
        marks.append([i[0],i[1],i[n]])
    return marks
def phy(arr,n=5):
    marks=Arr()
    for i in arr:
        marks.append([i[0],i[1],i[n]])
    return marks
def pds(arr,n=6):
    marks=Arr()
    for i in arr:
        marks.append([i[0],i[1],i[n]])
    return marks
def hse(arr,n=7):
    marks=Arr()
    for i in arr:
        marks.append([i[0],i[1],i[n]])
    return marks
def evs(arr,n=8):
    marks=Arr()
    for i in arr:
        marks.append([i[0],i[1],i[n]])
    return marks
def CAT1(arr=cat1):
    marks=Arr()
    for i in arr:
        marks.append([i[0],i[1],i[3],i[4],i[5],i[6],i[7],i[8]])
    return marks
def CAT2(arr=cat2):
    marks=Arr()
    for i in arr:
        marks.append([i[0],i[1],i[3],i[4],i[5],i[6],i[7],i[8]])
    return marks
def subject(sub):
    if sub=="math":
        a=math(cat1)
        m=marks(a)
        return m
    elif sub=="beee":
        a=beee(cat1)
        m=marks(a)
        return m
    elif sub=="phy":
        a=phy(cat1)
        m=marks(a)
        return m
    elif sub=="pds":
        a=pds(cat1)
        m=marks(a)
        return m
    elif sub=="hse":
        a=hse(cat1)
        m=marks(a)
        return m
    elif sub=="evs":
        a=evs(cat1)
        m=marks(a)
        return m
    else:
        print("INVALID SUBJECT SELECTED")
#plotting functions and plot creation
l1=[]
def marks(arr,l=[]):
    for i in arr:
        l.append(int(i[-1]))
    return l
markinput=input("enter a subject:")
mark=subject(markinput)
print(mark)
# subject("beee")
# subject("phy")
# subject("pds")
# subject("hse")
# subject("evs")
# frequencies
ages = mark
# frequencies
# setting the ranges and no. of intervals
range = (0, 50)
bins = 5

# plotting a histogram
plt.hist(ages, bins, range, color = 'green',
		histtype = 'bar', rwidth = 0.8)
# x-axis label
plt.xlabel('age')
# frequency label
plt.ylabel('No. of people')
# plot title
plt.title('My histogram')
# function to show the plot
plt.show()
fp=[]
pp=[]
ap=[]
#now we have to take the mark list traverse it and find students who passed the test and failed the test
def fpp_count(mark):
    for i in mark:
        if 50>=i>=25:
            pp.append(i)
        elif 0<=i<=25:
            fp.append(i)
        else:
            ap.append(i)
    # return f'{len(pp)},{len(fp)},{len(ap)}'
    return len(pp),len(fp),len(ap)
# print(fpp_count(mark))
print(fp)
print(ap)
print(pp)
#now with this function we cal culate the percentage
percent_input=fpp_count(mark)
print(percent_input)
l=[]
for j in percent_input:
    j=(j/65)*100
    l.append(j)
# T=a+b+c
print(l)
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
    exp_vals= [int(l[0]),int(l[1]),int(l[2])]
    print(l)
    colors=["r","g","b"]
    #exp_labels=["failurepercentage","passpercentage","absentees"]
    plt.pie(exp_vals,radius=1.5,autopct='%0.1f%%',shadow=True)
    plt.axis("equal")
    plt.title("Composition of results and Average marks")
    plt.show()
mybutton = Button(root,text="see report ",command=chart)
mybutton.pack()
root.mainloop()
    

