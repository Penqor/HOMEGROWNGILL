'''
See if I can display the menu in a new format
'''

menu = {
    # type of food
    'fruit': {
        # food item
        'apples': {
            # price of item
            'price': 1
        },
        'oranges': {
            'price': 1
        },
        'bananas': {
            'price': 2
        },
        'mandarins': {
            'price': 1.5
        }
    },
    'vegetables': {

        'carrots': {
            'price': 2
        },
        'broccoli': {
            'price': 0.5
        },
        'peas': {
            'price': 1
        },
        'lettuce': {
            'price': 1.5
        }
    },
    'milk products': {
        'milk': {
            'price': 3
        },
        'butter': {
            'price': 1.5
        },
        'ice cream': {
            'price': 4
        },
        'yogurt': {
            'price': 2
        }
    },
    'nuts': {
        'peanuts': {
            'price': 0.5
        },
        'pistachios': {
            'price': 0.6
        },
        'walnuts': {
            'price': 0.8
        },
        'cashews': {
            'price': 0.4
        }
    },
    'jams': {
        'strawberry jam': {
            'price': 2.8
        },
        'raspberry jam': {
            'price': 2.8
        },
        'apricot jam': {
            'price': 4.5
        }
    },
    'juices': {
        'orange juice': {
            'price': 5
        },
        'apples juice': {
            'price': 4.5
        },
        'cranberry juice': {
            'price': 5.5
        },
        'grapefruit juice': {
            'price': 3
        }
    }
}

def print_dict(statement, dictionary):
    # if it is the order dictionary do this
    """if dictionary == order:
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
    else:"""
    # do this for menu dictionary
    print(statement)
    print("----------")
    # go through the entire menu
    for category, a in dictionary.items():
        # print the catagory eg fruit or vegetables
        print(category.capitalize())
        print("                                          ")
        print()
    for fruit, info in a.items():
        # print each item and its price
        print(fruit.capitalize())
        print("Price: ${}".format(info['price']))
        print()

        print("---------")

print_dict("Menu:", menu)