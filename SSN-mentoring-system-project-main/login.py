import csv
class hashtable:
    def __init__(self):
        self.size=0
        self.capacity=100
        self.arr=[None for i in range(self.capacity)]
    
    def gethash(self,key):
         return key
    #hashfunc()
    def __setitem__(self,key,value):
        k=self.gethash(key)
        self.arr[k]=value
        self.size+=1
    
    def __getitem__(self,key):
        k=self.gethash(key)
        return self.arr[k]
    
    def __str__(self):
        s="{"
        for i in range(self.size):
            s+=str(i+1)+':'+str(self.arr[int(i+1)])+","
        s=s.rstrip(',')+"}"
        return s
    
    def __iter__(self):
        for i in range(self.size):
#            yield self.arr[int(i+1)]
             yield i+1
    
    def __delitem__(self,key):
        k=self.gethash(key)
        self.arr.pop(int(key))
        self.size-=1

t=hashtable()
f=open(r"C:\Users\enter\OneDrive\arshat ssn files\PROJECT COMPONENT\sem 2 Final Project\GIT FILES\SSN-mentoring-system-project\newcredentials.txt","r")
r=csv.reader(f)
no=next(csv.reader(f))
for i in csv.reader(f):
    t[int(i[0])]=i[1:]
f.close()
c=0
u=input("enter a user name:")
v=input("enter a password:")
def give(us,p):
    for i in t:
        if [us,p]==t[i]:
            return t[i]
        else:
            continue
    return "Invalid username or password"

print(give(u,v))
#need to connect this with the login page
