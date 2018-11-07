a = input("Geef een waarde (geen 0) ")

try:
    a = int(a)
    b = 100 /a
    print(b)
except:
    print("Divide by zero?")
finally:
    print("bedankt voor t meedoen")
#while True:
#    try:
#        invoer = input("Doe me eens een getal")