#functie bereik 2 param ondergrens(int),bovengrens(int) returned lijst met alle elementen vanaf de ondergrens tot de bovengrens
#bijv 2.9 > 2,3,4,5,6,7,8,9
#while + return

def bereken(a,b):
    while b > a:
        a = a+1
        c = a
        if b > a:
            print(c)


r = bereken(1,10)


print(r)
