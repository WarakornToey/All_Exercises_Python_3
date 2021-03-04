number = int(input("Number : "))
star = "*"
for x in range(number):
    y = 2 * x + 1
    number -= 1
    print(" " * number + y * star)
    
    
