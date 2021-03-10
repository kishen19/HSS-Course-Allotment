import pandas as pd
from course import Course
from student import Student
from iaf import IAF
from insights import insights


def get_input():
    studs = pd.read_csv("students_data.csv")
    cours = pd.read_csv("courses_data.csv")
    courses = [Course(i["Course Code"],i["Course Name"],int(i["Course Cap"])) for ind,i in cours.iterrows()]
    students = [Student(int(i["Student Roll Number"]),i["Student Name"],[i["Pref "+str(j+1)] for j in range(30)],int(i["No. of Courses Required"])) for ind,i in studs.iterrows()]
    return courses, students

def write_output(courses,students):
    max_req = max([s.req for s in students])
    df1 = pd.DataFrame([[s.roll,s.name]+s.alloc+['' for _ in range(max_req-len(s.alloc))] for s in students], columns=["Student Roll Number","Student Name"]+["Allocated Course "+str(i+1) for i in range(max_req)])
    df2 = pd.DataFrame([[c.code,c.name,c.cap,", ".join([str(roll) for roll in c.students])] for c in courses], columns=["Course Code","Course Name", "Course Cap","Allocated Students"])
    df1.to_csv("Students Allocation.csv")
    df2.to_csv("Courses Allocation.csv")


def main():
    courses,students = get_input()
    solver = IAF(courses,students)
    solver.run()
    write_output(courses,students)
    insights(courses,students)


if __name__=='__main__':
    main()