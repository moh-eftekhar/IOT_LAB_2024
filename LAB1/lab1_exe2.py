# import json
# class Calculator:
#     def __init__(self,paramlist):
#         self.paramlist = paramlist
#         self.result = None
#         self.operation = None
#         self.result_jason = {"operation": self.operation,"operands":self.paramlist, "result": self.result}
#         self.file = open("output.json", "a")

#     def add(self):
#         self.result = sum([float(i) for i in self.paramlist])
#         self.result_jason["operation"] = "add"
#         self.result_jason["result"] = self.result
#         json.dump(self.result_jason, self.file, indent=4)
#         self.file.flush()
#         return self.result
    
   


# if __name__ == "__main__":
#     print("Welcome to the calculator")
#     while True:
#         print("Enter 1 for addition")
#         print("Enter 2 for subtraction")
#         print("Enter 3 for multiplication")
#         print("Enter 4 for division")
#         print("Enter 5 to exit")
#         choice = int(input("Enter your choice: "))

#         if choice == 5:
#             break

#         paramlist = input("Enter numbers separated by ,: ").split(",")
#         paramlist = [float(num) for num in paramlist]


#         if choice == 1:
#             calc = Calculator(paramlist)
#             print("Result:", calc.add())

import json

class Calculator:
    def __init__(self, paramlist):
        self.paramlist = paramlist
        self.result = None
        self.operation = None
        self.result_json = {"operation": self.operation, "operands": self.paramlist, "result": self.result}

    def add(self):
        self.result = sum([float(i) for i in self.paramlist])
        self.result_json["operation"] = "add"
        self.result_json["result"] = self.result
        return self.result_json

# Function to save the JSON results properly
def save_to_file(data):
    with open("output.json", "w") as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    print("Welcome to the calculator")

    results = []

    while True:
        print("Enter 1 for addition")
        print("Enter 2 for subtraction")
        print("Enter 3 for multiplication")
        print("Enter 4 for division")
        print("Enter 5 to exit")
        choice = int(input("Enter your choice: "))

        if choice == 5:
            break

        paramlist = input("Enter numbers separated by ,: ").split(",")
        paramlist = [float(num) for num in paramlist]

        if choice == 1:
            calc = Calculator(paramlist)
            result = calc.add()
            results.append(result)
            print("Result:", result["result"])

    # Save all the results at once when the program ends
    save_to_file(results)
