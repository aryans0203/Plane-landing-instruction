requiredAltitude=1000
currentAltitude=int(input("enter your altitude in ft :-"))

if currentAltitude<=requiredAltitude:
    print("You are clear to land the plane")
elif currentAltitude>=requiredAltitude and currentAltitude<5000:
    print("come down to 1000ft and then land")
else:
    print("you are too high go around and try again later")
