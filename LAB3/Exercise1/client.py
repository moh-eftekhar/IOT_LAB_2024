import requests
import json

def get_operation():
    print("Select operation:")
    print("add")
    print("sub")
    print("mul")
    print("div")
    print("exit")
    operation = input("Enter choice (add/sub/mul/div/exit): ")
    return operation

def get_operands():
    operand1 = float(input("Enter first operand: "))
    operand2 = float(input("Enter second operand: "))
    operand3 = float(input("Enter third operand: "))
    return operand1, operand2, operand3

def invoke_calculator_service(operation, operand1, operand2, operand3):
    url = f'http://localhost:8080/{operation}'#?operand1={operand1}&operand2={operand2}'
    payload = {
        'operand1': operand1,
        'operand2': operand2,
        'operand3': operand3
    }
    response = requests.get(url, params=payload)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")
        return None

def main():
    while True:
        operation = get_operation()
        if operation == 'exit':
            break
        operand1, operand2,operand3 = get_operands()
        result = invoke_calculator_service(operation, operand1, operand2,operand3)
        if result:
            print(json.dumps(result, indent=4))

if __name__ == '__main__':
    main()