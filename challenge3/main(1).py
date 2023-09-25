class Student:
  def __init__(self, name, roll__number, cgpa):
    self.name = name  
    self.roll_number = roll__number
    self.cgpa = cgpa
def sort_students(student_list):

  sorted_students = sorted(student_list,
                          key=lambda student: student.cgpa,
                           reverse=True) 
  return sorted_students
students = [
    Student("Sudhiksha", "A123",7.8),
    Student("Sriharini", "A124",8.9),
    Student("Anish", "A125",9.1),
    Student("Rifana", "A126",9.9),
]

sorted_students = sort_students(students)


for student in sorted_students:
  print("NAME:{}, ROLL NUMBER: {}, CGPA:{}".format(student.name,
                              student.roll_number,
                                                   student.cgpa))