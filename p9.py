stk=[]
top=None
def push():
    language = input("Enter language name: ")
    region = input("Enter region name: ")
    lst=[region,language]
    global top
    stk.append(lst)
    top=-1

def pop():
    if stk==[]:
        print("Underflow. Stack is empty.")
    else:
        if len(stk)==1:
            top=None
            x=stk.pop()
            return x

def display():
    if stk==[]:
        print("Underflow. Stack is empty.")
    for i in range(top,-len(stk-1,1)):
        print(stk[i],'->')