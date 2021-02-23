import random
from collections import defaultdict
def input_generator():
    C = set(['HS'+"0"*(3-len(str(i+1)))+str(i+1) for i in range(25)])
    # {'HS211','HS319','HS510','HS007','MS503','HS212','HS339','HS514','HS607','MS511','HS523','HS427','HS515','HS997'}
    n = 50 # no. of students
    S = set([17110001+i for i in range(n)]+[18110001+i for i in range(n)]+[19110001+i for i in range(n)]+[20110001+i for i in range(n)])
    X = dict()
    Ps = dict()
    Pc = defaultdict(list)
    pref_map = {}
    for i in S:
        k = 3 # no. of courses per student that he can take
        X[i] = random.sample(C,k)
        Ps[i] = random.sample(X[i],random.randint(1,k))
        random.shuffle(Ps[i])
    for i in Ps:
        for j in Ps[i]:
            Pc[j].append(i)
    for i in Pc:
        Pc[i].sort()
    q = {}
    for i in C:
        q[i] = 25
    return S,C,X,Ps,Pc,q