import random
Username = input("Hello! What is your name?")
number1 = random.randint(1, 30)
number2 = random.randint(31, 60)
number3 = random.randint(61, 100)
guess= int(input("What is your favourite number?:"))
joke1 = ("Why did the M&M go to school, because it wanted to be a smartie.")
joke2 = ("Two artists had a contest, it ended in a draw.")
joke3 = ("What did the traffic light say to the car, look away! i am changing.")
if guess<number1:
    print (joke1)
elif guess<number2:
    print (joke2)
elif guess<number3:
    print (joke3)
else:
    print("Sorry, try again later")