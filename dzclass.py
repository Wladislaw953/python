# Вариант 4

class Student(object):

    def __init__(self, id, familiya, imia, otchestvo, data, adres, tel, facultet, kurs, gruppa):
        self.id = id
        self.familiya = familiya
        self.imia = imia
        self.otchestvo = otchestvo
        self.data = data
        self.adres = adres
        self.tel = tel
        self.facultet = facultet
        self.kurs = kurs
        self.gruppa = gruppa

    def ListGroups(self):
        if self.gruppa == 'Pedagogicheskij':
            print('Список учебной группы: ' + self.familiya + self.facultet + self.gruppa + self.kurs)
        else:
            print()

    def ListStudents(self):
        if self.facultet == 'Pedagogicheskij':
            print(
                'Список студентов заданного факультета: ' + self.id + self.familiya + self.imia + self.otchestvo + self.facultet)
        else:
            print('Другой факультет: ' + self.facultet)


Student1 = Student(1211, 'Ivanov', 'Ivan', 'Ivanovich', 01.1970, 'Minsk', 123443211, 'Pedagogicheskij', 4, 2)
Student2 = Student(1212, 'Petrov', 'Petr', 'Petrovich', 10.1970, 'Grodno', 123443212, 'Istoricheskij', 3, 5)
Student3 = Student(1213, 'Nikitin', 'Sergej', 'Fedorovich', 07.1970, 'Pinsk', 123443213, 'Pedagogicheskij', 2, 2)
Student4 = Student(1214, 'SMIRNOV', 'Nikolaj', 'Egorovich', 02.1970, 'Brest', 123445214, 'Istoricheskij', 3, 5)
Student5 = Student(1215, 'Ibragimov', 'Stepan', 'Antonovich', 12.1970, 'Gomel', 12343215, 'Pedagogicheskij', 4, 3)

print(Student1.facultet)
print(Student3.gruppa)
