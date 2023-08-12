from tkinter import *       
from tkinter import messagebox
import math
from samplecode import *
import csv
#from tkcalendar import Calendar

exam=None
one_mentee_details=None
class BST:

	"""This constructor takes 3 arguments: self, key and number. Key-record, number - serial number"""
	def __init__(self,key,number):
		self.key=key
		self.lchild=None
		self.rchild=None
		self.position=number
    
	# This method inserts the records in the binary search tree. It compares the number 
	# passed as an argument, compares the number with the numbers of previously inserted nodes,
	#  and places the record in the tree accordingly.

	def insert(self,data,number):
		if self.position is None:
			self.key=data
			return
		elif self.position>number:
			if self.lchild is None:
				self.lchild= BST(data,number)
			else:
				self.lchild.insert(data,number)
		else:
			if self.rchild:
				self.rchild.insert(data,number)
			else:
				self.rchild= BST(data,number)

	"""This method traverses and prints the records in the ascending order of serial number of records."""

	def inorder(self):
		if self.lchild:
			self.lchild.inorder()
		print(self.key,end= "\n")
		if self.rchild:
			self.rchild.inorder()
"""Piece of code which reads the records in the csv file containing mentee details""" 

f=open(r"Z:\ssn mentoring system project\SSN-mentoring-system-project\IT-A details.txt","r")
n=next(csv.reader(f))
l=[]
for i in csv.reader(f):
	l.append(i)
f.close()

"""Insertion of records into the binary search tree start here."""

obj=BST(l[31],32)
n=16
p=n
i=1
q=n
c=0
while c<5:
    
    for j in range(2**i):
        obj.insert(l[int(p-1)],p)
        p= p + 2**((math.log(q,2))+1)
    i+=1
    o = n/(2**(i-1))
    p=o
    q=o
    c+=1
def retrievex(tree,username,b=0):

	"""un-username,
	a-the coulumn of username"""
	
	global one_mentee_details
	if tree.key[b]==username:
		
		one_mentee_details=tree.key
		return tree.key
	elif username<tree.key[b]:
		if tree.lchild:
			retrievex(tree.lchild,username,b)
		else:
			return False
	elif username>tree.key[b]:
		if tree.rchild:
			retrievex(tree.rchild,username,b)
		else:
		    return False

"""Calling .inorder() method to print the records."""
m=Tk()
m.title("SSN Mentoring system")
m.iconbitmap()
m.geometry('1920x1080')
#
img=PhotoImage(file=r'Z:\ssn mentoring system project\SSN-mentoring-system-project\ssnpro1.png')  #importing image of SSN
lab=Label(m,image=img)
lab.place(x=0,y=0,relheight=1,relwidth=1)

myframe=LabelFrame(m,bg="#A2ACBE",bd=0)   #importing the frame colour
myframe.pack(padx=250,pady=250)

f=open(r"Z:\ssn mentoring system project\SSN-mentoring-system-project\credentials1.txt","r")

lis=[]
x=[]
y=[]
no=next(csv.reader(f))
for i in csv.reader(f):
    x.append(i[1])
f.seek(1)
no=next(csv.reader(f))
for j in csv.reader(f):
    y.append(j[2])
lis.append(x)
lis.append(y)
#f=open(r"C:\Users\ashwi\OneDrive\Documents\Ashwin M\New folder\SSN-mentoring-system-project\credentials1.txt","r")
aru=[]
f.seek(0)
a=next(csv.reader(f))
for z in csv.reader(f):
    aru.append(z)
#f.close()
f.close()
s=None
one_mentee_details=None
def personalinfo(myframe):
    
    myframe.destroy()
    myframe=LabelFrame(m,bg="white")   #importing the frame colour
    myframe.place(relx=0.5,rely=0.6)
    global aru
                      #mentee personal info

    

    

    def search(tree,data):

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
    credtree=createBST(aru)
   

    l1=[]
    def check(tree,un,pd):
        
        
        search(tree,[un,pd])

        
    
        retrieve(mentee_details_tree,user4)
        l1=[("digital Id",one_mentee_details[1]),("roll No",one_mentee_details[2]),
        ("Name",one_mentee_details[3]),("Section",one_mentee_details[4]),("dept",one_mentee_details[5]),
        ("Email-Id",one_mentee_details[6]),("Gender",one_mentee_details[7])]
        
        
        for i in range(len(l1)):
            for j in range(2):
                e=Entry(m,width=20,fg='blue')
                e.grid(row=i,column=j)
                e.insert(0,l1[i][j])  
            
        
    b=check(credtree,user4,passw4)
