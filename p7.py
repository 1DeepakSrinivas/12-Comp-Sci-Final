'''Create a binary file: cricket.dat, to store team name(KEY) and score (VALUE), of „n‟ teams ,
each in the form of a dictionary. Display the team name starting with the letter „I‟ if the score of
this team is the highest.'''

import pickle as p
f=open('cricket.dat','wb')
team={}
def create():
    n=int(input("Enter Number of Records: "))
    for i in range(n):
        key=str(input("Enter Team Name"))
        value=input("Enter Score: ")
        team[key]=value
        p.dump(team,f)

def disp():
    for teamn in team.keys():
        w=teamn.split()
        if w[0]=='I' or 'i': 
            print(teamn)

create()
disp()
