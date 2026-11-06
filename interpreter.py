expression = input("Expression : ")
x, y, z = expression.split(" ")
x = int(x)
z = int(z)
if y == "+":
    total = x+z
elif y == "-":
    total = x-z
elif y == "*":
    total = x*z 
elif y == "/":
    total = x/z 
else:
    print("Error")
print(f"{total:.1f}")