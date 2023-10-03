class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(students_list):
  # Sort the list of students in descending order of CGPA
  sorted_students = sorted(students_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students

# Example usage
students = [Student("Jack", "A123", 7.8),
            Student("Christy", "A124", 8.9),
            Student("Willy", "A125", 9.1),
            Student("Stephen", "A126", 9.9),
           ]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name, student.roll_number, student.cgpa))
