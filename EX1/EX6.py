import datetime as dt
import json
import os
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

    def vote(self):
        f = open("studentvotes.txt").read()
        votelist = f.split(",")
        votelist_int = [int(vote) for vote in votelist]
        self.votelist = votelist_int
    
    def stat(self):
        max_vote = max(self.votelist)
        print(f"The maximum vote is {max_vote}")
        min_vote = min(self.votelist)
        print(f"The minimum vote is {min_vote}")
        num_votes = len(self.votelist)
        sum_votes = 0
        for vote in self.votelist:
            sum_votes += vote
        average_votes = sum_votes / num_votes
        print(f"The average vote is {average_votes}")
    

    def asDictionary(self):
        #Output -> {“name”:”Lionel”,”surname”:”Messi”,”birthYear”:1987,”votes”:[24,27,18,30,21]}
        dictionary_student={
            "name":self.name,
            "surname":self.surname,
            "birthYear":self.birthyear,
            "votes":self.votelist
        }
        #print(dictionary_student)
        return dictionary_student
    def savejason(self):
        filename = "student.json"
        # Check if the file exists and read its content
        if os.path.exists(filename):
            with open(filename, "r") as stu_file:
                try:
                    students = json.load(stu_file)
                except json.JSONDecodeError:
                    students = []
        else:
            students = []

        # Append the new student dictionary
        students.append(self.asDictionary())

        # Write the updated list back to the file
        with open(filename, "w") as stu_file:
            json.dump(students, stu_file, indent=4)
    
    #with command is used to open the file and close it automatically
    def save(self):
        with open("student.txt", "a") as stu_file:
            stu_file.write(f"{self.name},{self.surname},{self.birthyear},{self.degree}\n")

        print(f"{self.name} {self.surname} is {self.get_age()} years old")
    

if __name__ == "__main__":
    while True:
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        brithyear = int(input("Enter your birth year: "))
        degree = input("Select your level of Eductation (bachelor,master):")
        studentA = Student(name, surname, brithyear, degree)
        studentA.isBachelor()
        studentA.isMaster()
        studentA.vote()
        studentA.stat()
        dictionary_student=studentA.asDictionary()
        print(dictionary_student)
        studentA.savejason()
        studentA.save()