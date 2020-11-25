
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
# in the course class our methd add_students allow us to store any tipe of object.
course.add_students(s1)
course.add_students(s2)

print(course.students[0].name)
print(course.students[0:1])

# ?inheretenc
class Pet:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def show(self):
    print(f"hey I am {self.name} and I am {self.age} years old")

  def Speak(self):
    print("I can't speak!") 

