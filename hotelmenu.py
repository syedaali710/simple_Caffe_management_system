#we are using dictionary
#define menu
menu = {
    'pizza':40,
    'burger':50,
    'biryani':13,
    'pasta':25,
    'coffe':14,
    'salad':18,
}

#greet
print("welcome to sammy restaurant")
print("pizza: 40\npasta: 25\nburger: 50\nbiryani: 13\ncoffee: 14\nsalad: 18")

order_total = 0
#40+50 = 90

item_one = input("enter ur order: ")
if item_one in menu:
    order_total+= menu[item_one] #0+40 it will add pizza price in 0
    print(f"your item {item_one} is added")

else:
    print("pls order from the menu")

order_another = input("do u want anything else? Yes/No ")
if order_another == "yes":
    item_two = input("Enter second item = ")
    if item_two in menu:
        order_total += menu[item_two]
    else:
        print("pls order from the menu")

print(f"the total amount is {order_total}")