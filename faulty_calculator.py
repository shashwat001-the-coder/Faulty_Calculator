'''This is a faulty calculator in which is you ask 45*3 or 3*45 and 56+9 or 9+56 and 56/6 it will give wrong
answers as feeded in it other than these it will give correct answers.'''
Ope = input("Enter the operator you want to use (+,-,*,/) :")
num_1 = int(input("Enter first number:"))
num_2 = int(input("Enter secomnd number:"))
if Ope == "*" and num_1 == 45 and num_2 == 3:
    print(555)
elif Ope == "*" and num_1 == 3 and num_2 == 45:
    print(555)
elif Ope == "+" and num_1 == 56 and num_2 == 9:
    print(77)
elif Ope == "+" and num_1 == 9 and num_2 == 56:
    print(77)
elif Ope == "/" and num_1 == 56 and num_2 == 6:
    print(4)
elif Ope == "+":
    print(num_1 + num_2)
elif Ope == "-":
    print(num_1 - num_2)
elif Ope == "*":
    print(num_1 * num_2)
else:
    print(num_1 / num_2)
