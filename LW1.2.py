print("Program-1")
print("Welcome", "to", "the", "world", "of", "Data",sep="-", end="&")
print("Python")

print('''
Program-2''')
name = input("Your name")
age = input("Your age")
hobby = input("Your hobby")
print("Hello,", name,"! At", age,",enjoying", hobby, "sounds fun!")

print('''
Program-3''')
num1 = int(input("1st Number"))
num2 = int(input("2nd Number"))
print("1st Number + 2nd Number =", num1 + num2)
print("1st number - 2nd Number =", num1 - num2)
print("1st number * 2nd Number =", num1 * num2)
print("1st number / 2nd Number =", num1 / num2)
print("1st number // 2nd Number =", num1 // num2) #Not understood
print("1st number % 2nd Number =", num1 % num2)
print("1st number raised to 2nd Number =", num1 ** num2) #why cant we directly change the input once entered

print('''
Program-4''')
a = 4
b = 8.2
c = "New Year"
d = True
e = 2 + 9j
print("a is ", a, type(a))
print("b is ", b, type(b))
print("c is ", c, type(c))
print("d is ", d, type(d))
print("e is ", e, type(e))

print('''
Program-5''')
ht = float(input("Your Height(ft)"))
wt = float(input("Your Weight(kgs)"))
print("Your Height is", ht, "ft", "and your weight is", wt, "kgs")

print('''
Program-6''')
Cond_1 = input("1st condition True/False:")
Cond_2 = input("2nd condition True/False:")
print("When and is used", Cond_1 and Cond_2)
print("When or is used", Cond_1 or Cond_2)
print("When not is used for 2nd condition", not Cond_2) #when false is given by user it should show true but it shows false only

print('''
Program-7''')
A = 1
print(A)
A += 1
print(A)
A -= 1
print(A)
A *= 3
print(A)
A /= 6
print(A)
