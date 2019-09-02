# create a dictionary for the menu
menu = {
    'fruit:': {
        'apples': {
            'price': 4
        },
        'oranges':{
            'price': 2
        }
    },
    'vegetables:':{
        'carrots':{
            'price': 2
        }
    },
    'milk products:': {
        'milk': {
            'price': 5
        }
    },
    'nuts:': {
        'peanuts': {
            'price':0.5
        }
    },
    'jams:': {
        'jelly': {
            'price': 4
        }
    },
    'juices:': {
        'orange juice': {
            'price': 5
        }
    }
}


# order will be filled via a function
order = {

}
# order = {'apple juice': {'price:': 5, 'quantity:': 10}}


# create a function that can order items
def order_items(menu_dict, order_dict):
    # setup a loop
    order_loop = True
    while order_loop:
        try:
            try:
                # ask what item they would like to get
                item = input("What food item would you like to purchase")
                # ask how many of the item they would like
                quantity = int(input("How many of this item would you like"))
                # ensure that quantity is above zero
                if quantity <= 0:
                    print("Please enter an quantity above zero")
                else:
                    # if the item is already in the order add to the quantity
                    if item in order_dict:
                        order_dict[item]['quantity'] = order_dict[item]['quantity'] + quantity
                        order_loop = False
    
                    else:
                        # go through the menu and look for the item
                        for catagory, value in menu_dict.items():
                            # if the item is in the menu
                            if item in list(value.keys()):
                                # add the item to the order
                                order_dict[item] = {'price': value[item]['price'], 'quantity': quantity}
                                break
                        # if the item is not in the order as it won't have been on the menu
                        if item not in order_dict:
                            print("Please enter an item on the menu.")
                            order_loop = True
                        else:
                            order_loop = False
            # check for errors
            except ValueError:
                print("Please enter a valid quantity.")
        except KeyError:
            print("Please enter a valid  name.")

def final_price(order_dict):
    # set the price to zero to ensure it starts at zero
    price = 0
    # loop through every item in the order
    for item in order_dict:
        # the price for the previous item and items before is now saved
        past_price = price
        # calculate the price of an item
        price = (order_dict[item]['price'] * order_dict[item]['quantity'])
        # print item and its price
        # print(item.capitalize())
        # print("Total item price is: ${}".format(price))
        # print()
        # add the new price to the past price to get the price of current item and all items before
        price = past_price + price

# set this up as a function - output order
def printDict(statement, dictionary):
    # if it is the order dictionary do this
    if dictionary == order:
        price = 0
        print(statement)
        print("---------")
        # loop through entire order dictionary to print whole order
        for item, info in dictionary.items():
            # calculate prices of each item
            past_price = price
            price = (dictionary[item]['price'] * dictionary[item]['quantity'])
            # print the item eg: oranges or milk
            print(item.capitalize())
            # print the price and quantity of the items and the overall price of the item
            print("Price: ${}".format(info['price']))
            print("Quantity: {}".format(info['quantity']))
            print("Item Price: ${}".format(price))
            price = past_price + price
            print()
        # print total order price
        print("Total Price: ${}".format(price))
        print("---------")
    else:
        # do this for menu dictionary
        print(statement)
        print("----------")
        # go through the entire menu
        for category, a in dictionary.items():
            # print the catagory eg fruit or vegetables
            print(category.capitalize())
            print()
            for fruit, info in a.items():
                # print each item and its price
                print(fruit.capitalize())
                print("Price: ${}".format(info['price']))
                print()

            print("---------")


def loop_function(function, param1, param2, question):
    loop = 'y'
    # loop when answer is yes
    while loop == 'y' or loop == 'yes':
        # call the function you want to loop
        # print("hi")
        function(param1, param2)
        Loop2 = True
        # validation loop
        while Loop2:
            loop = input("{} y/n".format(question))
            # if yes or no break validation loop and it will either break or repeat orginal loop
            if loop == 'y' or loop == 'yes' or loop == 'n' or loop == 'no':
                break
            # if response is not yes or no try again
            else:
                print("Please enter y or n")
    print()
# loop = 'y'
'''
while loop == 'y' or loop == 'yes':
    # call the function you want to loop
    order_items(menu, order)
    Loop2 = True
    # validation loop
    while Loop2:
        loop = input("Would you like to order another item? y/n")
        # if yes or no break validation loop and it will either break or repeat orginal loop
        if loop == 'y' or loop == 'yes':
            Loop2 = False
        elif loop == 'n' or loop == 'no':
            Loop2 = False
        # if response is not yes or no try again
        else:
            print("Please enter y or n")
'''
# display the menu
printDict("Menu:", menu)
print()
# loop the order function
loop_function(order_items, menu, order, "Would you like to order another item?")
# print out order
printDict("Your Order:", order)
# print(order)