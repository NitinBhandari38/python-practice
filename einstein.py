# In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.





c = 300000000 

def energy(m):
    return m * pow(c,2)

def main():
    mass = int(input("Enter a mass(in kg) : "))
    E = energy(mass)
    print(E)

main()