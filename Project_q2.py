"""

Brilliant School conducts an exam in subjects of English, Science and Mathematics.
Science exam is split up as Science Theory and Science Practical
The maximum marks for each subject is as follows : 
          -- English : 75 marks
          -- Science Theory : 75 marks
          -- Science Practical : 25 marks
          -- Science = Science Theory + Science Practical : 100 marks
          -- Mathematics : 100 marks

The pass marks for each subject is as follows :
          -- Pass marks for English : 25
          -- Pass marks for Science Theory : 25
          -- Pass marks for Science Practical : 8
          -- Pass marks for Science : 35
          -- Pass marks for Mathematics : 35

Write a Python program to collect the marks scored by a student in all the above 4 exams
Based on the marks scored by the student, grade them according to the following criteria :
          -- Grade A : if Total > 90%
          -- Grade B : if Total > 75%
          -- Fail is any score is less than pass marks
          -- Average otherwise
                 """
def rank(percentage):

    if (percentage >=90):
        print("student got first class")
    elif(percentage >=75 or percentage <90):
        print("student has got second class")
    elif(percentage >=35 or percentage < 75):
        print("student has got average class")
    else:
        print("student got failed")

def calculate_percentage(total_student_marks,max_marks):

    percentage=((total_student_marks/max_marks)*100)

    return percentage

def student_marks():

    eng_marks=int(input("enter the english marks:"))
    science_pra=int(input("enter the science practicle marks:"))
    science_theory=int(input("enter the science theory marks:"))
    maths_marks=int(input("enter the maths marks:"))

    total=eng_marks+science_pra+science_theory+maths_marks

    return total,eng_marks,science_pra,science_theory,maths_marks

def check_PassOrFail(eng_marks,science_pra,science_theory,maths_marks,percentage):

    if (eng_marks>=25 and science_pra>=8 and science_theory>=25 and maths_marks>=35):

        rank(percentage)

    else:

        print("student got failed")

    
# main Starts from here
total_student_marks,eng_marks,science_pra,science_theory,maths_marks=student_marks()
english_max_marks=75
science_max_practicle=75
science_max_theory=25
maths_max_marks=100

max_marks=english_max_marks+science_max_practicle+science_max_theory+maths_max_marks

percentage=calculate_percentage(total_student_marks,max_marks)

check_PassOrFail(eng_marks,science_pra,science_theory,maths_marks,percentage)
