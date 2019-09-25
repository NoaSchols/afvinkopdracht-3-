# Rectangle 1 
rectangle1length = int(input(" What is the length? "))
rectangle1width = int(input (" What is the width? "))

#Rectangle 2
rectangle2length = int(input(" What is the length? "))
rectangle2width = int(input(" What is the width? "))

#Area rectangle 1
area1 = (rectangle1length * rectangle1width)

#Area rectangle 2
area2 = (rectangle2length * rectangle2width)

if area1 > area2:
    print ("area1 is bigger than area2")
elif area1 < area2:
    print ("area1 is smaller than area2")
else :
    print ("area1 and area2 are the same size")

