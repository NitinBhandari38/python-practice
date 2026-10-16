def main():
    x = int(input("Write the value of x: "))
    print(f"square of {x} is: ", square(x))

def square(n):
    return pow(n, 2)

main()