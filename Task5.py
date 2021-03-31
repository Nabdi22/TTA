num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
operator = input("Please choose a math operator: a) + , b) / , c) - or d) * : ")
a = ("a")
b = ("b")
c = ("c")
d = ("d")

if operator == a:
    print(num1 + num2)
elif operator == b:
    print(num1 / num2)
elif operator == c:
    print(num1 - num2)
elif operator == d:
    print(num1 * num2)
