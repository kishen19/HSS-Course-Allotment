'''
Code to create synthetic data for testing

Note: Modify as per requirement

'''

import random
from collections import defaultdict
import pandas as pd

def shuffler(l):
    random.shuffle(l)
    return l

def input_generator(c):
    C = ['HS'+"0"*(3-len(str(i+1)))+str(i+1) for i in range(c)]
    n = 250 # no. of students
    S = [17110001+i for i in range(n)]+[18110001+i for i in range(n)]+[19110001+i for i in range(n)]+[20110001+i for i in range(n)]
    S_prefs = {i:shuffler(random.sample(C,random.randint(1,c))) for i in S}
    S_req = {i:random.randint(1,3) for i in S}
    for i in S_prefs:
        for j in C:
            if j not in S_prefs[i]:
                S_prefs[i].append(j)
    l = []
    for i in S:
        l.append([i," ",S_req[i]]+S_prefs[i])
    df1 = pd.DataFrame(l,columns = ["Student Roll Number","Student Name", "No. of Courses Required"]+["Pref "+str(i+1) for i in range(c)])
    df1.to_csv("students_data.csv")
    q = {}
    l1 = []
    for i in C:
        q[i] = 40
        l1.append([i," ",q[i]])
    df2 = pd.DataFrame(l1,columns = ["Course Code", "Course Name", "Course Cap"])
    df2.to_csv("courses_data.csv")

    return C,q,S,S_prefs,S_req

input_generator(30)