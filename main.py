
# creating a class means creating reusable object
class Student:
  def __init__(self, name , age, grade):
    self.name = name
    self.age = age
    self.grade = grade

  def get_grade(self):
    return self.grade

class Course:
  def __init__(self, name, max_students):
    self.name = name
    self.max_students = max_students
    self.students = []

# store whatever value in max_students Attribute to students array
  def add_students(self, student_in_class):
    if len(self.students) < self.max_students:
      self.students.append(student_in_class)
      return True
    return False

  def get_average(self):
    pass

s1 = Student("tim", 23, 99)
s2 = Student("noor", 33, 0)

course = Course("math",2)
course.add_students(s1)
course.add_students(s2)

print(course.students[0].name)
print(course.students[0:1])