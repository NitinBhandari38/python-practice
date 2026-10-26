c = 300000000 

def energy(m):
    return m * pow(c,2)

def main():
    mass = int(input("Enter a mass(in kg) : "))
    E = energy(mass)
    print(E)

main()