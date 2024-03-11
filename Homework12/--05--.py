class Class:
    __students_count = 22
    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if Class.__students_count > len(self.students):
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        if len(self.grades) > 0:
            average_grade = sum(self.grades) / len(self.grades)
            return round(average_grade, 2)
        return 0

    def __repr__(self):
        average_grade = self.get_average_grade()
        students_repr = ', '.join(self.students)
        return f"The students in {self.name}: {students_repr}. Average grade: {average_grade:.2f}"


# Example
# a_class = Class("11B")
# a_class.add_student("Peter", 4.80)
# a_class.add_student("George", 6.00)
# a_class.add_student("Amy", 3.50)
# a_class.get_average_grade()
# print(a_class)
