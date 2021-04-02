import pandas as pd
from course import Course
from student import Student
from iaf import IAF
from insights import insights

def get_courseid(s):
    s1 = s[:6]
    for i in range(6,len(s)-1):
        if s[i]==" ":
            break
        else:
            s1+=s[i]
    return s1

def get_input():
    cours = pd.read_excel("./courses_data/courses_2020_21.xlsx")
    courses = [Course(i["Course Code"],i["Course Name"],int(i["Course Cap"])//3) for ind,i in cours.iterrows()]
    studs = pd.read_excel("./students_data/mock_data.xlsx")
    students_data = {}
    for ind,i in studs.iterrows():
        if ((i["Roll Number"] in students_data and students_data[i["Roll Number"]][0]<i["Timestamp"]) or (i["Roll Number"] not in students_data)):
            students_data[i["Roll Number"]] = [
                i["Timestamp"],
                i["Programme"],
                i["Minors"].strip(",").strip(),
                int(i["Roll Number"]),
                i["Name"],
                min(int(i["Number of courses to register"]),int(i["Number of Preferences"])),
                int(i["Number of Preferences"]),
                [get_courseid(i["Preference #"+str(j+1)].strip()) for j in range(int(i["Number of Preferences"]))],
                int(i["Number of least preferences"]),
                [get_courseid(i["Course #"+str(j+1)].strip()) for j in range(int(i["Number of least preferences"]))]
            ]
            students_data[i["Roll Number"]][7],students_data[i["Roll Number"]][9] = students_data[i["Roll Number"]][7],students_data[i["Roll Number"]][9]
    students = [Student(roll_num= students_data[i][3], name= students_data[i][4], programme= students_data[i][1], minors= students_data[i][2], req= students_data[i][5], num_pref= students_data[i][6], pref_list= students_data[i][7], num_excl= students_data[i][8], excl_list= students_data[i][9]) for i in students_data]
    return courses, students

def write_output(courses,students):
    max_req = max([s.req for s in students])
    df1 = pd.DataFrame([[s.roll,s.name]+s.alloc+['' for _ in range(max_req-len(s.alloc))] for s in students], columns=["Student Roll Number","Student Name"]+["Allocated Course "+str(i+1) for i in range(max_req)])
    df2 = pd.DataFrame([[c.code,c.name,c.cap,", ".join([str(roll) for roll in c.students])] for c in courses], columns=["Course Code","Course Name", "Course Cap","Allocated Students"])
    df1.to_csv("./output/Mock-Students Allocation.csv")
    df2.to_csv("./output/Mock-Courses Allocation.csv")


def main():
    courses,students = get_input()
    solver = IAF(courses,students)
    solver.run()
    write_output(courses,students)
    insights(courses,students)


if __name__=='__main__':
    main()