tp1 = False
while tp1 == False:
    try:
        tpoint1x = int(input("Please enter the x value for your first coordinate for your triangle: "))
        tpoint1y = int(input("Please enter the y value for your first coordinate for your triangle: "))
        tpoint1 = (tpoint1x,tpoint1y)
        tp1 = True
    except:
        print("Thats not a valid coordinate, please enter a valid coordinate")

tp2 = False
while tp2 == False:
    try:
        tpoint2x = int(input("Please enter the x value for your second coordinate for your triangle: "))
        tpoint2y = int(input("Please enter the y value for your second coordinate for your triangle: "))
        tpoint2 = (tpoint2x,tpoint2y)
        tp2 = True
    except:
        print("Thats not a valid coordinate, please enter a valid coordinate")

tp3 = False
while tp3 == False:
    try:
        tpoint3x = int(input("Please enter the x value for your second coordinate for your triangle: "))
        tpoint3y = int(input("Please enter the y value for your second coordinate for your triangle: "))
        tpoint3 = (tpoint3x,tpoint3y)
        tp3 = True
    except:
        print("Thats not a valid coordinate, please enter a valid coordinate")

triangle = (tpoint1, tpoint2, tpoint3)
print("Your triangle has the coordinates",triangle)

p1 = False
while p1 == False:
    try:
        point1x = int(input("Please enter the x value for your coordinate: "))
        point1y = int(input("Please enter the y value for your coordinate: "))
        point1 = (point1x,point1y)
        p1 = True
    except:
        print("Thats not a valid coordinate, please enter a valid coordinate")

print("Your point has the coordinates",point1)

tmidx = (tpoint1x + tpoint2x + tpoint3x)//3
tmidy = (tpoint1y + tpoint2y + tpoint3y)//3
tmidp = (tmidx, tmidy)

if point1x > tmidx:
    xpos = "Right"
elif point1x < tmidx:
    xpos = "Left"
elif point1x == tmidx:
    xpos = "Same x"
else:
    print("Error, please try again")

if point1y > tmidy:
    ypos = "Above"
elif point1y < tmidy:
    ypos = "Below"
elif point1y == tmidy:
    ypos = "Same y"
else:
    print("Error, please try again")

print("Relative to your triangle your point is:", xpos, "and", ypos)
