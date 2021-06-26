'''
Analysis on the course allocation

Note: You can add/modify as per requirement
'''

import matplotlib.pyplot as plt
import yaml


###################################################################################################
# reading config file for fetching paths
paths = open("../config.yaml", 'r')
paths_dictionary = yaml.load(paths)

# Path where the insight plots are to be stored
INSIGHTS_PATH = "./insights"

def insights(courses,students):
    nums = len(students)
    numc = len(courses)
    print("Number of Students:",nums,"Number of Course:",numc)
    print()

    # Req Courses vs Percentage
    fig = plt.figure(figsize = (15,7))
    max_req = max([s.req for s in students])
    req_num = [str(i+1) for i in range(max_req)]
    num_studs = [len([s for s in students if s.req==i]) for i in range(1,max_req+1)]
    plt.bar(req_num,num_studs)
    plt.xlabel("Number of Required Courses")
    plt.ylabel("Number of Students")
    plt.title("Number of Required Courses v/s Number of Students")
    plt.savefig(INSIGHTS_PATH + "/req_courses_vs_students.png")
    # plt.show()

    # Preference vs Students - One (best) course only
    fig = plt.figure(figsize = (15,7))
    max_req = max([s.req for s in students])
    pref_num = [str(i+1) for i in range(numc)]
    best_pref = [min([s.pref_list.index(u)+1 if u in s.pref_list else 50 for u in s.alloc]) if len(s.alloc)>0 else 0 for s in students]
    num_studs = [len([j for j in best_pref if j==i]) for i in range(1,numc+1)]
    plt.bar(pref_num,num_studs)
    plt.xlabel("Best Preference Allocated")
    plt.ylabel("Number of Students")
    plt.title("Best Preference Allocated v/s Number of Students")
    plt.savefig(INSIGHTS_PATH + "/best_pref_vs_no_of_students.png")
    # plt.show()

    # Preference vs Students - One (best) course only
    fig = plt.figure(figsize = (15,7))
    max_req = max([s.req for s in students])
    pref_num = [str(i+1) for i in range(numc)]
    num_studs = [0]*numc
    for s in students:
        for j in s.alloc:
            if j in s.pref_list:
                num_studs[s.pref_list.index(j)]+=1
    plt.bar(pref_num,num_studs)
    plt.xlabel("Preferences Allocated")
    plt.ylabel("Number of Students")
    plt.title("Preferences Allocated v/s Number of Students")
    plt.savefig(INSIGHTS_PATH + "/pref_allocated_vs_no_of_students.png")
    # plt.show()

    # Max Preference Allocated
    for j in range(numc-1,-1,-1):
        if num_studs[j]>0:
            print("Max Preference Allocated:",j+1)
            break
    # Allocated Students Data
    num0 = len([s for s in students if len(s.alloc)==0])
    num1 = len([s for s in students if s.req==1])
    num2 = len([s for s in students if s.req==2])
    num11 = len([s for s in students if s.req==1 and len(s.alloc)==1])
    num22 = len([s for s in students if s.req==2 and len(s.alloc)==2])
    num12 = len([s for s in students if s.req==2 and len(s.alloc)==1])
    ## 0 courses
    print("Students who got 0 courses:", num0,"of",nums,"students")
    # ## 1 of 1
    print("Students who got 1 of 1 courses required:", num11,"of",num1,"students")
    # ## 2 of 2
    print("Students who got 2 of 2 courses required:", num22,"of",num2,"students")
    # ## 1 of 2
    print("Students who got 1 of 2 courses required:", num12,"of",num2,"students")

    course_num_studs = {c.code:[0,c.cap,len(c.students)] for c in courses}
    for s in students:
        for c in s.pref_list:
            course_num_studs[c][0]+=1
    for c in course_num_studs:
        print(c,"Num of requests:",course_num_studs[c][0], "Cap:",course_num_studs[c][1],"Num of allocated:",course_num_studs[c][2])
    
    # Requirement vs Preferences - Students who didnt get any course
    fig = plt.figure(figsize = (15,7))
    max_pref = max([s.num_pref for s in students])
    pref = [i for i in range(1,max_pref+1)]
    num_pref1 = [0 for i in range(max_pref)]
    num_pref2 = [0 for i in range(max_pref)]
    for s in students:
        if len(s.alloc)==0:
            if s.req==1:
                num_pref1[s.num_pref-1]+=1
            else:
                num_pref2[s.num_pref-1]+=1
    plt.bar(pref,num_pref1)
    plt.xlabel("Number of Preferences")
    plt.ylabel("Number of Students")
    plt.title("Number of Preferences v/s Number of Students (who didn't get any course, req: 1)")
    plt.savefig(INSIGHTS_PATH + "/num_pref1_vs_no_of_students.png")
    # plt.show()
    fig = plt.figure(figsize = (15,7))
    plt.bar(pref,num_pref2)
    plt.xlabel("Number of Preferences")
    plt.ylabel("Number of Students")
    plt.title("Number of Preferences v/s Number of Students (who didn't get any course, req: 2)")
    plt.savefig(INSIGHTS_PATH + "/num_pref2_vs_no_of_students.png")
    # plt.show()

    fig = plt.figure(figsize = (15,7))
    progs = ["B.Tech", "M.Tech", "MSc", "MA", "PhD"]
    num_studs = {p:0 for p in progs}
    for s in students:
        if len(s.alloc)==0:
            num_studs[s.programme]+=1
    plt.bar(progs,[num_studs[p] for p in progs])
    plt.xlabel("Programme")
    plt.ylabel("Number of Students")
    plt.title("Programme v/s Number of Students (who didn't get any course)")
    plt.savefig(INSIGHTS_PATH + "/prog_vs_no_of_students.png")
    # plt.show()

    # Per Course Insights
    fig = plt.figure(figsize = (10,15))
    course_codes = [c.code for c in courses]
    course_names = {c.code:c.code for c in courses}
    num_studs = {c.code:0 for c in courses}
    for s in students:
        num_studs[s.pref_list[0]]+=1
    plt.bar([course_names[cd] for cd in course_codes],[num_studs[cd] for cd in course_codes])
    plt.xlabel("Course")
    plt.ylabel("Number of Students")
    plt.title("Courses v/s Number of Students who filled as first pref")
    plt.xticks(rotation=90)
    plt.savefig(INSIGHTS_PATH + "/course_vs_no_of_students_pref1.png")
    
    # plt.show()