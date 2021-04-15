from random import sample
from tqdm import tqdm

class IAF:
    def __init__(self, courses: list, students: list):
        self.C = courses
        self.c2C = {c.code:c for c in self.C}
        self.S = students
        self.max_req = max([s.req for s in self.S])
        self.total_allocations = 0
        self.total_required_allocations = sum([s.req for s in self.S])
        self.student_slots = {s.roll:set() for s in students}

    def run(self):
        for req_num in tqdm(range(1,self.max_req+1)):
            curr_C = [c for c in self.C if c.rem > 0]
            curr_S = [s for s in self.S if s.req >= req_num]
            while len(curr_S)>0 and len(curr_C)>0:
                self.allocate(curr_C,curr_S,req_num)
                curr_C = [c for c in curr_C if c.rem>0]
                curr_S = [s for s in curr_S if s.latest_itr<req_num and self.check_availability(s,curr_C)]
    
    def check_availability(self,student, courses):
        for c in courses:
            if (c.code in student.pref_list) and (c.code not in student.alloc) and (not self.check_clashes(student,c)):
                return 1
        return 0
    
    def check_clashes(self, s, c):
        clashing = 0
        if c.lecture_slots:
            for slot in c.lecture_slots:
                if slot in self.student_slots[s.roll] or slot[0] in self.student_slots[s.roll]:
                    clashing = 1
                    break 
        if c.tutorial_slots:
            for slot in c.tutorial_slots:
                if slot in self.student_slots[s.roll] or slot[0] in self.student_slots[s.roll]:
                    clashing = 1
                    break 
        return clashing

    def allocate(self,C,S,req_num):
        curr_cc = {c.code for c in C}
        for s in S:
            for code in s.pref_list:
                if (code in curr_cc) and (code not in s.alloc) and (not self.check_clashes(s,self.c2C[code])):
                    self.c2C[code].requests.append(s)
                    break
        for c in C:
            if len(c.requests) <= c.rem:
                for s in c.requests:
                    s.alloc.append(c.code)
                    c.students.append(s.roll)
                    s.latest_itr = req_num
                    self.total_allocations += 1
                    if c.lecture_slots:
                        self.student_slots[s.roll] |= set(c.lecture_slots)
                    if c.tutorial_slots: 
                        self.student_slots[s.roll] |= set(c.lecture_slots)
                c.rem-=len(c.requests)
            else:
                w = self.break_ties(c.requests,c.rem)
                for s in w:
                    s.alloc.append(c.code)
                    c.students.append(s.roll)
                    s.latest_itr = req_num
                    self.total_allocations += 1
                    if c.lecture_slots:
                        self.student_slots[s.roll] |= set(c.lecture_slots)
                    if c.tutorial_slots: 
                        self.student_slots[s.roll] |= set(c.lecture_slots)
                c.rem = 0
            c.requests = []

    def break_ties(self,l,num):
        return list(sample(l,num))