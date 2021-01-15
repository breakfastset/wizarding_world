from wizard import Wizard

def main():
    wizard1 = Wizard("Harry Potter", 12, 20, 1000)
    wizard2 = Wizard("Dumbledore", 75, 98, 200000)
    wizard3 = Wizard("Voldermort", 50, 99, 250000)

    print(wizard1)
    print(wizard2)
    print(wizard3)

if __name__ == '__main__':
    main()

# identifiers - 1) meaningful names, 2) avoid short names, 3) follow conventions
# variables will in lower case and separated by _ for each word
# function names will be same