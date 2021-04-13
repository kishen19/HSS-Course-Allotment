from random import sample, shuffle
from tqdm import tqdm

def check(student, courses):
    for c in courses:
        if (c.code in student.pref_list) and (c.code not in student.alloc):
            return 1
    return 0

class IAF:
    def __init__(self, courses: list, students: list):
        self.C = courses
        self.c2C = {c.code:c for c in self.C}
        self.S = students
        self.max_req = max([s.req for s in self.S])
        self.total_allocations = 0
        self.total_required_allocations = sum([s.req for s in self.S])

    def run(self):
        for req_num in tqdm(range(1,self.max_req+1)):
            curr_C = [c for c in self.C if c.rem > 0]
            curr_S = [s for s in self.S if s.req >= req_num]
            while len(curr_S)>0 and len(curr_C)>0:
                self.allocate(curr_C,curr_S,req_num)
                curr_C = [c for c in curr_C if c.rem>0]
                curr_S = [s for s in curr_S if s.latest_itr<req_num and check(s,curr_C)]

    def allocate(self,C,S,req_num):
        curr_cc = {c.code for c in C}
        for s in S:
            for code in s.pref_list:
                if (code in curr_cc) and (code not in s.alloc):
                    self.c2C[code].requests.append(s)
                    break
        for c in C:
            if len(c.requests) <= c.rem:
                for s in c.requests:
                    s.alloc.append(c.code)
                    c.students.append(s.roll)
                    s.latest_itr = req_num
                    self.total_allocations += 1
                c.rem-=len(c.requests)
            else:
                w = self.break_ties(c.requests,c.rem)
                for s in w:
                    s.alloc.append(c.code)
                    c.students.append(s.roll)
                    s.latest_itr = req_num
                    self.total_allocations += 1
                c.rem = 0
            c.requests = []

    def break_ties(self,l,num):
        return list(sample(l,num))