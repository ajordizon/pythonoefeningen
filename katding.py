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
        print("het aantal pogingen is"+ str(aantal_pogingen))
        print(kat_gevonden)
        print("de kat zit eigenlijk in" + str(doos_met_kat))
        variable = random.randrange(1)
        variable = int(variable)
        print("het random nummer is" +str(variable))
        if variable == 1 and doos_met_kat != 0 and doos_met_kat <= aantal_dozen:
                doos_met_kat = int(doos_met_kat)
                doos_met_kat= int(doos_met_kat)-1
                print("de kat zit eigenlijk in" + str(doos_met_kat))
        elif variable == 0:
                doos_met_kat = int(doos_met_kat)
                doos_met_kat = doos_met_kat+1
                print("de kat zit eigenlijk in" + str(doos_met_kat))
        gekozen_nummer = input("nieuw nummer" )