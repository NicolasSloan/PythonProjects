import time
print("We're going to figure out how old you are in years and months!")

Age=int(input('How old are you? '))
print("You said " + str(Age) + " years old")
time.sleep(.5)
Months = Age*12
print("That means you are " + str(Months) + " months old!")
time.sleep(.5)

Minutes=Age*525600
Seconds=Age*31536000
print("This also means that you are " +str(Minutes) + " minutes old, and "
      +str(Seconds)+ " seconds old!!")
