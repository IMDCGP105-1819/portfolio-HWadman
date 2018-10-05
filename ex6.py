name = input("What is your name? ")
age = int(input("What is your age? "))
height = float(input("What is your height in inches? "))
weight = float(input("What is your weight in kilograms? "))
eyecolour = input("What is your eye colour? ")
haircolour = input("What is your hair colour? ")

isyoung = age < 30
istall = height > 60
isoverweight = weight > 76

print(f"It is {isyoung} that you are young")
print(f"It is {istall} that you are tall")
print(f"It is {isoverweight} that you are overweight")
