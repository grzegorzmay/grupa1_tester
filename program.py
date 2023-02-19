# v.1.0 dzialajacej aplikacji
region = input("Wybierz region: ") 
if region != 'USA' and region != 'EUR':
    exit("Musisz wybrac region USA lub EUR")

plec = input ("wybierz plec: ")
if plec != 'Kobieta' and plec != 'Mezczyzna':
    exit("Musisz wybrac plec kobieta lub mezczyzna")

wiek = input("Podaj wiek uzytkownika: ")
#sprawdzenie czy wiek jest liczba calkowita
if wiek.isdigit() == False:
    exit("Wiek musi byc liczba calkowita. Zamykam aplikacje")
wiek=int(wiek)

if region == "USA" and wiek>=21 and wiek<=40:
    print("Witamy w aplikacji. Mozesz kupowac u nas alkohol")
if region == "EUR" and wiek>=18 and wiek<=40:
    print("Witamy w aplikacji. Mozesz kupowac u nas alkohol")
elif wiek>40 and wiek<=120:
    print("Witam w apce. Mozesz u nas kupowac alkohol")
    print("Korzystaj z produktow z umiarem")
elif wiek>120:
    print("Witam w apce. Mozesz u nas kupowac alkohol")
    print("Ale w tym nie wieku lepiej tego jednak nie robic...")
else:
    a = 18 - wiek
    print("Jestes za mlody/a na alkohol. Zapraszamy za",a,"lat/a")
    exit

plec = input ("wybierz plec K/M: ")
if plec != 'K' and plec != 'M':exit("Musisz wybrac plec Kobieta lub Mezczyzna")

if wiek > 30 and plec == 'K':
    print ("Pierwszy Aperol Spritz gratis")
