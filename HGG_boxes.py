"""
  4: Box Size

Determine paper or boxes
Work out smallest possible number of a box size
Chose that box size
Large = 20 items
Medium = 10 items
Small = 5 items
"""
# import math library for later calculations
import math

# random order for testing
order = {'apples': {'price': 4, 'quantity': 5}, 'oranges': {'price': 2, 'quantity': 2}, 'milk': {'price': 5, 'quantity': 22}, 'orange juice': {'price': 5, 'quantity': 4}, 'peanuts': {'price': 0.5, 'quantity': 8}}

# function for calculating box sizes
def box_size(order_dict):
    # set up a loop for validation
    box_loop = True
    while box_loop:
        # would the user like paper bags or boxes
        paper = input("Would you like paper bags (pb) or boxes (b). Please note paper bags will cost an extra $1.".lower())
        # if the user chose paper bags
        if paper == 'pb' or paper == 'paper bags':
            # print("Plastic")
            print("Your order will be packaged in paper bags")
            # return paper bags for adding to price later
            return paper
            box_loop = False
        # if the user chose boxes
        elif paper == 'b' or paper == 'boxes':
            # print("Boxes")
            # set the quantity to zero to ensure it starts as zero
            quantity = 0
            # loop through every item in the order
            for item in order_dict:
                # increase the overall quantity by the current item quantity and previous quantities
                quantity = order_dict[item]['quantity'] + quantity
            # print out total number of items
            print("Total quantity of item(s): {}".format(quantity))
            # if the quantity is smaller than 10 use small boxes
            if quantity < 10:
                box_size = 'small'
                # calculate number of small boxes required
                box_number = quantity / 5
            # if the quantity is between 10 and 19 use medium boxes
            elif quantity < 20 and quantity >= 10:
                box_size = 'medium'
                # calculate number of medium boxes required
                box_number = quantity / 10
            # if the quantity is above 20 use large boxes
            elif quantity >= 20:
                box_size = 'large'
                # calulate number of large boxes required
                box_number = quantity / 20
            # round up box number as you can't have 1.5 boxes
            box_number = math.ceil(box_number)
            # print out number of ____ boxes
            print("{} {} boxes".format(box_number, box_size.capitalize()))

            # large = quantity / 20
            # medium = quantity / 10
            # small = quantity / 5
            # print(large, medium, small)
            # stop loop
            box_loop = False
        # if user entered wrong input do this
        else:
            print("Please enter pb or b")

# call function
box_size(order)
# allow varaible to be equal to input for later
bag_or_box = box_size(order)
# if the input is paper bags
if bag_or_box == "pb" or bag_or_box == "paper bags":
    # add one doller to price note that this will be the price value previously calculated
    price = 0
    price += 1
