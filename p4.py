#Create a python program to write „n‟ lines into the text file: sample.txt. Create another
#text file :new.txt, by deleting the words “a”, “the”,”an”

def write():
    n=(int(input("Enter Number of lines: ")))
    with open("sample.txt",'w') as file:
        for i in range(n):
            str=input(f"Enter Line {i}: ")
            file.write(str+'\n')
    
def new():
    with open("sample.txt",'w') as file1:
        with open('new.txt','w+') as file2:
            lines=file1.readlines()
            for line in lines:
                for word in line:
                    if word.lower()=='a' or 'an' or 'the':
                        lines.pop(word)
                        file2.write(line+'\n')

write()
new()