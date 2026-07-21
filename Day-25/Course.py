'''
6. Course Enrollment with Capacity Control
Context: A university course has limited seats.

Task: Create a Course class with:

Attributes: course_name, max_capacity, enrolled_students (list of student names).

Methods:

enroll(student_name) – if seats available, add to list; else print "Course full".

drop(student_name) – remove from list.

available_seats() – returns remaining seats.

Class variable: total_enrolled_across_courses (incremented on enroll, decremented on drop).

Class method: get_total_enrolled() – returns total enrolled across all courses.

Sample Usage:

c1 = Course("Math", 2)
c1.enroll("Alice")  # ok
c1.enroll("Bob")    # ok
c1.enroll("Charlie") # full
print(c1.available_seats())  # 0
print(Course.get_total_enrolled())  # 2
c1.drop("Bob")
print(Course.get_total_enrolled())  # 1
'''

class Course:

    total_enrolled_across_courses = 0
    
    def get_total_enrolled():
        return Course.total_enrolled_across_courses
    
    def __init__(self,name,cap,enorolled=[]):
        self.course_name = name
        self.max_capacity = cap
        self.enrolled_students = enorolled

    def enroll(self,name):
        if len(self.enrolled_students) < self.max_capacity:
            if name.lower().strip() not in self.enrolled_students:
                self.enrolled_students.append(name.lower().strip())
                Course.total_enrolled_across_courses+=1
                return "Student added successfully"
            else:
                return "Student already enrolled in this course"
        else:
            return "No seats available"
        
    def drop(self,name):
        if name.lower().strip() in self.enrolled_students:
            self.enrolled_students.remove(name.lower().strip())
            Course.total_enrolled_across_courses-=1
            return "Removed Successfully"
        else:
            return "Student with this name does not exist"
        
    def available_seats(self):
        av = self.max_capacity - len(self.enrolled_students)
        return av
    
c1 = Course("Math", 2)
c1.enroll("Alice")  # ok
c1.enroll("Bob")    # ok
c1.enroll("Charlie") # full
print(c1.available_seats())  # 0
print(Course.get_total_enrolled())  # 2
c1.drop("Bob")
print(Course.get_total_enrolled())  # 1