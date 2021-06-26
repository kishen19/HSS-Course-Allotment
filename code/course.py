''''
Course Object

'''
class Course:
    def __init__(self,code: str, name: str, cap: int, lecture_slots: list, tutorial_slots: list):
        self.code = code
        # Course code, ex: HS 151, dtype: (string)
        self.name = name if name else ''
        # Name of the course, ex: World Civilization, dtype: (string)
        self.cap = cap
        # Course cap, ex: 40, dtype: (int)
        self.students = []
        # Roll numbers of the students who will be alloted this course after allocation, ex: [17110090, 17110074, ....], dtype: (list of int)
        self.lecture_slots = lecture_slots
        # Lecture slots for this course, ex: ['C1' , 'A'], dtype: (list of strings)
        self.tutorial_slots = tutorial_slots
        # Tutorial slots for this course, ex: ['C2', 'B2'], dtype: (list of strings)

        # Private vars only used during allocation by the main func
        self.rem = cap
        # Remaining seats for this course: to keep track during allocation, ex: 31, dtype: (int) 
        self.requests = []
        # Roll numbers of the students who filled this course in their preferences, ex: [17110090, 17110074, ....], dtype: (list of int) 

    # Printing a Course Object
    def __str__(self):
        return self.code + " " +self.name + "\nNo. of Allocated Students: "+ str(len(self.students)) +"\nAllocated Students: "+" ".join([str(i) for i in self.students])
