print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 120
        print("Child tickets are 120CZK.")
    elif age <= 18:
        bill = 150
        print("Youth tickets are 150CZK.")
    else:
        bill = 270
        print("Adult tickets are 270CZK.")

    price_w_photo = input("Do you want to have a photo take? Type y for Yes n for No.")
    if price_w_photo == "y":
        price_w_photo = bill + 100
        print(f"Photo take costs additional 100CZK. Your full price for a ticket is {price_w_photo}")
    else:
        print(f"Your full price of ticket is {bill}")

else:
    print("Sorry you have to grow taller before you can ride. :(")