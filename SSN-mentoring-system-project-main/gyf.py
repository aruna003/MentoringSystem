from tkinter import *

#mentee personal info

import csv
from samplecode import *
import math

s=None
one_mentee_details=None

def search(tree,data):
  """This function checks whether the function present in the tree or not
  Makes s as 'found' if found else s remains as it is.
  """
  global s
  if tree.key==data:
    s="found"
  elif data<tree.key:
    if tree.lchild:
      search(tree.lchild,data)
    else:
      return False
  elif data>tree.key:
    if tree.rchild:
      search(tree.rchild,data)
    else:
      return False


def createBST(l,a=0):
    """This function creates BST """
    obj=BST(l[31][a:],32)
    n=16
    p=n
    i=1
    q=n
    c=0
    while c<5:
        
        for j in range(2**i):
            obj.insert(l[int(p-1)][a:],p)
            p= p + 2**((math.log(q,2))+1)
        i+=1
        o = n/(2**(i-1))
        p=o
        q=o
        c+=1
    return obj

def retrieve(tree,um):
    global one_mentee_details
    if tree.key[-2]==um:
      one_mentee_details=tree.key
    elif um<tree.key[-2]:
      if tree.lchild:
        retrieve(tree.lchild,um)
      else:
        return False
    elif um>tree.key[-2]:
      if tree.rchild:
        retrieve(tree.rchild,um)
      else:
        return False
    

f=open(r"C:\Users\ashwi\OneDrive\Documents\Ashwin M\New folder\SSN-mentoring-system-project\credentials1.txt","r")
l=[]
no=next(csv.reader(f))
for i in csv.reader(f):
    l.append(i)
f.close()



credtree=createBST(l)
username=input("Enter correct username:")
password=input("Enter correct password:")

l1=[]
def check(tree,un,pd):
    
    
    search(tree,[un,pd])

    if s is None:
        return "Invalid username or password"
    else:
        retrieve(mentee_details_tree,username)
        l1=[("digital Id",one_mentee_details[1]),("roll No",one_mentee_details[2]),
        ("Name",one_mentee_details[3]),("Section",one_mentee_details[4]),("dept",one_mentee_details[5]),
        ("Email-Id",one_mentee_details[6]),("Gender",one_mentee_details[7])]
    root=Tk()
    for i in range(len(l1)):
        for j in range(2):
            e=Entry(root,width=20,fg='blue')
            e.grid(row=i,column=j)
            e.insert(0,l1[i][j])  
        

    root.mainloop()
b=check(credtree,username,password)
