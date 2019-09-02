"""
Home Grown Gill
 is a local business that wants to computerise their boxed food orders for click and collect options.
 Specifically, they want to be able to enter customer details, specific items ordered and pick-up or delivery
 requirements into a computer while displaying their wares at a farmer’s market (which they do every weekend)
  and have this program display the delivery details, itemised order, and total cost, which can then be printed off.
  Follow up orders generally consist of a specific box size (small, medium, large) with chosen items from a database
  that changes weekly (fruits, veggies, milk products, nuts, jams and juices).  Your task is to create a PROTOTYPE
  program to emphasize the usability of such an application which can be used by customers at a market.



  Decomposition:
  1: Create menu(dictionary)
  1.5: Allow items to be added to menu
  2: Ask for name and address
  2.5 Allow people to order and store the order
  2.75 Allow parts of the order to be deleted
  2.8 Calculate Price
  3: Pickup and delivery functions
  3.5 Create system so user can choose what to do
  4: Box Size
  5: Present Menu
  6: Present final order with details

    Do:
    make a loop function
"""
import math

# set up a loop for the final program
program_loop = True

# create a dictionary for the menu
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
        'apple juice': {
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

# order will be filled via a function
order = {

}


# create a function that asks for the users details
def identity():
    # set up a loop
    phone_loop = True
    # address = input("What is your address?")
    global name_input
    global phone_num
    # phone number loop
    while phone_loop:
        # ask for name and address
        name_input = str(input("Hello Welcome to Home Grown Gill. What is your name?"))
        # ask for phone number
        phone_num = str(input("What is your phone number?"))
        try:
            # convert phone to a number and check it is a number greater than zero
            if int(phone_num) < 0:
                print("Please enter a valid phone number.")
                # continue
            # if there are no letters in the name
            elif not name_input.split():
                print("Please enter a valid name.")
            # if everything is all good end the loop
            else:
                phone_loop = False
        # if the phone number is not a number repeat
        except ValueError:
            print("Please enter a valid phone number.")
    return name_input, phone_num


# create a function that allows user to add to the menu
def add_menu(dictionary, cost2):
    # set up a loop
    menu_loop = True
    while menu_loop:
        try:
            try:
                # ask what type of food they will like add
                catagory = str(input("What food item will you like to add? (Fruit, Vegetables, Milk Products, "
                                     "Nuts, Jams or Juices) or you can cancel (c). ").lower())
                # print(catagory)
                # if the user wanted to cancel break the loop
                if catagory == 'c' or catagory == 'cancel':
                    return catagory
                # ask what food item they want to add and how much each will cost
                item = input("What food item will you like to add?").lower()
                cost = float(input("What will be the cost of this item?").lower())
                if not item.split():
                    print("Please enter a valid item")
                elif cost <= 0:
                    print("Please enter a cost above zero.")
                else:
                    # print(item)
                    # print(cost)
                    # add the item to the menu
                    dictionary[catagory][item] = {cost2: cost}
                    # menu_loop = False
                    return catagory
            # check for any errors
            except KeyError:
                print("Please enter a correct food catagory.")
        except ValueError:
            print("Please enter a valid number.")


# function for calculating box sizes
def box_or_paper(price, order_dict):
    # set up a loop for validation
    box_loop = True
    while box_loop:
        # would the user like paper bags or boxes
        paper = input("Would you like paper bags (pb) or boxes (b). Please note paper bags will cost an extra $1."
                      "".lower())

        # if the user chose paper bags
        if paper == 'pb' or paper == 'paper bags':
            # print("Plastic")
            print("Your order will be packaged in paper bags.")
            # add one dollar to the price
            paper_price = price + 1
            # return the new price
            return paper_price
            # stop the loop
            # box_loop = False

        # if the user chose boxes
        elif paper == 'b' or paper == 'boxes':
            global box_number
            global box_size
            # print("Boxes")
            # set the quantity to zero to ensure it starts as zero
            quantity = 0
            # loop through every item in the order
            for item in order_dict:
                # increase the overall quantity by the current item quantity and previous quantities
                quantity = order_dict[item]['quantity'] + quantity
            # print out total number of items
            print("Total quantity of item(s): {}.".format(quantity))
            # if the quantity is smaller than 10 use small boxes
            if quantity < 10:
                box_size = 'small'
                # calculate number of small boxes required
                box_number = quantity / 5
            # if the quantity is between 10 and 19 use medium boxes
            # elif quantity < 20 and quantity >= 10:
            elif 20 > quantity >= 10:
                box_size = 'medium'
                # calculate number of medium boxes required
                box_number = quantity / 10
            # if the quantity is above 20 use large boxes
            elif quantity >= 20:
                box_size = 'large'
                # calculate number of large boxes required
                box_number = quantity / 20
            # round up box number as you can't have 1.5 boxes
            box_number_rounded = math.ceil(box_number)
            # print out number of ____ boxes
            print("{} {} boxes.".format(box_number_rounded, box_size.capitalize()))
            # return the original price
            return price

            # large = quantity / 20
            # medium = quantity / 10
            # small = quantity / 5
            # print(large, medium, small)
            # stop loop
            # box_loop = False
        # if user entered wrong input do this
        else:
            print("Please enter pb or b.")


# create a function that can order items
def order_items(menu_dict, order_dict):
    # setup a loop
    order_loop = True
    while order_loop:
        try:
            try:
                # ask what item they would like to get
                item = input("What food item would you like to purchase. Or would you like to cancel (c).").lower()
                # if the user wants to cancel break the loop
                if item == 'c' or item == 'cancel':
                    return item
                # ask how many of the item they would like
                quantity = int(input("How many of this item would you like?"))
                # ensure that quantity is above zero
                if quantity <= 0:
                    print("Please enter an quantity above zero.")
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
                            # order_loop = False
                            return item
            # check for errors
            except ValueError:
                print("Please enter a valid quantity.")
        except KeyError:
            print("Please enter a valid  name.")


# set this up as a function - output order
def print_dict(statement, dictionary):
    # if it is the order dictionary do this
    if dictionary == order:
        # set the price to zero
        price = 0
        print(statement)
        print("---------")
        # loop through entire order dictionary to print whole order
        for item, info in dictionary.items():
            # calculate prices of each item
            past_price = price
            price = (dictionary[item]['price'] * dictionary[item]['quantity'])
            # round the price value to 2DP
            price = round(price, 2)
            # print the item eg: oranges or milk
            print(item.title())
            # print the price and quantity of the items and the overall price of the item
            print("Price: ${}.".format(info['price']))
            print("Quantity: {}.".format(info['quantity']))
            print("Item Price: ${}.".format(price))
            price = past_price + price
            print()
        # print total order price
        print("Total Price: ${}.".format(price))
        print("---------")
    else:
        # do this for menu dictionary
        print(statement)
        print("----------")
        # go through the entire menu
        for category, food in dictionary.items():
            # print the catagory eg fruit or vegetables
            print("{}:".format(category.title()))
            print()
            for fruit, info in food.items():
                # print each item and its price
                print(fruit.title())
                print("Price: ${}.".format(info['price']))
                print()

            print("---------")


# create a function that can loop other functions
def loop_function(function, param1, param2, question):
    loop = 'y'
    # loop when answer is yes
    while loop == 'y' or loop == 'yes':
        # print("hi")
        # if the wanted function has only one parameter do this
        if param2 == 'no':
            # call the function
            cancel = function(param1)
        else:
            # call the function
            cancel = function(param1, param2)
        loop2 = True
        # validation loop
        if cancel == 'c' or cancel == 'cancel':
            break
        while loop2:
            # ask a yes or no question eg do you want to order another item
            loop = input("{} y/n".format(question)).lower()
            # if yes or no break validation loop and it will either break or repeat orginal loop
            if loop == 'y' or loop == 'yes' or loop == 'n' or loop == 'no':
                break
            # if response is not yes or no try again
            else:
                print("Please enter y or n.")
    print()


# create a function that gets the user to chose pickup or delivery
def pickup_delivery(phone_number, price):
    # set up a loop
    pick_loop = True
    while pick_loop:
        # ask if they want pickup or delivery
        pickup_or_delivery = input("Would you like to pickup (p) or get your food delivered (d). Please note that "
                                   "an extra $3 will be added to your price for a delivery.").lower()
        # if the user chose pickup
        if pickup_or_delivery == "p" or pickup_or_delivery == "pickup":
            print("Your order will be available at Home Grown Gill for Pickup. We will call you on {} when it is ready"
                  " for pickup.".format(phone_number))
            print("")
            # return new price as nothing is being added
            return price
            # stop the loop
            # pick_loop = False
        # if the user chose delivery
        elif pickup_or_delivery == "d" or pickup_or_delivery == "delivered" or pickup_or_delivery == 'delivery':
            # ask the user their address
            address = input("What is your address.")
            print("Your order will be delivered to {}.".format(address))
            print("")
            # add three dollars to the price for delivery
            new_price = price + 3
            # return the new price
            return new_price
            # stop the loop
            # pick_loop = False
        else:
            print("Please enter p or d.")


# create a a function that can delete things off order
def delete_order(order_dict):
    # create a loop
    del_loop = True
    while del_loop:
        try:
            try:
                # if there is nothing in the order price will be zero
                price = calculate_price(order_dict)
                # if price is zero stop and tell them to order an item before removing one
                if price == 0:
                    print("Please order an item before trying to delete one.")
                    quantity_or_item = 'c'
                    return quantity_or_item
                # check if the user wants to delete an item remove a quantity or cancel
                quantity_or_item = input("Would you like to delete a quantity (q) or an item (i) or cancel (c)? ")\
                    .lower()
                # if they want to remove a quantity
                if quantity_or_item == "q" or quantity_or_item == "quantity":
                    # ask which item to remove a quantity from
                    item = input("What item would you like to remove a quantity from? ").lower()
                    # how much of the item do they want to remove
                    quantity = int(input("How many of this item would you like to remove? "))
                    # check the number entered is greater than zero
                    if quantity <= 0:
                        print("Please enter a quantity larger than zero. ")
                    else:
                        # ensure that the item entered is in the order
                        if item in order_dict:
                            # make sure the quantity doesn't go below zero
                            if order_dict[item]['quantity'] - quantity > 0:
                                # remove the quantity from the item
                                order_dict[item]['quantity'] = order_dict[item]['quantity'] - quantity
                                # stop loop
                                # del_loop = False
                                return quantity_or_item
                            # if the quantity goes below zero retry
                            else:
                                print("Please enter a quantity smaller than the current quantity.")
                        # if the item isn't in the order
                        else:
                            print("Please enter a valid item.")
                # if the user chose to remove an item
                elif quantity_or_item == "i" or quantity_or_item == "item":
                    # ask what item the user would like to remove
                    item = input("What item would you like to remove? ")
                    # ensure the item is in the order
                    if item in order_dict:
                        order_dict.pop(item)
                        # del_loop = False
                        return quantity_or_item
                    # if item isn't in the order
                    else:
                        print("Please enter a valid item.")
                # if the user chose cancel break the loop
                elif quantity_or_item == 'c' or quantity_or_item == 'cancel':
                    return quantity_or_item

                # if the user didn't input a correct option
                else:
                    print("Please enter either q, i or c.")
            # if there are any errors
            except ValueError:
                print("Please enter a whole number quantity above zero.")
        except KeyError:
            print("Please enter an item that you have ordered.")


# function that can calculate the price of the order
def calculate_price(order_dict):
    # set the price to zero to ensure it starts at zero
    price = 0
    # loop through every item in the order
    for item in order_dict:
        # the price for the previous item and items before is now saved
        past_price = price
        # calculate the price of an item
        price = (order_dict[item]['price'] * order_dict[item]['quantity'])
        # add the new price to the past price to get the price of current item and all items before
        price = past_price + price
    # return the price so it can be added to with extra costs
    return price


# put the program in a function
def program(loop):
    # find the users name and phone number
    name, phone = identity()
    # delete order to clear any past orders
    order.clear()
    # print(name, address, phone)
    # welcome the user
    print("Welcome {}. What would you like to do. Please the corresponding number to the task. Eg 1, 2, 3.".format
          (name.title()))

    while loop:
        # give the user a choice of what they want to do
        choice = input("""
    Home Grown Gill
    -----------------
    1. View the Menu
    2. Add to the Menu
    3. Order Items
    4. Delete Items from Order
    5. View Order and Price (Note: Delivery and Paper Bags do add to the price)
    6. Finish your order and chose Paper Bags or Boxes and chose Pickup or Delivery
    7. Cancel your order and end the program
        """)

        # if the user wants to view the menu
        if choice == '1':
            # print the menu
            print_dict('Menu:', menu)
        # if the user wants to add to the menu
        elif choice == '2':
            # call the function that adds to the menu and loop it
            loop_function(add_menu, menu, 'price', "Would you like to add another item to the menu?")
            # add_menu(menu, 'price')
        # if the user wants to order an item
        elif choice == '3':
            # display the menu
            print_dict('Menu:', menu)
            # run the order item function and loop it
            loop_function(order_items, menu, order, 'Would you like to order another item?')
            # display order
            print_dict("Your Order:", order)
        # if the user wants to remove an item from their order
        elif choice == '4':
            # display their order
            print_dict("Your Order:", order)
            # run the delete order function and loop it
            loop_function(delete_order, order, 'no', "Would you like to remove another item?")
        # if the user wants to view their order
        elif choice == '5':
            # print out the order
            print_dict("Your Order:", order)
        # if the user is finished and wants to chose pickup and delivery and boxes
        elif choice == '6':
            # calculate the final price of the order
            order_price = calculate_price(order)
            # if the order price is zero tell them to order some items
            if order_price == 0:
                print("Please make an order.")
            # if the order has a price
            else:
                # chose boxes or paper bags and if it is paper bags add to the cost
                box_price = box_or_paper(order_price, order)
                # chose pickup and delivery and if delivery add to the cost
                final_price = pickup_delivery(phone, box_price)
                # thank customer and display order
                print("Thanks {} for shopping at Home Grown Gill. Please come again.".format(name))
                print_dict("Your Order:", order)
                # display final price
                print("Your final price with any extra charges is ${}.".format(final_price))
                loop = False
        # if the user wants to cancel their order
        elif choice == '7':
            # set up a loop to validate yes or no for cancel
            cancel_loop = True
            global cancel_answer
            while cancel_loop:
                # check if they want to cancel
                cancel_answer = input("Are you sure you want to cancel? y / n.").lower()
                # if they input yes or no break the validation loop
                if cancel_answer == 'yes' or cancel_answer == 'y' or cancel_answer == 'n' or cancel_answer == 'no':
                    cancel_loop = False
                # if they didn't put in yes or no retry
                else:
                    print("Please enter y or n.")
            # if yes break the loop and finish the program
            if cancel_answer == 'y' or cancel_answer == 'yes':
                break
        # if a number is entered retry
        else:
            print("Please enter a number corresponding to a task eg; 1 2 3.")


# program(program_loop)
# allow program to be repeated to make another order and run the program
loop_function(program, program_loop, 'no', "Would you like to make another order?")
