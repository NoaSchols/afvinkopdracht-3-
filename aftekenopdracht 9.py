pocket = int(input("Name a number between 0 and 36"))


if pocket == 0:
    print (" the pocket is green ")
elif str(pocket >= 1 and pocket  <=10) or str(pocket >=19 and pocket <=28):
    if (pocket.endswith("2")
    or pocket.endswith("0")
    or pocket.endswith("4")
    or pocket.endswith("6")
    or pocket.endswith("8")):
        print (" Your pocket is red ")
else:
        print (" Your pocket is black")
    
        
   
if  str(pocket  >=11 and pocket <=18) or str(pocket  >=29 and pocket <=36):
    if (pocket.endswith("2")
    or pocket.endswith("0")
    or pocket.endswith("4")
    or pocket.endswith("6")
    or pocket.endswith("8")):
        print (" Your pocket is black")
else :
    print ("Your pocket is red")
    

