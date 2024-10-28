import json

class Calculator:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
        self.result = None
        self.operation = None
        self.result_json = {"operation": self.operation, "operands": [self.param1, self.param2], "result": self.result}

    def add(self):
        self.result = self.param1 + self.param2
        self.result_json["operation"] = "add"
        self.result_json["result"] = self.result
        return self.result_json

    def sub(self):
        self.result = self.param1 - self.param2
        self.result_json["operation"] = "sub"
        self.result_json["result"] = self.result
        return self.result_json

    def mul(self):
        self.result = self.param1 * self.param2
        self.result_json["operation"] = "mul"
        self.result_json["result"] = self.result
        return self.result_json

    def div(self):
        if self.param2 == 0:
            self.result = "Division by zero is not allowed."
        else:
            self.result = self.param1 / self.param2
        self.result_json["operation"] = "div"
        self.result_json["result"] = self.result
        return self.result_json

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
        param1 = float(input("Enter first operand: "))
        param2 = float(input("Enter second operand: "))
        mycal = Calculator(param1, param2)
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