print("This is a program to demonstrate operations between two numbers")
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
op = input("Enter the operator to perform operation between 1st number and 2nd number:")
match op:
    case '+':
        add = a + b
        print("The addition of both the numbers is", add)
    case '-':
        sub = a - b
        print("The subtraction between both the numbers is ", sub)
    case '*':
        prod = a * b
        print("The product of both the numbers is ", prod)
    case '/':
        div = a/b
        print("The division of both the numbers is ", div)
    case _:
        print("Invalid operation")
