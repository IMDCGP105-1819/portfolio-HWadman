start = int(input("Enter the number you wish to start at: "))
end = int(input("Enter the number you wish to end at: "))

output = ""
for x in range(start,end+1):

    if x % 3 == 0:
        output += "Fizz"

    if x % 5 == 0:
        output += "Buzz"

    if "Fizz" not in output and "Buzz" not in output:
        output = str(x)

    print(f"{output}")
    output = ""
