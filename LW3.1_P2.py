age = int(input("Please enter your age"))
if age<=0:
    print("Age is invalid")
elif age<=12:
    print("You are a child")
elif age<=19:
    print("You are a teenager")
elif age<=59:
    print("You are an adult")
elif age<100:
    print("You are a senior")
else:
    print("Age is invalid")
