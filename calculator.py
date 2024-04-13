def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y

while True:
    try:
        print("Enter your first number: ")
        num1 = float(input())
        print("Enter your second number: ")
        num2 = float(input())
    except ValueError:
        print("Please enter valid numbers.")
        continue
  
    print("Enter an operation to perform:")
    print("'a': Addition")
    print("'s': Subtraction")
    print("'m': Multiplication")
    print("'d': Division")
    print("'e': Exit")
    operation = input()

    if operation == 'e':
        break
    elif operation == 'a':
        result = add(num1, num2)
    elif operation == 's':
        result = subtract(num1, num2)
    elif operation == 'm':
        result = multiply(num1, num2)
    elif operation == 'd':
        if num2 == 0:
            print("Cannot divide by zero!")
            continue
        result = divide(num1, num2)
    else:
        print("Invalid operation!")
        continue
  
    print("Result:", result)
  
    while True:
        print("Would you like to perform another operation on this result?")
        print("'y': Yes")
        print("'n': No")
        choice = input()

        if choice == 'n':
            exit()
        elif choice == 'y':
            num1 = result
            try:
                print("Enter your next number: ")
                num2 = float(input())
                print("Enter an operation to perform:")
            except ValueError:
                print("Please enter a valid number.")
                continue
    
            print("'a': Addition")
            print("'s': Subtraction")
            print("'m': Multiplication")
            print("'d': Division")
            print("'e': Exit")
            operation = input()
          
            if operation == 'e':
                exit()
            elif operation == 'a':
                result = add(num1, num2)
            elif operation == 's':
                result = subtract(num1, num2)
            elif operation == 'm':
                result = multiply(num1, num2)
            elif operation == 'd':
                if num2 == 0:
                    print("Cannot divide by zero!")
                    continue
                result = divide(num1, num2)
            else:
                print("Invalid operation!")
                continue
          
            print("Result:", result)
        else:
            print("Invalid choice!")
            continue
