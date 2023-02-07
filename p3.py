'''f=open("names.txt",'w+')
def names():
    n=int(input("Enter Number of Records: "))
    for i in range(n):
        fn=input("Enter First Name: ")
        ln=input("Enter Last Name: ")
        nm=(fn,ln)
        f.write(f"{nm}\n")

def check():
    last=input("Enter last name to check: ")
    names=f.readlines()
    for name in names:
        if name.strip().endswith(last):
            matchingnames=[name]
            print("Matching names: ")
            for name in matchingnames:
                print(name.strip())
        else:
            print("Not found")
names()
check()
'''
def store_names(n):
    with open("NAMES.TXT", "w") as file:
        for i in range(n):
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            file.write(first_name + " " + last_name + "\n")

def find_names(last_name):
    with open("NAMES.TXT", "r") as file:
        names = file.readlines()
        matching_names = [name for name in names if name.strip().endswith(last_name)]
        if len(matching_names) > 0:
            print("Matching names:")
            for name in matching_names:
                print(name.strip())
        else:
            print("NOT FOUND")

store_names(3)
last_name = input("Enter last name to search: ")
find_names(last_name)