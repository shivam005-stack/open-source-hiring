def addition(x):
    return x+2

def multiply(y):
      return y*2 
      
numbers=addition(5)
product=multiply(7)
print(numbers)
print(product)

#Calling A Function

def greet():
    print("Good Morning")
    print("Welcome! New York Is Waiting For You With Open Arms")

greet()  

# BMI Calculator For Three Person's

def bmi_Calculator(name,height_m,weight_kg):
    bmi= weight_kg/(height_m**2)
    print(" bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " not overweight "
    else:
        return name + " is overweight"   

def add_numbers(n1,n2):
    result= n1+n2
    print(" Sum Of Two Numbers Are: ", result)  
number1=int(input(" Enter Value Of Number 1: "))
number2=int(input(" Enter Value Of Number 2: "))
add_numbers(number1,number2) 

marks= [55,80,11,9,100]
marks_sum= len(marks)
print(" Total Length" ,marks_sum)

total_marks= sum(marks)
print(" The Total Marks You Got Is : ", total_marks)

# Function To Find Average Marks
def find_average_marks(marks):
    sum_of_marks= sum(marks)
    total_subjects= len(marks)
    average_marks= sum_of_marks/total_subjects
    return average_marks

# Calculate The Grade 
def compute_grade(average_marks):
    if average_marks >=80:
        grade ='A'
    elif average_marks>=60:
        grade = 'B'
    elif average_marks>=50:
        grade='C'
    else:
        grade='F'
    return grade                

marks =[55,90,92,88,85]
average_marks= find_average_marks(marks)
print(" Your Average Marks Is: ", average_marks)  

grade= compute_grade(average_marks)
print(" Your Grade Is: ", grade)