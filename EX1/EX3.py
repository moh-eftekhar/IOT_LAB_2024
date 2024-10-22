import datetime as dt
class Student:
    def __init__(self, name, surname, birthyear, degree):
        self.name = name
        self.surname = surname
        self.birthyear = birthyear
        self.degree = None
        self.bachelor = degree == 'b' or degree == 'B' or degree == 'bachelor' or degree == 'BACHELOR' or degree == 'Bachelor'
        self.master = degree == 'm' or degree == 'M' or degree == 'master' or degree == 'MASTER' or degree == 'Master'


    def get_age(self):
        return dt.datetime.now().year - self.birthyear
    
    def isBachelor(self):
        if self.bachelor:
            self.degree = "Bachelor"
            print ("The student is a bachelor")
        else:
            print ("The student is not a bachelor")
    
    def isMaster(self):
        if self.master:
            self.degree = "Master"
            print ("The student is a master")
        else:
            print ("The student is not a master")
    
    #with command is used to open the file and close it automatically
    def save(self):
        with open("student.txt", "a") as stu_file:
            stu_file.write(f"{self.name},{self.surname},{self.birthyear},{self.degree}\n")

        print(f"{self.name} {self.surname} is {self.get_age()} years old")
    

if __name__ == "__main__":
    f = open("student.txt")
    print(f.read())
    while True:
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        brithyear = int(input("Enter your birth year: "))
        degree = input("Select your level of Eductation (bachelor,master):")
        studentA = Student(name, surname, brithyear, degree)
        studentA.isBachelor()
        studentA.isMaster()
        studentA.save()