
from tkinter import *       
from tkinter import messagebox
m=Tk()
m.title("SSN Mentoring system")
m.iconbitmap()

#img=PhotoImage(file=r'C:\Users\ashwi\Downloads\ssn-1.png')  #importing image of SSN
#lab=Label(m,image=img)
#lab.place(x=0,y=0,relheight=1,relwidth=1)
#img2=PhotoImage(file=r'C:\Users\ashwi\Downloads\ssn-logo.png')  #importing SSN logo
#lab2=Label(m,image=img2,anchor=CENTER)
#lab2.pack()

myframe=Frame(m,bg="#817D8B")   #importing the frame colour
myframe.pack(pady=20)
z=1
#ACADEMIC INFO SELECTION POP-UP
root = Tk()
root.geometry("400x400")
def show():
	label.config( text = clicked.get() )

# Dropdown menu options
options = [
	"CAT-1",
	"CAT-2",
	"SAT",
	"SEMESTER"]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("SELCT EXAM")

# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.pack()

# Create button, it will change label text
button = Button( root , text = "SELECT" , command = show ).pack()

# # Create Label
# label = Label( root , text = " " )
# label.pack()

def login():            # entering details of the user
    user=entry1.get()
    passw=entry2.get()
    if user=='' and passw=='':
        messagebox.showinfo("","blank invalid")
    elif (user=='arun' and passw=='123'):
        if z==1:
            root.destroy()
            global r4
            r4=Tk()
            a1=Button(r4,text='personal info',font=('Helvetica',16),fg='blue').place(relx=0.38,rely=0.5,anchor=CENTER)
            a2=Button(r4,text='mentorship',font=('Helvetica',16),fg='blue').place(relx=0.5,rely=0.5,anchor=CENTER)
            a3=Button(r4,text='academic info',font=('Helvetica',16),fg='blue').place(relx=0.62,rely=0.5,anchor=CENTER)
        
        if z==2:

            r2.destroy()
            global r3
            r3=Tk()
            a1=Button(r3,text='personal info',font=('Helvetica',16),fg='blue').place(relx=0.38,rely=0.5,anchor=CENTER)
            a2=Button(r3,text='mentorship',font=('Helvetica',16),fg='blue').place(relx=0.5,rely=0.5,anchor=CENTER)
            a3=Button(r3,text='academic info',command=show(),font=('Helvetica',16),fg='blue').place(relx=0.62,rely=0.5,anchor=CENTER)
        
    else:
        messagebox.showinfo("","incorrect")

def ope():
    global r2
    r1.destroy()
    r2=Tk()
    r2.geometry('1920x1080')
    
    #img=PhotoImage(file=r'C:\Users\ashwi\Downloads\ssn-1.png')
    #lab=Label(r2,image=img)
    #lab.place(x=0,y=0,relheight=1,relwidth=1)
    #img2=PhotoImage(file=r'C:\Users\ashwi\Downloads\ssn-logo.png')
    #lab2=Label(r2,image=img2,anchor=CENTER)
    #lab2.pack()

    
    global entry1
    global entry2
    b3=Button(r2,text="BACK",command=back).place(relx=0.55,rely=0.8)
    la=Label(r2,text="USERNAME",font=('Helvetica',16),fg='blue').place(relx=0.5,rely=0.5,anchor=CENTER)   #function for creating the username and password button
    la2=Label(r2,text='PASSWORD:',font=('Helvetica',16),fg='blue').place(relx=0.5,rely=0.6,anchor=CENTER)
    entry1=Entry(r2,bd=5)
    entry1.place(relx=0.6,rely=0.5,anchor=CENTER)
    entry2=Entry(r2,bd=5,show='*')
    entry2.place(relx=0.6,rely=0.6,anchor=CENTER)
    b2=Button(r2,text="LOGIN",fg='brown',font=('Helvetica',16),command=login,bd=6).place(relx=0.55,rely=0.7,anchor=CENTER)
    r2.mainloop()


def back():
    global r1
    root.destroy()
    r1=Tk()
    global z
    z=2
    r1.geometry('1920x1080')
    #img=PhotoImage(file=r'C:\Users\ashwi\Downloads\ssn-1.png')
    #lab=Label(r1,image=img)
    #lab.place(x=0,y=0,relheight=1,relwidth=1)
    #img2=PhotoImage(file=r'C:\Users\ashwi\Downloads\ssn-logo.png')
    #lab2=Label(r1,image=img2,anchor=CENTER)
    #lab2.pack()
    myframe=Frame(r1,bg="#817D8B")   #importing the frame colour
    myframe.pack(pady=20)
    m1=Button(myframe,text="manager",command=ope)
    m1.grid(row=1,column=0,padx=10,pady=10)
    m2=Button(myframe,text="mentor",command=ope)
    m2.grid(row=1,column=1,padx=10,pady=10)
    m3=Button(myframe,text="mentee",command=ope)
    m3.grid(row=1,column=2,padx=10,pady=10)
    r1.mainloop()
def open():
    global root
    m.destroy()
    root=Tk()
    
    root.geometry('1920x1080')
    #img=PhotoImage(file=r'C:\Users\ashwi\Downloads\ssn-1.png')
    #lab=Label(root,image=img)
    #lab.place(x=0,y=0,relheight=1,relwidth=1)
    #img2=PhotoImage(file=r'C:\Users\ashwi\Downloads\ssn-logo.png')
    #lab2=Label(root,image=img2,anchor=CENTER)
    #lab2.pack()
    global entry1
    global entry2
    b3=Button(root,text="BACK",command=back).place(relx=0.55,rely=0.8)
    la=Label(root,text="USERNAME",font=('Helvetica',16),fg='blue').place(relx=0.5,rely=0.5,anchor=CENTER)   #function for creating the username and password button
    la2=Label(root,text='PASSWORD:',font=('Helvetica',16),fg='blue').place(relx=0.5,rely=0.6,anchor=CENTER)
    entry1=Entry(root,bd=5)
    entry1.place(relx=0.6,rely=0.5,anchor=CENTER)
    entry2=Entry(root,bd=5,show='*')
    entry2.place(relx=0.6,rely=0.6,anchor=CENTER)
    b2=Button(root,text="LOGIN",fg='brown',font=('Helvetica',16),command=login,bd=6).place(relx=0.55,rely=0.7,anchor=CENTER)
    root.mainloop()

mybutton1=Button(myframe,text="Manager",command=open)        # creating buttons for manager, mentor , mentee
mybutton1.grid(row=1,column=0,padx=10,pady=10)
mybutton2=Button(myframe,text="Mentor",command=open)
mybutton2.grid(row=1,column=1,padx=10,pady=10)
mybutton3=Button(myframe,text="Mentee",command=open)    
mybutton3.grid(row=1,column=2,padx=10,pady=10)

m.mainloop()
