"""
  1: Create menu(dictionary)

"""
#create a dictionary for the menu
menu = {
    # type of food
    'fruit:': {
        # food item
        'apples': {
            # price of item
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

# print out dictionary in a way that displays the different keys in an order for the menu

# print out the menu nicely
# loop through catagories eg fruit, vegetables
for category, value in menu.items():
    # print the catagory
    print(category)
    # loop through each item in the catagory
    for item, info in value.items():
        # print the item and price
        print(item)
        print("price: ${}".format(info['price']))

    print()
