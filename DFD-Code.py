print("Hello Welcome to Nafisa's Shoe Shop")
shoe_size = int(input("Please enter your shoe size: "))
if shoe_size > 6:   
    print("You will need to shop from the Adult Section")
else:
    print("You will need to shop from the Junior Section")

print("Please choose from our three different brands which are Nike, Addidas or Vans")

Brand = input("Which Shoe Brand would you like to buy: Nike, Addidas and Vans: ")

beg_sen = "You are a "

print(beg_sen + str(shoe_size) + " and have ordered "+ Brand + ".")
print("We have your order, Thank you for shopping at Nafisa's Shoe Shop")
