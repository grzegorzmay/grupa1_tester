# v.1.0 dzialajacej aplikacji

wiek = input("Podaj wiek uzytkownika: ")
#sprawdzenie czy wiek jest liczba calkowita
if wiek.isdigit() == False:
    exit("Wiek musi byc liczba calkowita. Zamykam aplikacje")
wiek=int(wiek)
if wiek>=18 and wiek<=40:
    print("Witam w apce. Mozesz u nas kupowac alkohol")
elif wiek>40 and wiek<=120:
    print("Witam w apce. Mozesz u nas kupowac alkohol")
    print("Korzystaj z produktow z umiarem")
elif wiek>120:
    print("Witam w apce. Mozesz u nas kupowac alkohol")
    print("Ale w tym nie wieku lepiej tego jednak nie robic...")
else:
    exit("Jestes za mlody/a na alkohol. Zapraszamy na disney.com")
    