print (" Naar welk restaurant gaan we?")

vegatarisch1 = str(input (" Is iemand vegatarisch (ja/nee)?"))
veganistisch1 = str(input(" Is iemand veganistisch (ja/nee)?"))
glutenvrij1 = str(input(" Is iemand glutenvrij (ja/nee)?"))



if vegatarisch1 == "ja" and veganistisch1 == "ja" and glutenvrij1 == "ja":
    print ("keuze uit cornercafe en The chefs kitchen")
elif vegatarisch1 == "ja" and veganistisch1 == "ja" and glutenvrij1 == "nee":
    print ("keuze uit cornercafe en the chefs kitchen")
elif vegatarisch1 == "ja" and veganistisch1 == "nee" and glutenvrij1 == "nee":
    print (" keuze uit mainstreet pizza, cornercafe, mama en the chefs kitchen")
elif vegatarisch1 == "nee" and veganistisch1 == "nee" and glutenvrij1 == "nee":
    print (" je kan naar alle restaurants")
elif vegatarisch1 == "ja" and veganistisch1 == "nee" and glutenvrij1 == "ja":
    print ("mainstreet pizza compagnie")
elif vegatarisch1 == "nee" and veganistisch1 == "ja" and glutenvrij1 == "nee":
    print (" keuze uit cornercafe en chefs kitchen")
elif vegatarisch1 == "nee" and veganistisch1 == "ja" and glutenvrij1 == "ja":
    print (" keuze uit  cornercafe en the chefs kitchen")
else: 
    print ("main street compagnie en chefs kitchen")
