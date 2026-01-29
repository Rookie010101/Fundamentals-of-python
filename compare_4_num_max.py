print("This is a program for comparing 4 numbers and deciding which is the maximum number.")
a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
c = int(input("Enter the 3rd number: "))
d = int(input("Enter the 4th number: "))
if a==b and b==c and c==d:
    print("All are same")
elif a==b:
    if a>c:
        if a>d:
            print("1st and 2nd number are same and are maximum")
        else:
            print("1st and 2nd number are same but 4th is maximum")
    elif c>d:
        print("1st and 2nd number are same but 3rd is maximum")
    else:
        print("1st and 2nd number are same but 4th is maximum")
elif a==c:
    if b>d:
        print("1st and 3rd number are same but 2nd is maximum")
    else:
        print("1st and 3rd number are same but 4th is maximum")
elif a==d:
    if a>b:
        if a>c:
            print("1st and 4th number are same and are maximum")
        else:
            print("1st and 4th number are same but 3rd is maximum")
    elif b>c:
        print("1st and 4th number are same but 2nd is maximum")
    else:
        print("1st and 4th number are same but 3rd is maximum")
elif a>b:
    if a>c:
        if a>d:
            print("1st number is maximum")
        else:
            print("4th number is maximum")
    elif c>d:
        print("4th number is maximum")
    else:
        print("3rd number is maximum")
elif b>c:
    if b>d:
        print("2nd number is maximum")
    else:
        print("4th number is maximum")
elif c>d:
    print("3rd number is maximum")
else:
    print("4th number is maximum")
