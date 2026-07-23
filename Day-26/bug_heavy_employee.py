class Review:
    def __init__(self,q,scores):
        self.quater = q
        self.scores = scores
    
    def average_score(self):
        l = len(self.scores)
        sum = 0
        for i in self.scores.values():
            sum+=i
        avg = sum / l
        return avg

class Employee:
    def __init__(self,name):
        self.__name = name
        self.__reviews = []

    def add_review(self,q,scores):
        r = Review(q=q,scores=scores)
        avg = r.average_score()
        self.__reviews.append(avg)

    def get_average_score(self):
         l = len(self.__reviews)
         sum = 0
         for i in self.__reviews:
            sum+=i
         avg = sum / l
         return avg
    
    def last_two_average(self):
        if len(self.__reviews) >= 2:
            last = self.__reviews[-1]
            second_last = self.__reviews[-2]
            avg = (last + second_last)/2.0
            return avg
        else:
            return "The reviews are less then 2"
    
    def is_eligible(self,threshold):
        last_two = self.last_two_average()
        if type(last_two) == float:
            if last_two >= threshold:
                return True
            else:
                return False
        else:
            return False

class Department:

    DEFAULT_PROMOTION_THRESHOLD = 4.0

    def __init__(self,name):
        self.name = name
        self.employees = []

    def add_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
            return "Employee added successfuly"
        else:
            return "Employee already in the department"
        
    def department_average(self):
        l = len(self.employees)
        sum = 0
        for i in self.employees:
            sum+=i.get_average_score()
        avg = sum/l
        return avg
    
    def eligible_employees(self,th=DEFAULT_PROMOTION_THRESHOLD):
        eligible = []
        for i in self.employees:
            if i.is_eligible(th):
                eligible.append(i)
        return eligible
    


emp = Employee("Sara")
emp.add_review("Q1", {"Tech": 4.5, "Comm": 4.0})
emp.add_review("Q2", {"Tech": 4.8, "Comm": 4.5})
print(emp.is_eligible(4.0))  # True if average >= 4.0
dept = Department('Tech')
dept.add_employee(emp)
print(dept.department_average())