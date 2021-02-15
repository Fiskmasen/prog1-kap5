userString = input("Skriv en mening, minst två ord: ")
splitString = userString.split()

if len(splitString) > 1:
    print(f"Du skrev {len(userString): 1} tecken.")

    print("Det första ordet är: " + splitString[0])

    print(len(userString) -1)

    print("Det sista ordet: " + splitString[len(splitString) -1])
else:
    print("Du måste ha minst 2 ord i meningen.")