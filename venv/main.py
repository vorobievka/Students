class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def __str__(self):
        courses_in_progress_string = ",".join(str(element) for element in self.courses_in_progress)
        finished_courses_string = ",".join(str(element) for element in self.finished_courses)
        res = f"Имя: {self.name} \r\nФамилия: {self.surname}\r\nСредняя оценка за домашние задания: {self.average()}\r\n" \
              f"Курсы в процессе изучения: {courses_in_progress_string}\r\n" \
              f"Завершенные курсы: {finished_courses_string}"
        return res

    def average(self):
        summ = 0
        leng = 0
        for grade in self.grades:
            list = self.grades[grade]
            summ += sum(list)
            leng += len(list)
        if leng > 0:
            return summ / leng
        else:
            return 0

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.average() < other.average()

    def rate_lec(self, lecturer, course, rate):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.rates:
                lecturer.rates[course] += [rate]
            else:
                lecturer.rates[course] = [rate]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


pass


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rates = {}
        self.courses_attached = []
        # del Mentor.rate_hw

    def rate_hw(self):
        print('Не умею оценивать')

    def add_courses(self, course_name):
        self.courses_attached.append(course_name)
        self.rates[course_name] = []

    def average(self):
        summ = 0
        leng = 0
        for rate in self.rates:
            list = self.rates[rate]
            summ += sum(list)
            leng += len(list)
        if leng > 0:
            return summ / leng
        else:
            return 0

    def __str__(self):
        res = f"Имя: {self.name} \r\nФамилия: {self.surname}\r\nСредняя оценка за лекции: {self.average()}"
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.average() < other.average()


pass


class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        res = f"Имя: {self.name} \r\nФамилия: {self.surname}"
        return res


pass

list_lecturer = []
cool_lecturer = Lecturer('Ivan', 'Petrov')
cool_lecturer.add_courses('Python')
list_lecturer.append(cool_lecturer)

bad_lecturer = Lecturer('Some', 'Buddy')
bad_lecturer.add_courses('Python')
list_lecturer.append(bad_lecturer)

list_student = []
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.add_courses('Введение в программирование')
best_student.rate_lec(cool_lecturer, 'Python', 10)
best_student.rate_lec(bad_lecturer, 'Python', 5)
list_student.append(best_student)

worst_student = Student('Tom', 'Sawyer', 'your_gender')
worst_student.courses_in_progress += ['Python']
worst_student.add_courses('Введение в программирование')
worst_student.rate_lec(cool_lecturer, 'Python', 10)
worst_student.rate_lec(bad_lecturer, 'Python', 5)
list_student.append(worst_student)

cool_reviewer = Reviewer('Chuck', 'Norris')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer.rate_hw(worst_student, 'Python', 5)
cool_reviewer.rate_hw(worst_student, 'Python', 10)
cool_reviewer.rate_hw(worst_student, 'Python', 5)
cool_reviewer.rate_hw(worst_student, 'Python', 10)

print(" ")
print('Проверяющие')
print(cool_reviewer)

print(" ")
print('Студенты')
print(*list_student, sep="\n")
print("Хороший студент лучше плохого:", best_student > worst_student)
print("Хороший преподаватель лучше плохого:", cool_lecturer > bad_lecturer)

print(" ")
print('Лекторы')
print(*list_lecturer, sep="\n")

pass
