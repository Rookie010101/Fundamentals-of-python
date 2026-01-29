print("This is a program for comparing 3 numbers and deciding which is the minimum number.")
a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
c = int(input("Enter the 3rd number: "))
if a==b and b==c:
    print("All are same")
elif a==b:
    if a<c:
        print("1st and 2nd numbers are same and are minimum")
    else:
        print("1st and 2nd numbers are same but 3rd is minimum")
elif a==c:
    if b<c:
        print("1st and 3rd numbers are same but 2nd number is minimum")
    else:
        print("1st and 3rd numbers are same and are minimum")
elif b==c:
    if a<c:
        print("2nd and 3rd numbers are same but 1st is minimum")
    else:
        print("2nd and 3rd numbers are same and are minimum")
else:
    if a<b:
        if a<c:
            print("1st number is minimum")
        else:
            print("3rd number is minimum")
    elif b<c:
        print("2nd number is minimum")
    else:
        print("3rd number is minimum")
