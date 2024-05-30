print("\t\t---Calculate Your Number Here---\t\t")
print()

def simple_calculator():

    num1 = float(input("Enter the first number: "))
    
    num2 = float(input("Enter the second number: "))
    
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    operation = input("Enter the number corresponding to the operation (1/2/3/4): ")
    
    if operation == '1':
        result = num1 + num2
        operation_symbol = '+'
    elif operation == '2':
        result = num1 - num2
        operation_symbol = '-'
    elif operation == '3':
        result = num1 * num2
        operation_symbol = '*'
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            operation_symbol = '/'
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation choice."
    
    return f"{num1} {operation_symbol} {num2} = {result}"

print(simple_calculator())
