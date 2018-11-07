import random

aantal_pogingen = 0
doos_te_openene = 3
kat_gevonden = False

aantal_dozen = input("Voer een aantal dozen in waar de kat zich kan bevinden " )
print(int(aantal_dozen))
doos_met_katgen = random.randrange(int(aantal_dozen))
doos_met_kat = doos_met_katgen
print(doos_met_kat)
aantaldozen1 = aantal_dozen
gekozen_nummer = input("Welke doos check je?")

while kat_gevonden == False:
    if int(gekozen_nummer) == int(doos_met_kat):
        kat_gevonden = True
        print("kat gevonden")
        print(kat_gevonden)
    else:
        print("nope")
        aantal_pogingen = aantal_pogingen + 1
        print(aantal_pogingen)
        print(kat_gevonden)






