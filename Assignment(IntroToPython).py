#Question1
num1=int(input("enter first number"))
num2=int(input("enter second number"))
num3=int(input("enter third number"))
avg=(num1+num2+num3)/3
print("average is ",avg)


#Question2
std_deduction=10000
dep_deduction=3000
g_income=float(input("Enter the gross income:"))    
dependents=int(input("Enter the no of dependents:"))
tax_income=float(g_income - std_deduction - (dep_deduction*dependents))
tax=tax_income*0.2
print("The person's income tax is:")
print(float(tax))


#Question3
Name=("Karan NANDA")
SID=21105054
Gender= 'M'
Course=("Electronic and Communication Engineering")
CGPA='9.2'
Student=[Name,SID,Gender,Course,CGPA]
print (Student)


#Question4
print("marks of 5 students are ")
Marks=[15,45,43,72,65]
print("Marke before sorting:",Marks)
Marks.sort()
print("Marks after sorting",Marks)


#Question5A
color=['red','green','white','black','green','yellow']
print ("Colors before listing are ",color)
color.pop(3)
print ("colors after listing ", color)


#Question5B
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print (color)
color[3:5]=['Purple']
print ("colors after listing are",color) 
