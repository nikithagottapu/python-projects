students = [
    {"name": "Nikitha", "course": "Data Engineering", "grades": [85, 90, 78, 92]},
    {"name": "Rahul", "course": "Python", "grades": [60, 55, 70, 65]},
    {"name": "Priya", "course": "Data Engineering", "grades": [45, 50, 40, 55]},
]

grade_boundaries = (80, 60, 40)

def calculate_average(grades):
    return sum(grades)/len(grades)


def assign_grade(average):
     if average>= grade_boundaries[0]:
          return "A"
     elif average>= grade_boundaries[1]:
          return "B"
     elif average>= grade_boundaries[2]:
          return "C"
     else:
          return "F"
     
for student in students:
     average = calculate_average(student["grades"])
     grade = assign_grade(average)
     print("----Student Report----")
     print(f"Name    : {student['name']}")
     print(f"Course  : {student['course']}")
     print(f"Average : {average}")
     print(f"Grade   : {grade}")
     print()

unique_courses = set(student["course"] for student in students)
print(f"Unique Courses: {unique_courses}")
    
