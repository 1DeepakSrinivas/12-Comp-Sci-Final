n=int(input("Enter Number of records: "))        
def stud(n):
    students = []
    for i in range(n):
        name = input("Enter student name: ")
        avg_marks = float(input("Enter average marks: "))
        employment = input("Is student employed? (y/n): ")
        employment = True if employment == "y" else False
        students.append([name, avg_marks, employment])
    return students

employed = [student for student in students if student[2] == True]
unemployed = [student for student in students if student[2] == False]
print(f"Employed students: {len(employed)}")
print(f"Unemployed students: {len(unemployed)}")


highest_scorer = max(students, key=lambda x: x[1])
print(f"Highest scorer: {highest_scorer[0]} with marks {highest_scorer[1]}")

def stud(n):
    students = []
    for i in range(n):
        name = input("Enter student name: ")
        avg_marks = float(input("Enter average marks: "))
        employment = input("Is student employed? (y/n): ")
        employment = True if employment == "y" else False
        students.append([name, avg_marks, employment])
    return students