def show(myframe):
    global exam
    myframe.destroy()
    
    myframe=LabelFrame(m,text=clicked.get(),bg="black")   #importing the frame colour
    myframe.place(relx=0.5,rely=0.5)
    
    myframe.config( text = clicked.get() )
    exam=str(clicked.get())
    print(exam)
    if exam=="CAT-1":
        f=open(r"Z:\ssn mentoring system project\SSN-mentoring-system-project\CAT-1results.txt","r")
        c=csv.reader(f)
        no=next(c)
        l=[]
        for i in c:
            l.append(i)
        f.close()
        
        marks_tree=createBST(l)
    elif exam=="CAT-2":
        f=open(r"Z:\ssn mentoring system project\SSN-mentoring-system-project\CAT-2 results.txt","r")
        c=csv.reader(f)
        no=next(c)
        l=[]
        for i in c:
            l.append(i)
        f.close()
        marks_tree=createBST(l)
    elif exam=="SAT":
        f=open()  #inside the parenthesis put the filename containing SAT Marks
        c=csv.reader(f)
        no=next(c)
        l=[]
        for i in c:
            l.append(i)
        f.close()
        marks_tree=createBST(l)
    
    retrievex(marks_tree,user4,1)
    marks_details=one_mentee_details[3:]
    marks_details=[("Maths",marks_details[0]),("BEEE",marks_details[1]),("Physics",marks_details[2]),("PDS",marks_details[3]),
    ("HSE",marks_details[4]),("EVS",marks_details[5])]
    total_rows=len(marks_details)
    
    for i in range(total_rows):
        for j in range(2):
            e=Entry(m,width=20,fg='blue')
            e.grid(row=i,column=j)
            e.insert(0,marks_details[i][j])  
    

    
def academicdetails(myframe):
    global clicked
    myframe.destroy()
    myframe=LabelFrame(m,bg="white")   #importing the frame colour
    myframe.place(relx=0.5,rely=0.5)


    options = [                              
	"CAT-1",
	"CAT-2",
	"SAT"]

# datatype of menu text
    clicked = StringVar()

    # initial menu text
    clicked.set("SELCT EXAM")

    # Create Dropdown menu
    drop = OptionMenu( myframe, clicked , *options )
    drop.pack()

    # Create button, it will change label text
    button = Button( myframe, text = "click here",command=lambda :show(myframe)).pack()
    return
def mentorship(myframe):
    return
def login(myframe):   
    global user4
    global passw4
    
            # entering details of the user
    user4=entry1.get()
    passw4=entry2.get()
    
    if user4=='' and passw4=='':
        messagebox.showinfo("","blank invalid")
    elif (user4 in lis[0] and passw4 in lis[1]):
        myframe.destroy()
        myframe=LabelFrame(m,bg="white")   #importing the frame colour
        myframe.pack(padx=250,pady=250)
        mb=Button(myframe,text='PERSONAL INFO',font=('Helvetica',16),borderwidth=0,bg="white",fg='blue',command=lambda :personalinfo(myframe))
        mb.grid(row=1,column=1,padx=10,pady=10)
        mb1=Button(myframe,text='ACADEMIC DETAILS',font=('Helvetica',16),borderwidth=0,bg="white",fg='blue',command=lambda :academicdetails(myframe))
        mb1.grid(row=1,column=2,padx=10,pady=10)
        mb2=Button(myframe,text='MENTORSHIP',font=('Helvetica',16),borderwidth=0,bg="white",fg='blue',command=lambda :mentorship(myframe))
        mb2.grid(row=1,column=3,padx=10,pady=10)
    else:
        messagebox.showinfo("","incorrect")
#def next(myframe):          #for creating a page to add update delete
    # myframe.destroy()
    # myframe=LabelFrame(m,bg="white")   #importing the frame colour
    # myframe.pack(padx=250,pady=250)
    # mb=Button(myframe,text='PERSONAL INFO',font=('Helvetica',16),borderwidth=0,bg="white",fg='blue',command=lambda :personalinfo(myframe))
    # mb.grid(row=1,column=1,padx=10,pady=10)
    # mb1=Button(myframe,text='ACADEMIC DETAILS',font=('Helvetica',16),borderwidth=0,bg="white",fg='blue',command=lambda :academicdetails(myframe))
    # mb1.grid(row=1,column=2,padx=10,pady=10)
    # mb2=Button(myframe,text='MENTORSHIP',font=('Helvetica',16),borderwidth=0,bg="white",fg='blue',command=lambda :mentorship(myframe))
    # mb2.grid(row=1,column=3,padx=10,pady=10)
    # return

