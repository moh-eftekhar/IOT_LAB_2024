import datetime as dt
class Student:
    def __init__(self, name, surname, birthyear):
        self.name = name
        self.surname = surname
        self.birthyear = birthyear

    def get_age(self):
        return dt.datetime.now().year - self.birthyear
    
    #with command is used to open the file and close it automatically
    def save(self):
        with open("student.txt", "a") as stu_file:
            stu_file.write(f"{self.name},{self.surname},{self.birthyear}\n")

        print(f"{self.name} {self.surname} is {self.get_age()} years old")
    

if __name__ == "__main__":
    f = open("student.txt")
    print(f.read())
    while True:
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        brithyear = int(input("Enter your birth year: "))
        studentA = Student(name, surname, brithyear)
        studentA.save()