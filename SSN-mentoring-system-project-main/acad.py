from main import cat1,cat2
import ARRAY

def math(arr,n=3):
    marks=ARRAY.Arr()
    for i in arr:
        marks.append([i[0],i[1],i[n]])
    return marks

def beee(arr,n=4):
    marks=ARRAY.Arr()
    for i in arr:
        marks.append([i[0],i[1],i[n]])
    return marks

def phy(arr,n=5):
    marks=ARRAY.Arr()
    for i in arr:
        marks.append([i[0],i[1],i[n]])
    return marks

def pds(arr,n=6):
    marks=ARRAY.Arr()
    for i in arr:
        marks.append([i[0],i[1],i[n]])
    return marks

def hse(arr,n=7):
    marks=ARRAY.Arr()
    for i in arr:
        marks.append([i[0],i[1],i[n]])
    return marks

def evs(arr,n=8):
    marks=ARRAY.Arr()
    for i in arr:
        marks.append([i[0],i[1],i[n]])
    return marks

def CAT1(arr=cat1):
    marks=ARRAY.Arr()
    for i in arr:
        marks.append([i[0],i[1],i[3],i[4],i[5],i[6],i[7],i[8]])
    return marks

def CAT2(arr=cat2):
    marks=ARRAY.Arr()
    for i in arr:
        marks.append([i[0],i[1],i[3],i[4],i[5],i[6],i[7],i[8]])
    return marks
for i in CAT1():
    print(i)



