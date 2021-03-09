from input import input_generator
from course import Course
from student import Student
from iaf import IAF
import pandas as pd


def get_input():
    studs = pd.read_csv("students_data.csv")
    cours = pd.read_csv("courses_data.csv")
    courses = [Course(i["Course Code"],i["Course Name"],int(i["Course Cap"])) for ind,i in cours.iterrows()]
    students = [Student(int(i["Student Roll Number"]),i["Student Name"],[i["Pref "+str(j+1)] for j in range(30)],int(i["No. of Courses Required"])) for ind,i in studs.iterrows()]
    return courses, students


def main():
    courses,students = get_input()
    solver = IAF(courses,students)
    solver.run()
    print("HSS Course Allocation")
    print("-"*30)
    for c in courses:
        print(c)
        print()
    print("-"*30)
    # Testing Output
    for s in students:
        if len(s.alloc)<s.req:
            print(s.roll,str(len(s.alloc))+'/'+str(s.req),"courses alloted")
    for s in students:
        if len(s.alloc)==3:
            print(s.roll,str(len(s.alloc))+'/'+str(s.req),"courses alloted")

if __name__=='__main__':
    main()