def login1(myframe):            # entering details of the user
    user=entry1.get()
    passw=entry2.get()
    if user=='' and passw=='':
        messagebox.showinfo("","blank invalid")
    elif (user=='chandrasekar@ssn.edu.in' and passw=='chandru'):
        myframe.destroy()
        myframe=LabelFrame(m,bg="white")   #importing the frame colour
        myframe.grid(row=0,column=0)
        #cal=Calendar(myframe, selectmode = 'day',
         #      year = 2020, month = 5,
         #      day = 22)
        #cal.pack()
        column=len(l[1])
        for i in range(0,21):
            for j in range(column):
                e=Button(m,width=25,height=2,text=l[i][j],fg='white',bg='black',borderwidth=0)
                e.grid(row=0,column=0)
                e.grid(row=i,column=j)
    
        
    elif (user=='rajalakshmi@ssn.edu.in' and passw=='raji'):
        myframe.destroy()
        myframe=LabelFrame(m,bg="white")   #importing the frame colour
        myframe.grid(row=0,column=0)
        column=len(l[1])
        for i in range(21,42):
            for j in range(column):
                e=Button(m,width=25,height=2,text=l[i][j],fg='white',bg='black',borderwidth=0)
                e.grid(row=0,column=0)
                e.grid(row=i,column=j)
        
      
    elif (user=='divyajohn@ssn.edu.in' and passw=='dj'):
        myframe.destroy()
        myframe=LabelFrame(m,bg="white")   #importing the frame colour
        myframe.grid(row=0,column=0,padx=100,pady=50)
        column=len(l[1])
        for i in range(42,63):
            for j in range(column):
                e=Button(myframe,width=25,height=2,text=l[i][j],fg='white',bg='#A2ACBE',borderwidth=0,command=lambda:next(myframe))
                e.grid(row=0,column=0)
                e.grid(row=i,column=j)
       
    else:
        messagebox.showinfo("","incorrect")
def raja(myframe):
    myframe.destroy()
    myframe=LabelFrame(m,bg="white")   #importing the frame colour
    myframe.grid(row=0,column=0)
    column=len(l[1])
    for i in range(0,21):
        for j in range(column):
            e=Entry(m,width=20,fg='blue')
            e.grid(row=i,column=j)
            e.insert(0,l[i][j])
def chandra(myframe):
    myframe.destroy()
    myframe=LabelFrame(m,bg="white")   #importing the frame colour
    myframe.grid(row=0,column=0)
    column=len(l[1])
    for i in range(21,42):
        for j in range(column):
            e=Entry(m,width=20,fg='blue')
            e.grid(row=i,column=j)
            e.insert(0,l[i][j])
def dj(myframe):
    myframe.destroy()
    myframe=LabelFrame(m,bg="white")   #importing the frame colour
    myframe.grid(row=0,column=0)
    
    column=len(l[1])
    for i in range(42,63):
        for j in range(column):
            e=Entry(m,width=20,fg='blue')
            e.grid(row=i,column=j)
            e.insert(0,l[i][j])
    
def login2(myframe):
    
    user2=entry1.get()
    passw2=entry2.get()
    myframe.destroy()
    myframe=LabelFrame(m,bg="#A2ACBE",bd=0)   #importing the frame colour
    myframe.pack(padx=250,pady=250)
    
    if user2=='' and passw2=='':
        messagebox.showinfo("","blank invalid")
    elif user2=='manager' and passw2=='123':
        myframe.destroy()
        myframe=LabelFrame(m,bg="white")   #importing the frame colour
        myframe.grid(row=0,column=0)
        
        b1=Button(myframe,text='ACADEMIC REPORT',width=0)
        
        b1.grid(row=0,column=1,padx=10,pady=10)
        b2=Button(myframe,text='Chandrasekar',width=0,command=lambda:chandra(myframe))
        b2.grid(row=0,column=2,padx=10,pady=10)
        b=Button(myframe,text='Rajalakshmi',width=0,command=lambda:raja(myframe))
        b.grid(row=0,column=3,padx=10,pady=10)
        b3=Button(myframe,text='Divya John',width=0,command=lambda:dj(myframe))
        b3.grid(row=0,column=4,padx=10,pady=10)

def back(myframe):
    myframe.destroy()
    myframe=LabelFrame(m,bg="#A2ACBE",bd=0)   #importing the frame colour
    myframe.pack(padx=250,pady=250)
    mybutton1=Button(myframe,text="Manager",bg="#A2ACBE",font=('Helvetica',14),command=lambda:open2(myframe))        # creating buttons for manager, mentor , mentee
    mybutton1.grid(row=1,column=0,padx=10,pady=10)
    mybutton2=Button(myframe,text="Mentor",bg="#A2ACBE",font=('Helvetica',14),command=lambda :open1(myframe))
    mybutton2.grid(row=1,column=1,padx=10,pady=10)
    mybutton3=Button(myframe,text="Mentee",bg="#A2ACBE",font=('Helvetica',14),command=lambda :openx(myframe))    
    mybutton3.grid(row=1,column=2,padx=10,pady=10)
