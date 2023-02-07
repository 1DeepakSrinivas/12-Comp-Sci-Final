import csv as c
import random
def q1():
    f=open('marks.csv','w+',newline="")
    reader=c.reader(f)
    writer = c.writer(f)
    r1=["Candidate Name", "Test 1", "Test 2", "Test 3", "Test 4", "Average", "Selected"]
    writer.writerow(r1)

    n=int(input("Number of entries: "))
    for i in range(n):
        name=input("Enter Name of Candidate: ")
        t1=random.randint(0,50)
        t2=random.randint(0,50)
        t3=random.randint(0,50)
        t4=random.randint(0,50)
        avg=((t1+t2+t3+t4)/4)
        if avg>=25:
            s=1
        else:
            s=0
        r=(name,t1,t2,t3,avg,s)
        writer.writerow(r)

def qread():
    f=open('marks.csv','r',newline="")
    reader=c.reader(f)
    selected_count=[]
    for line in reader:
        if line[5]==str(1):
            selected_count.append(line[0])
        else:
            print("No one qualified")
    print("Selected Candidates:", selected_count)   
q1()
qread()