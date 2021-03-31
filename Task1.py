#Task 1 Question A
import random
number = random.randint(1,10)
print("The random number is ", number)

#Task 1 Question B
Name = input("Enter your name: ")

#Task 1 Question C&D

Guessnumber = int(input("Guess a number from 1 - 10: "))
if Guessnumber == 1 or Guessnumber == 2 or Guessnumber == 3 or Guessnumber == 4 or Guessnumber == 5 or Guessnumber == 6 or Guessnumber == 7 or Guessnumber == 9 or Guessnumber == 10:
    print("You have guessed incorrectly")
else:
    print("You have guessed correctly")

