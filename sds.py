def bereik(a, b):
    getal = a
    lst = []

    while getal < b:
        lst = lst + [getal]
        getal = getal +1
    return lst

print(bereik(2,9))

for item in [1,2,3,4,5,6,7,8,9]:
    print("nu")
    print("is")
    print("nu!")
    print(item)

for dingetjes in bereik(1, 10):
    print("u")
    print("s")
    print("a!")
    print(dingetjes)