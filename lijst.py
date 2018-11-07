def takeSecond(elem):
    return elem[1]

productgroepen = ["Drinken","Groenten en fruit", "Blikvoedsel", "Zuivel", "Vlees"]


drinken = 0
groenten = 1
blik = 2
zuivel = 3
vlees = 4


boodschappen = [
    ["Cola Zero", 4, drinken],
    ["Bananen", "tros", groenten],
    ["Worteltjes","blik 500g", blik]
]

def artikel(item):
    return(item[0], "aantal", item[1], "in groep", productgroepen[item[2]])


#boodschappenlijst = [
#    ['Ice Tea', 2],
#    ['Cola', 1],
#    ['Cola Zero', 2],
#    ['Kilo Bananen', 3],
#    ['Kilo Iets', 5],
#    ['Kilo Anders', 9]
#]

#boodschappenlijst.sort(key=takeSecond)
#print(boodschappenlijst)

boodschappen.sort()
for item in boodschappen:
    print(artikel(item))
