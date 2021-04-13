class Student:
    def __init__(self, roll_num: int, name: str, programme: str, minors: str, req: int, num_pref:int, pref_list: list):
        self.roll = roll_num
        self.name = name if name else ''
        self.programme = programme
        self.num_pref = num_pref
        self.pref_list = pref_list
        self.req = req
        self.alloc = []
        # Private vars
        self.latest_itr = 0

    def __str__(self):
        pass