"""
  2.75 Allow parts of the order to be deleted

"""
# random dictionary
order = {'apples': {'price': 4, 'quantity': 5}, 'oranges': {'price': 2, 'quantity': 2}, 'milk': {'price': 5, 'quantity': 22}, 'orange juice': {'price': 5, 'quantity': 4}, 'peanuts': {'price': 0.5, 'quantity': 8}}

# create a a function that can delete things off order
def delete_order(order_dict):
    # create a loop
    del_loop =  True
    while del_loop:
        try:
            try:
                # check if the user wants to delete an item remove a quantity or cancel
                quant_or_item = input("Would you like to delete a quantity (q) or an item (i) or cancel (c)? ")
                # if they want to remove a quantity
                if quant_or_item == "q" or quant_or_item == "quantity":
                    # ask which item to remove a quantity from
                    item = input("What item would you like to remove a quantity from? ")
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
                                del_loop = False
                            # if the quantity goes below zero retry
                            else:
                                print("Please enter a quantity smaller than the current quantity.")
                        # if the item isn't in the order
                        else:
                            print("Please enter a valid item.")
                # if the user chose to remove an item
                elif quant_or_item == "i" or quant_or_item == "item":
                    # ask what item the user would like to remove
                    item = input("What item would you like to remove? ")
                    # ensure the item is in the order
                    if item in order_dict:
                        order_dict.pop(item)
                        del_loop = False
                    # if item isn't in the order
                    else:
                        print("Please enter a valid item.")
                # if the user chose cancel break the loop
                elif quant_or_item == 'c' or quant_or_item == 'cancel':
                    break

                # if the user didn't input a correct option
                else:
                    print("Please enter either q, i or c.")
            # if there are any errors
            except ValueError:
                print("Please enter a whole number quantity above zero.")
        except KeyError:
            print("Please enter an item that you have ordered.")

# call the function
delete_order(order)
# print the order to see if it worked
print(order)