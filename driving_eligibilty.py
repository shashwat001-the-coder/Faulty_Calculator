name = input("Enter Your Name:")
age = int(input("Enter Your Age:"))
if age<=0:
    print("PLease enter a valid age.")
elif age<4:
    print("You are too small to drive and using computer.(Please enter a valid age 5-120)")
elif age>120:
    print("Please enter a valid age.")
elif age > 18:
    print("Congrats "+name+" you are eligble to drive car")
elif age==18:
    print("Sorry "+name+" we can't say anything about you.You have to come in our office physically.")
else:
    print("Sorry "+name+" you are not eligible to drive car in India.")
