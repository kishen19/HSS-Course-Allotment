from collections import defaultdict
from input import input_generator

'''
Input: Graph G(C U S), X, P, q
S -> Students (set)
C -> Courses (set)
s: indentifier: Roll no. (integer)
c: indentifier: course code (string) 
X(s) -> Subset of courses that student s can take -> dictionary, key: s, value: list of courses
Ps(s) -> Preference order of student s (strict) -> dictionary, key: s, value: list of courses, in decreasing order
Pc(c) -> Preference order for course c (strict) -> dictionary, key: c, value: list of students, in decreasing order
        [4th > 3rd > 2nd > 1st, bigger roll no.]
q(c) -> capacity of course c (cap) -> dictionary, key: c, value: int (default 40)

Output: A pareto-optimal matching M -> dictionary, key: s, value: list of courses allocated
M(s) set of allocated courses of student s.

In the algorithm:
r(c) -> residual capacity of course c
R(s) -> remaining preference order of student s
'''

def IAF(S, C, X, Ps, Pc, q):
    '''
    Input:
    S: set (roll no.)
    C: set (course code)
    Ps: dict -> key: s, value: list of courses (non-empty)
    Pc: dict -> key: c, value: list of students (non-empty)
    q: dict -> key: c, value: int > 0 (cap)
    
    Output: Matching M (key: s, value: list of courses allocated)
    '''
    r = {c: q[c] for c in C}
    M = {s:[] for s in S}
    R = {s: Ps[s] for s in S}
    R.update({c:Pc[c] for c in C})
    rems = len(S)
    remc = len(C)
    while rems:
        Mi = solve(S, C, R, r) # Dictionary -> s: course allocated, -1 otherwise
        full_courses = set()
        for s in Mi:
            if Mi[s]!=-1:
                c = Mi[s]
                r[c] -= 1
                if r[c]==0:
                    full_courses.add(c)
                    del R[c]
                    C.discard(c)
                    remc-=1
        for s in Mi:
            c = Mi[s]
            if c!=-1:
                M[s].append(c)
                if c not in full_courses:
                    R[c].remove(s)
                R[s].remove(c)
            for c1 in full_courses:
                try:
                    R[s].remove(c1)
                except:
                    pass
            if len(R[s])==0:
                del R[s]
                S.discard(s)
                rems-=1
    return M


def solve(S, C, R, r):
    '''
    Input:
    S: set (roll no.)
    C: set (course code)
    R: dict -> key: s, value: list of courses (non-empty)
               key: c, value: list of students (non-empty)
    r: dict -> key: c, value: int > 0 (cap)
    
    Output: Matching M (key: s, value: course code or -1)
    '''
    curr_a = defaultdict(list)
    M = {s:-1 for s in S}
    for s in S:
        curr_a[R[s][0]].append([R[R[s][0]].index(s),s])
    
    for c in C:
        curr_a[c].sort()
        for i in range(min(len(curr_a[c]), r[c])):
            M[curr_a[c][i][1]] = c
    return M

def main():
    S,C,X,Ps,Pc,q = input_generator()
    M = IAF(S,C,X,Ps,Pc,q)
    print("Courses Allocation")
    print("-"*30)
    d = {c:[s for s in M if c in M[s]] for c in C}
    for c in C:
        if len(d[c])==0:
            print("Course ",c," **No Student Registered**")
        else:
            print("Course "+c+": Students Registered:",len(d[c]))
    print("-"*30)
    print("No. of students who were not allocated any course:",len([s for s in M if len(M[s])==0]))




if __name__=='__main__':
    main()