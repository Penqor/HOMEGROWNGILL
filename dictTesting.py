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


def printDict(statement, dictionary):
    if dictionary == 'order':
        print(statement)
        for category, a in dictionary.items():
            print(category)
            print("--------")
            for fruit, info in a.items():
                print(fruit)
                print("Price: ${}".format(info['price']))
                print("Quantity: {}".format(info['quantity']))
                print()
        print("---------")
    else:
        print(statement)
        print("----------")
        for category, a in dictionary.items():
            print(category)
            print()
            for fruit, info in a.items():
                print(fruit)
                print("Price: ${}".format(info['price']))
                print()

            print("---------")

printDict("Order:", menu)
print(menu)