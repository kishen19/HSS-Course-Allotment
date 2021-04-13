import matplotlib.pyplot as plt

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
    # plt.savefig("../insights/req_courses_vs_students_upscaled_5.png")
    plt.show()


    # Preference vs Students - One (best) course only
    fig = plt.figure(figsize = (15,7))
    max_req = max([s.req for s in students])
    pref_num = [str(i+1) for i in range(numc)]
    best_pref = [min([s.pref_list.index(u)+1 if u in s.pref_list else 50 for u in s.alloc]) for s in students]
    num_studs = [len([j for j in best_pref if j==i]) for i in range(1,numc+1)]
    plt.bar(pref_num,num_studs)
    plt.xlabel("Best Preference Allocated")
    plt.ylabel("Number of Students")
    plt.title("Best Preference Allocated v/s Number of Students")
    # plt.savefig("../insights/best_pref_vs_no_of_students_upscaled_5.png")
    plt.show()

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
    # plt.savefig("../insights/pref_allocated_vs_no_of_students_upscaled_5.png")
    plt.show()

    # Max Preference Allocated
    for j in range(numc-1,-1,-1):
        if num_studs[j]>0:
            print("Max Preference Allocated:",j+1)
            break
    # Allocated Students Data
    num0 = len([s for s in students if len(s.alloc)==0])
    # num1 = len([s for s in students if s.req==1])
    # num2 = len([s for s in students if s.req==2])
    # num3 = len([s for s in students if s.req==3])
    # num11 = len([s for s in students if s.req==1 and len(s.alloc)==1])
    # num22 = len([s for s in students if s.req==2 and len(s.alloc)==2])
    # num33 = len([s for s in students if s.req==3 and len(s.alloc)==3])
    # num12 = len([s for s in students if s.req==2 and len(s.alloc)==1])
    # num13 = len([s for s in students if s.req==3 and len(s.alloc)==1])
    # num23 = len([s for s in students if s.req==3 and len(s.alloc)==2])
    ## 0 courses
    print("Students who got 0 courses:", num0,"of",nums,"students")
    # ## 1 of 1
    # print("Students who got 1 of 1 courses required:", num11,"of",num1,"students")
    # ## 2 of 2
    # print("Students who got 2 of 2 courses required:", num22,"of",num2,"students")
    # ## 3 of 3
    # print("Students who got 3 of 3 courses required:", num33,"of",num3,"students")
    # ## 1 of 2
    # print("Students who got 1 of 2 courses required:", num12,"of",num2,"students")
    # ## 1 of 3
    # print("Students who got 1 of 3 courses required:", num13,"of",num3,"students")
    # ## 2 of 3
    # print("Students who got 2 of 3 courses required:", num23,"of",num3,"students")