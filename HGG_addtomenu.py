"""
  1.5: Allow items to be added to menu
"""
# create a dictionary for the menu
add = 'y'
menu = {
    'fruit': {
        'apples': {
            'price': 4
        },
        'oranges': {
            'price': 2
        }
    },
    'vegetables:': {
        'carrots': {
            'price': 2
        }
    },
    'milk products': {
        'milk': {
            'price': 5
        }
    },
    'nuts': {
        'peanuts': {
            'price':0.5
        }
    },
    'jams': {
        'jelly': {
            'price': 4
        }
    },
    'juices': {
        'orange juice': {
            'price': 5
        }
    }
}

# adds apple juice to juices
menu['juices']['apple'] = {'price': 5}
# replaces all of the key
# menu['juices:'] = {'apple': {'price:': 5}}


# create a function that allows user to add to the menu
def add_menu(dict, cost2):
    # set up a loop
    menu_loop = True
    while menu_loop:
        try:
            try:
                # ask what type of food they will like add
                catagory = str(input("What food item will you like to add? (Fruit, Vegetables, Milk Products, "
                                     "Nuts, Jams or juices ").lower())
                # print(catagory)
                # ask what food item they want to add and how much each will cost
                item = input("What food item will you like to add?").lower()
                cost = int(input("What will be the cost of this item?").lower())
                # print(item)
                # print(cost)
                # add the item to the menu
                dict[catagory][item] = {cost2: cost}
                menu_loop = False
            # check for any errors
            except KeyError:
                print("Please enter a valid input.")
        except ValueError:
            print("Please enter a valid input.")


# basic loop to redo adding to menu
while add == 'y':
    add_menu(menu,'price')
    add = input("Would you like to add another item? y/n")

# print out dictionary in a way that displays the different keys in an order for the menu
for category, a in menu.items():
    print(category)

    for fruit, info in a.items():
        print(fruit)
        print("price: ${}".format(info['price']))

    print()