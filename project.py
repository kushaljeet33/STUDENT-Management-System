class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def __repr__(self):
        return f"Student(ID: {self.student_id}, Name: {self.name}, Average: {self.average_grade():.2f})"


class GradeChecker:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)
            print(f"Student {name} added successfully.")
        else:
            print(f"Student with ID {student_id} already exists.")

    def add_grade(self, student_id, grade):
        if student_id in self.students:
            self.students[student_id].add_grade(grade)
            print(f"Grade {grade} added for student ID {student_id}.")
        else:
            print(f"Student with ID {student_id} does not exist.")

    def get_student(self, student_id):
        return self.students.get(student_id, None)

    def calculate_class_average(self):
        if not self.students:
            return 0
        total = sum(student.average_grade() for student in self.students.values())
        return total / len(self.students)

    def sort_students_by_grade(self):
        return sorted(self.students.values(), key=lambda s: s.average_grade(), reverse=True)

    def __repr__(self):
        return '\n'.join(str(student) for student in self.sort_students_by_grade())


def main():
    grade_checker = GradeChecker()
    
    while True:
        print("\nStudent Grade Checker")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View Student")
        print("4. View All Students")
        print("5. Calculate Class Average")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            student_id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            grade_checker.add_student(student_id, name)
        
        elif choice == '2':
            student_id = int(input("Enter student ID: "))
            grade = float(input("Enter grade: "))
            grade_checker.add_grade(student_id, grade)
        
        elif choice == '3':
            student_id = int(input("Enter student ID: "))
            student = grade_checker.get_student(student_id)
            if student:
                print(student)
            else:
                print("Student not found.")
        
        elif choice == '4':
            print("\nAll Students:")
            print(grade_checker)
        
        elif choice == '5':
            print(f"\nClass Average: {grade_checker.calculate_class_average():.2f}")
        
        elif choice == '6':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
