import datetime as dt
class Student:
    def __init__(self, name, surname, birthyear):
        self.name = name
        self.surname = surname
        self.birthyear = birthyear

    def get_age(self):
        return dt.datetime.now().year - self.birthyear
    def show(self):
        return f"{self.name} {self.surname} is {self.get_age()} years old"

if __name__ == "__main__":
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    brithyear = int(input("Enter your birth year: "))
    studentA = Student(name, surname, brithyear)
    print(studentA.show())