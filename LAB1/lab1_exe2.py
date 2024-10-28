import json
import os

class Calculator:
    def __init__(self,paramlist):
        self.paramlist = paramlist
        self.result = None
        self.operation = None
        self.result_json = {"operation": self.operation, "operands": self.paramlist, "result": self.result}

    def add(self):
        self.result = sum(self.paramlist)
        self.result_json["operation"] = "add"
        self.result_json["result"] = self.result
        return self.result_json
    
    def sub(self):
        self.result = self.paramlist[0]
        for i in range(1,len(self.paramlist)):
            self.result -= self.paramlist[i]
        self.result_json = {"operation": "sub", "operands": self.paramlist, "result": self.result}
        return self.result_json
    
    def mul(self):
        self.result = 1
        for i in self.paramlist:
            self.result *= i
        self.result_json["operation"] = "mul"
        self.result_json["result"] = self.result
        return self.result_json
    
    def div(self):
        if 0 in self.paramlist:
            self.result = "Division by zero is not allowed."
        else:
            self.result = self.paramlist[0]
            for i in range(1,len(self.paramlist)):
                self.result /= self.paramlist[i]
        self.result_json["result"] = self.result
        self.result_json["operation"] = "div"
        return self.result_json
    
    def savejson(self):
        filename = "calculator.json"
        if os.path.exists(filename):
            with open(filename, "r") as file:
                try:
                    calculator = json.load(file)
                except json.JSONDecodeError:
                    calculator = []
        else:
            calculator = []
        
        calculator.append(self.result_json)
        with open(filename, "w") as cal_file:
            json.dump(calculator, cal_file, indent=4)

if __name__ == "__main__":
    condition = True
    while condition:
        operation = input("Enter operation: add/sub/mul/div/exit: ")
        if operation == "exit":
            print("Calculator closed.")
            break
        elif operation not in ["add", "sub", "mul", "div"]:
            print("Invalid operation. Please enter a valid operation.")
            continue
        paramlist = input("Enter operands separated by comma: ").split(",")
        for i in range(len(paramlist)):
            paramlist[i] = float(paramlist[i])
        mycal = Calculator(paramlist)
        if operation == "add":
            mycal.add()
            print(json.dumps(mycal.result_json, indent=4))
        elif operation == "sub":
            mycal.sub()
            print(json.dumps(mycal.result_json, indent=4))
        elif operation == "mul":
            mycal.mul()
            print(json.dumps(mycal.result_json, indent=4))
        elif operation == "div":
            mycal.div()
            print(json.dumps(mycal.result_json, indent=4))

        mycal.savejson()