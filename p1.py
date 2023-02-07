import mysql.connector as m
con=m.connect(host='localhost',database='deepak_12d',passwd='1105',user='root')
cur=con.cursor()

def tab():
    c1="CREATE TABLE PATIENT('No' INT PRIMARY KEY,'Name' VARCHAR(20), 'Age' INT, 'Dateofadmin' DATE, 'Charge' INT)"
    cur.execute(c1)

def data_ent():
    n=int(input("Enter Number of Entries: "))
    for i in range(n):
        no=1
        name=input("Enter Name of Patient: ")
        age=input("Enter age of Patient: ")
        dep=input("Enter Department: ")
        date=input("Enter Date (dd/mm/yy): ")
        charge=input("Enter Charge: ")
        no+=1
        c2=(f"INSERT INTO PATIENT VALUES({no},{name},{age},{dept},{date},{charge}")
        cur.execute(c2)

