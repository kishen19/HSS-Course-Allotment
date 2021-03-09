from course import Course
from student import Student
from random import sample

class IAF:
    def __init__(self, courses: list, students: list):
        self.C = courses
        self.c2C = {c.code:c for c in self.C}
        self.S = students
        self.max_req = max([s.req for s in self.S])

    def run(self):
        for req_num in range(1,self.max_req+1):
            curr_C = [c for c in self.C if c.rem > 0]
            curr_S = [s for s in self.S if s.req >= req_num]
            while len(curr_S)>0 and len(curr_C)>0:
                self.allocate(curr_C,curr_S)
                curr_S = [s for s in curr_S if len(s.alloc)<req_num and s.itr<len(s.pref)]
                curr_C = [c for c in curr_C if c.rem>0]

    def allocate(self,C,S):
        curr_cc = {c.code for c in C}
        for s in S:
            while s.itr<len(s.pref) and ((s.pref[s.itr] not in curr_cc) or (s.pref[s.itr] in s.alloc)):
                s.itr+=1
            if s.itr<len(s.pref):
                self.c2C[s.pref[s.itr]].requests.append(s)
        
        for c in C:
            if len(c.requests) <= c.rem:
                for s in c.requests:
                    s.alloc.append(c.code)
                    c.students.append(s.roll)
                    s.itr = 0
                c.rem-=len(c.requests)
            else:
                w = self.break_ties(c.requests,c.rem)
                for s in w:
                    s.alloc.append(c.code)
                    c.students.append(s.roll)
                    s.itr = 0
                c.rem = 0
            c.requests = []

    def break_ties(self,l,num):
        return list(sample(l,num))