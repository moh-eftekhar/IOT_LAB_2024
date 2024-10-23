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
        studentA.save()







# if __name__ == "__main__":
#     numbers = [1,2,3,4,5]
#     listlen = len(numbers)
#     print(f"The list is {numbers}")
#     print(f"The length of the list is {listlen}")
#     sum_numbers = 0
#     # for i in range(listlen):
#     #     print (f"i is {i}")
#     #     print(f"Adding {numbers[i]} to the sum")
#     #     sum_numbers += numbers[i]
#     for items in numbers:
#         print(f"Adding {items} to the sum")
#         sum_numbers += items
#     # i= 0
#     # while i < listlen:
#     #     print (f"i is {i}")
#     #     print(f"Adding {numbers[i]} to the sum")
#     #     sum_numbers += numbers[i]
#     #     i+=1
#     print(f"The sum of the numbers is {sum_numbers}")
