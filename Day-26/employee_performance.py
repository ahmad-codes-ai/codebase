class Review:
    def __init__(self,q,scores):
        self.q = q
        self.scores = scores

    def average_score(self):
        l = len(self.scores)
        s = 0
        for k,v in self.scores.items():
            s+=v
        if s > 0:
            avg = s/l
            return avg
        else:
            return 0

class Employee:
    def __init__(self,name):
        self.__name = name
        self.__reviews = []

    def add_review(self,rev):
        self.__reviews.append(rev)

    def get_average_score(self):
        l = len(self.__reviews)
        s = 0
        for i in self.__reviews:
            s+=i.average_score()
        if s > 0:
            return s/l
        else:
            return 0

    def last_two_average(self):
        if len(self.__reviews) >= 2:
            last = self.__reviews[-1]
            second_l = self.__reviews[-2]
            avg = (last.average_score() + second_l.average_score()) /2.0
            return avg
        else:
            return 0

    def is_eligible(self,promotion_threshold=None):
        if promotion_threshold is None:
            promotion_threshold = 4.0
        if self.last_two_average() >= promotion_threshold:
            return True
        else:
            return False

class Department():

    DEFAULT_PROMOTION_THRESHOLD = 4.0

    def __init__(self):
        self.__employees = []

    def add_employee(self,emp):
        if emp not in self.__employees:
            self.__employees.append(emp)
            return "Emp added in department successfully"
        else:
            return "Emp already in department"

    def department_average(self):
        l = len(self.__employees)
        s = 0
        for i in self.__employees:
            s+=i.get_average_score()
        if s > 0:
            return s/l
        else:
            return 0

    def eligible_employees(self,threshold=None):
        if threshold is None:
            threshold = Department.DEFAULT_PROMOTION_THRESHOLD
        eligible = []
        for i in self.__employees:
            if i.is_eligible(threshold):
                eligible.append(i)
        return eligible

emp = Employee("Sara")
emp.add_review(Review("Q1", {"Tech": 4.5, "Comm": 4.0}))
emp.add_review(Review("Q2", {"Tech": 4.8, "Comm": 4.5}))
print(emp.is_eligible())  # True if average >= 4.0
dept = Department()
dept.add_employee(emp)
print(dept.department_average())