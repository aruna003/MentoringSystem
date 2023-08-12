#python email sender
#import os  #(right now we're not using)
import csv
import smtplib
#email address from the file
receivermail=input("enter a email address to send email:")#change this to tkinter

def emailandpassword():
    f=open(r"C:\Users\enter\OneDrive\arshat ssn files\PROJECT COMPONENT\sem 2 project\GIT FILES\SSN-mentoring-system-project\credentials1.txt","r")
    n=next(csv.reader(f))
    l=[]
    for i in csv.reader(f):
        l.append(i)
    f.close()
    # print(l)

    for email,password in l:
        if email==receivermail:
            return(email)




EMAIL_ADDRESS = "enteraemail"
EMAIL_PASS="enterapassword"
with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()#identifies ourselves with thee mail server
    smtp.starttls()#to encrypt traffic
    smtp.ehlo()
#login now but remember it's always safe to encrypt the login info within "ENVIRONMENT VARIABLES"
    smtp.login(EMAIL_ADDRESS,EMAIL_PASS)
    subject = 'test email'
    body = 'Hi badri'
    msg =f'Subject:{subject}\n\n{body}'
    smtp.sendmail(EMAIL_ADDRESS,emailandpassword(),msg)
    # print(f"{emailandpassword()}")