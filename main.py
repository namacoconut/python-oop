class Student:
  def __init__(self, name , age, grade):
    self.name = name
    self.age = age
    self.grade = grade

  def get_grade(self):
    return self.grade

class Course:
  def __init__(self, name, max_students):
    