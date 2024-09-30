Суть работы:
## Задание № 1. Наследование
Исходя из квиза к предыдущему занятию, у нас уже есть класс преподавателей и класс студентов. Студентов пока оставим без изменения, а вот преподаватели бывают разные, поэтому теперь класс Mentor должен стать родительским классом, а от него нужно реализовать наследование классов Lecturer (лекторы) и Reviewer (эксперты, проверяющие домашние задания). Очевидно, имя, фамилия и список закрепленных курсов логично реализовать на уровне родительского класса. А чем же будут специфичны дочерние классы? Об этом в следующих заданиях.

## Задание № 2. Атрибуты и взаимодействие классов.
В квизе к предыдущей лекции мы реализовали возможность выставлять студентам оценки за домашние задания. Теперь это могут делать только Reviewer (реализуйте такой метод)! А что могут делать лекторы? Получать оценки за лекции от студентов :) Реализуйте метод выставления оценок лекторам у класса Student (оценки по 10-балльной шкале, хранятся в атрибуте-словаре у Lecturer, в котором ключи – названия курсов, а значения – списки оценок). Лектор при этом должен быть закреплен за тем курсом, на который записан студент.

## Задание № 3. Полиморфизм и магические методы
Перегрузите магический метод __str__ у всех классов.
У проверяющих он должен выводить информацию в следующем виде:

print(some_reviewer)
Имя: Some
Фамилия: Buddy
У лекторов:

print(some_lecturer)
Имя: Some
Фамилия: Buddy
Средняя оценка за лекции: 9.9
А у студентов так:

print(some_student)
Имя: Ruoy
Фамилия: Eman
Средняя оценка за домашние задания: 9.9
Курсы в процессе изучения: Python, Git
Завершенные курсы: Введение в программирование
Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания.

## Задание № 4. Полевые испытания
Создайте по 2 экземпляра каждого класса, вызовите все созданные методы, а также реализуйте две функции:

для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса);
для подсчета средней оценки за лекции всех лекторов в рамках курса (в качестве аргумента принимаем список лекторов и название курса).
