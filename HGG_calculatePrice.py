"""
  2.8 Calculate Price
"""
# random order to calculate price with
order = {'apples': {'price': 4, 'quantity': 5}, 'oranges': {'price': 2, 'quantity': 2}, 'milk': {'price': 5, 'quantity': 22}, 'orange juice': {'price': 5, 'quantity': 4}, 'peanuts': {'price': 0.5, 'quantity': 8}}

# create a function which calculates price
def calculate_price(order_dict):
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

    # after going through all items print he final price
    # print("Your final price is: ${}".format(price))
    return price


# call the price function
final_price = calculate_price(order)
print(final_price)