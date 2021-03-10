class Course:
    def __init__(self,code: str, name: str, cap: int):
        self.code = code
        self.name = name if name else ''
        self.cap = cap
        self.students = []
        # Private vars
        self.rem = cap
        self.requests = []

    def __str__(self):
        return self.code + " " +self.name + "\nNo. of Allocated Students: "+ str(len(self.students)) +"\nAllocated Students: "+" ".join([str(i) for i in self.students])