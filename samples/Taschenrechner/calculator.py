def prompt_menu():
    a = float(input("Gib die erste Zahl ein: "))
    b = float(input("Gib die zweite Zahl ein: "))
    print("""
Welche Rechenoperation soll ausgeführt werden?:
1. Addition
2. Subtraktion
3. Multiplikation
4. Exponentialfunktion
5. Division
    """)
    op = int(input("Gib die entsprechende Nummer ein: "))
    return a, b, op

def calculate():
    a, b, op = prompt_menu()
    if op == 1:
        print("Summe: {} + {} = {}".format(a,b,a+b))
    elif op == 2:
        print("Difference: {} - {} = {}".format(a,b,a-b))
    elif op == 3:
        print("Produkt: {} * {} = {}".format(a,b,a*b))
    elif op == 4:
        print("Power: {}^{} = {}".format(a,b,a**b))
    elif op == 5:
        try:
            print("Quotient: {} / {} = {}".format(a,b,a/b))
        except:
            print("Division durch 0 ist nicht möglich!")
    else:
        print("Diese Auswahl gibts nicht!")
    loop()

def loop():
    choice = input("Willst Du weiterrechnen? (Y,N): ")
    if choice.upper() == "Y":
        calculate()
    elif choice.upper() == "N":
        print("Goodbye!")
    else:
        print("Diese Auswahl gibts nicht!")
        loop()

calculate()