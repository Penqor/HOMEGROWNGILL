"""
Do:
    make a loop function
"""

# old code commented out
'''
def loopFunction(function, question):
    Loop = 'y'
    # loop when answer is yes
    while Loop == 'y' or Loop == 'yes':
        # call the function you want to loop
        function
        Loop2 = True
        # validation loop
        while Loop2:
            Loop = input("{} y/n".format(question))
            # if yes or no break validation loop and it will either break or repeat orginal loop
            if Loop == 'y' or Loop == 'yes':
                Loop2 = False
            elif Loop == 'n' or Loop == 'no':
                Loop2 = False
            # if response is not yes or no try again
            else:
                print("Please enter y or n")

def printDict(dictionary):
    for category, a in dictionary.items():
        print(category)

        for fruit, info in a.items():
            print(fruit, info)

        print()
'''
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
        'orange': {
            'price': 5
        }
    }
}


# order will be filled via a function
order = {

}
# order = {'apple juice': {'price:': 5, 'quantity:': 10}}


def order_items(menu_dict, order_dict):
    order_loop = True
    while order_loop:
        try:
            try:
                item = input("What food item would you like to purchase")
                quantity = int(input("How many of this item would you like"))
                if item in order_dict:
                    order_dict[item]['quantity'] = order_dict[item]['quantity'] + quantity
                    order_loop = False
                else:
                    for category, value in menu_dict.items():
                        if item in list(value.keys()):
                            order_dict[item] = {'price': value[item]['price'], 'quantity': quantity}
                            break
                    if item not in order_dict:
                        print("Please enter an item on the menu.")
                        order_loop = True
                    else:
                        order_loop = False
            except ValueError:
                print("Please enter a valid quantity.")
        except KeyError:
            print("Please enter a valid  name.")


# set this up as a function - output order
def printDict(statement, dictionary):
    print(statement)
    for category, a in dictionary.items():
        print(category)

        for fruit, info in a.items():
            print(fruit, info)

        print()


# set up the mechanics of the whole order as a function!!
def loop_function(function, param1, param2, question):

    Loop = 'y'
    # loop when answer is yes
    while Loop == 'y' or Loop == 'yes':
        # call the function you want to loop
        print("hi")
        function(param1, param2)
        Loop2 = True
        # validation loop
        while Loop2:
            Loop = input("{} y/n".format(question))
            # if yes or no break validation loop and it will either break or repeat original loop
            if Loop == 'y' or Loop == 'yes' or Loop == 'n' or Loop == 'no':
                break
            # if response is not yes or no try again
            else:
                print("Please enter y or n")


# call the function and print order
loop_function(order_items, menu, order, "Would you like to order another item.")
printDict("Your Order:", order)