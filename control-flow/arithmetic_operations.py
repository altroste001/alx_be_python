


def perform_operation(num1, num2, operation):
    operation = operation.strip().lower()  
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return "Cannot divide by zero"
            return num1 / num2
        case _:
            return "Invalid operation"

