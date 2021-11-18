n=input(" nbr of students? ")
names=[]
grades=[]
for i in range (0,int(n)):
    name=input("enter the name: ")
    names.append(name)
    grade=("enter the grade : ")
    grades.append(grade)
for j in range(0,int(n)):
    print(names[j],"\t", grades[j])
    
print('hello world')

