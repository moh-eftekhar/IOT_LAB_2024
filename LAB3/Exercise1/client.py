import requests

def get_operation():
    print("Select operation:")
    print("add")
    print("sub")
    print("mul")
    print("div")
    operation = input("Enter choice (add/sub/mul/div): ")
    return operation

def get_operands():
    operand1 = float(input("Enter first operand: "))
    operand2 = float(input("Enter second operand: "))
    return operand1, operand2

def invoke_calculator_service(operation, operand1, operand2):
    url = 'http://localhost:8080'  # Replace with your actual URL
    payload = {
        'operation': operation,
        'operand1': operand1,
        'operand2': operand2
    }
    response = requests.get(url, json=payload)
    print("response ------>>>>>>",response)
    if response.status_code == 200:
        return response
    else:
        print(f"Request failed with status code {response.status_code}")
        return None

def main():
    operation = get_operation()
    operand1, operand2 = get_operands()
    print(f"--------->>>>>>Operation: {operation}, Operand1: {operand1}, Operand2: {operand2}")
    result = invoke_calculator_service(operation, operand1, operand2)
    if result:
        print(f"The result of the operation is: {result['result']}")

if __name__ == '__main__':
    main()