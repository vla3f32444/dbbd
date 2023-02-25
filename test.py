# Необходимо создать класс Ученик, где будут динамически создаваться поля:
# имя, фамилия 
# словарь оценок, где ключ - предмет (2 - 3 предмета), значение - список оценок,
# метод для вычисления средней оценки по какому-либо предмету.
# * Добавить метод заполения оценками предмет данными извне.
# Количество оценок = 15

from random import randint

STUDENT_ID = 0
LESSONS_COUNT = 5

class Student:
    def __init__(self, name, surname):
        global STUDENT_ID
        self.__id = STUDENT_ID
        self.name = name
        self.surname = surname
        STUDENT_ID += 1
    
    def get_id(self):
        return self.__id
    
leslist = ['math', 'phy', 'lit']

class Journal:
    def __init__(self, clsname, lst):
        self.clsname = clsname
        self.marks = {}
        for les in lst:
            self.marks[les] = {}

    def add_student(self, idst):
        for les in self.marks.keys():
            self.marks[les][idst] = [randint(0, 5) for i in range(LESSONS_COUNT)]

    def add_student_mark(self, les, idst, mark):
        self.marks[les][idst].append(mark)

    def print_student_marks(self):
        for les, st in self.marks.items():
            print(f'{les} - {st}')
    
    def print_mean_student_marks(self):
        for les, st in self.marks.items():
            print(f'\n{les}')
            for id, marks in st.items():
                print(f'{id} mean = {sum(marks) / len(marks)}')

ob1 = Student('Borya', 'Ivanov')
ob2 = Student('Kostya', 'Ivanov')
ob3 = Student('Anya', 'Ivanov')

cl1 = Journal('A1', leslist)
cl1.add_student(ob1.get_id())
cl1.add_student(ob2.get_id())
cl1.add_student(ob3.get_id())
cl1.print_mean_student_marks()