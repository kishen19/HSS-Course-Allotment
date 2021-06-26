'''
Student Object

'''

class Student:
    def __init__(self, roll_num: int, name: str, programme: str, req: int, num_pref:int, pref_list: list):
        self.roll = roll_num
        # Roll no. of the student, ex: 17110090, dtype: (int)
        self.name = name if name else ''
        # Name of the student, ex: "Karthikeya", dtype: (string)
        self.programme = programme
        # Programme of the student, ex: "B.Tech", dtype: (string)
        self.num_pref = num_pref
        # No of preferrences the student filled, ex: 2, dtype: (int)
        self.pref_list = pref_list
        # Preference list of the student: list of course codes with highest priority first, ex: ['HS 151', 'HS 302'], dtype: (list of strings)
        self.req = req
        # No. of courses student wants to do, ex: 1, dtype: (int)
        self.alloc = []
        # The list of course codes which have been alloted to this student, ex: ['HS 302'], dtype: (list of strings)
        
        # Private vars
        self.latest_itr = 0
        # Last iteration in which the student got a course: used by the algo while allocating, ex: 2, dtype: (int)
    
    def __str__(self):
        pass