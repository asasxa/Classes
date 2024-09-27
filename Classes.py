class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        if self.grades:
            return sum(sum(grades) for grades in self.grades.values()) / sum(len(grades) for grades in self.grades.values())
        return 0

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.average_grade():.2f}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade() == other.average_grade()
        return NotImplemented


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        if self.grades:
            return sum(sum(grades) for grades in self.grades.values()) / sum(len(grades) for grades in self.grades.values())
        return 0

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.average_grade():.2f}")

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() == other.average_grade()
        return NotImplemented


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")


# Функции для подсчета средней оценки
def average_student_grade(students, course):
    total_grade = 0
    count = 0
    for student in students:
        if course in student.grades:
            total_grade += sum(student.grades[course])
            count += len(student.grades[course])
    return total_grade / count if count > 0 else 0


def average_lecturer_grade(lecturers, course):
    total_grade = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grade += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return total_grade / count if count > 0 else 0


student1 = Student('Пашок', 'Эминем', 'your_gender')
student1.courses_in_progress += ['Python']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Дмитрий', 'Иванов', 'male')
student2.courses_in_progress += ['Python', 'Java']
student2.finished_courses += ['Алгоритмы']

lecturer1 = Lecturer('Евграф', 'Колумб')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Александр', 'Суворов')
lecturer2.courses_attached += ['Python', 'Java']

reviewer1 = Reviewer('Игнат', 'Путин')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Сергей', 'Лукашенко')
reviewer2.courses_attached += ['Java']

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student2, 'Python', 8)

reviewer2.rate_hw(student2, 'Java', 9)

student1.rate_lecturer(lecturer1, 'Python', 8)
student2.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer2, 'Java', 10)

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)
print()
print("Средняя оценка за домашние задания по курсу 'Python':", average_student_grade([student1, student2], 'Python'))
print("Средняя оценка за домашние задания по курсу 'Java':", average_student_grade([student1, student2], 'Java'))
print("Средняя оценка за лекции по курсу 'Python':", average_lecturer_grade([lecturer1, lecturer2], 'Python'))
print("Средняя оценка за лекции по курсу 'Java':", average_lecturer_grade([lecturer1, lecturer2], 'Java'))