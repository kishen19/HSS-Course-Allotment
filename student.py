class Student:
    def __init__(self, roll_num: int, name: str, pref: list, req: int):
        self.roll = roll_num
        self.name = name if name else ''
        self.pref = pref
        self.req = req
        self.alloc = []
        # Private vars
        self.itr = 0

    def __str__(self):
        pass