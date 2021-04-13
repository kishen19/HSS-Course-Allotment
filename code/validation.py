from collections import defaultdict
def validation(students,courses):
    coures_codes = {c.code for c in courses}
    course_studentroll_map = {c.code:sorted(c.students) for c in courses}
    student_rolls = {stud.roll for stud in students}
    course_caps_allocated = defaultdict(list)

    # students side
    for stud in students:
        if len(stud.alloc)!=len(set(stud.alloc)):
            raise Exception("Same course is allocated more than once for the student "+str(stud.name)+"-"+str(stud.roll))
        if len(stud.alloc)>stud.req:
            raise Exception("Student "+str(stud.name)+"-"+str(stud.roll)+" was allocated courses more than his requirement")
        pref_set = set(stud.pref_list)
        for course_code in stud.alloc:
            if course_code not in coures_codes:
                raise Exception("Course code allocated is not valid")
            if course_code not in pref_set:
                raise Exception("Course allocated to the student "+str(stud.name)+"-"+str(stud.roll)+" is not in his preference list")
            course_caps_allocated[course_code].append(stud.roll)

    # cross validation
    for i in course_caps_allocated:
        course_caps_allocated[i] = sorted(course_caps_allocated[i])
    if course_caps_allocated!=course_studentroll_map:
        raise Exception("Cross validation failed")
    
    # course side
    for cours in courses:
        if len(cours.students)!=len(set(cours.students)):
            raise Exception("Same student was allocated to the course "+str(cours.code)+" more than once") 
        for stud_roll in cours.students:
            if stud_roll not in student_rolls:
                raise Exception("The student allocated for the course "+str(cours.code)+" is invalid")
        if len(cours.students)>cours.cap:
            raise Exception("Allocation exceeded the course cap for the course "+str(i))
    print("Yay! everything is fine.")
    return True            
