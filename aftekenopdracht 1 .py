nummer = int(input(" Noem een nummer "))

#Dit is om te kijken of het een positief of negatief getal is.
if nummer > 0:
    print ("positief")
elif nummer < 0:
    print (" negatief")
else :
    print (" zero")
# Nu we weten of het positief of negatief
nummer = str(nummer)
if (nummer.endswith("2")
    or nummer.endswith("0")
    or nummer.endswith("4")
    or nummer.endswith("6")
    or nummer.endswith("8")):
    print ("even")
else :
    print ("odd")