def openx(myframe):
    
    myframe.destroy()
    myframe=LabelFrame(m,bg="#A2ACBE",padx=25,pady=40,bd=0)   #importing the frame colour
    myframe.pack(padx=250,pady=250)

   
    global entry1
    global entry2
    b3=Button(myframe,text="BACK",fg='white',bg='#A2ACBE',font=('Helvetica',12),command=lambda :back(myframe)).place(relx=0.3,rely=1)
    la=Label(myframe,text="USERNAME :",font=('Helvetica',14),fg='white',bg='#A2ACBE').grid(row=1,column=0)   #function for creating the username and password button
    la2=Label(myframe,text='PASSWORD :',font=('Helvetica',14),fg='white',bg='#A2ACBE').grid(row=2,column=0)
    entry1=Entry(myframe,bd=5)
    entry1.grid(row=1,column=2)
    entry2=Entry(myframe,bd=5,show='*')
    entry2.grid(row=2,column=2)
    b2=Button(myframe,text="LOGIN",fg='white',bg='#A2ACBE',padx=1,pady=1,font=('Helvetica',12),command=lambda :login(myframe)).place(relx=0.7,rely=1)
def open1(myframe):
    
    myframe.destroy()
    myframe=LabelFrame(m,bg="#A2ACBE",padx=25,pady=40,bd=0)   #importing the frame colour
    myframe.pack(padx=250,pady=250)

   
    global entry1
    global entry2
    b3=Button(myframe,text="BACK",fg='white',bg='#A2ACBE',font=('Helvetica',12),command=lambda :back(myframe)).place(relx=0.3,rely=1)
    la=Label(myframe,text="USERNAME :",font=('Helvetica',14),fg='white',bg='#A2ACBE').grid(row=1,column=0)   #function for creating the username and password button
    la2=Label(myframe,text='PASSWORD :',font=('Helvetica',14),fg='white',bg='#A2ACBE').grid(row=2,column=0)
    entry1=Entry(myframe,bd=5)
    entry1.grid(row=1,column=2)
    entry2=Entry(myframe,bd=5,show='*')
    entry2.grid(row=2,column=2)
    b2=Button(myframe,text="LOGIN",fg='white',bg='#A2ACBE',padx=1,pady=1,font=('Helvetica',12),command=lambda :login1(myframe)).place(relx=0.7,rely=1)
        
def open2(myframe):
    myframe.destroy()
    myframe=LabelFrame(m,bg="#A2ACBE",padx=25,pady=40,bd=0)   #importing the frame colour
    myframe.pack(padx=250,pady=250)
    global entry1
    global entry2
    b3=Button(myframe,text="BACK",fg='white',bg='#A2ACBE',font=('Helvetica',12),command=lambda :back(myframe)).place(relx=0.3,rely=1)
    la=Label(myframe,text="USERNAME :",font=('Helvetica',14),fg='white',bg='#A2ACBE').grid(row=1,column=0)   #function for creating the username and password button
    la2=Label(myframe,text='PASSWORD :',font=('Helvetica',14),fg='white',bg='#A2ACBE').grid(row=2,column=0)
    entry1=Entry(myframe,bd=5)
    entry1.grid(row=1,column=2)
    entry2=Entry(myframe,bd=5,show='*')
    entry2.grid(row=2,column=2)
    b2=Button(myframe,text="LOGIN",fg='white',bg='#A2ACBE',padx=1,pady=1,font=('Helvetica',12),command=lambda :login2(myframe)).place(relx=0.7,rely=1)


mybutton1=Button(myframe,text="Manager",bg="#A2ACBE",font=('Helvetica',14),command=lambda :open2(myframe))        # creating buttons for manager, mentor , mentee
mybutton1.grid(row=4,column=0,padx=10,pady=10)
mybutton2=Button(myframe,text="Mentor",bg="#A2ACBE",font=('Helvetica',14),command=lambda :open1(myframe))
mybutton2.grid(row=4,column=1,padx=10,pady=10)
mybutton3=Button(myframe,text="Mentee",bg="#A2ACBE",font=('Helvetica',14),command=lambda :openx(myframe))    
mybutton3.grid(row=4,column=2,padx=10,pady=10)

m.mainloop()
