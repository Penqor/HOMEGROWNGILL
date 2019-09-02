"""
  3: Pickup and delivery functions

"""
# create a function
def pick_del():
    # set up a loop
    pick_loop = True
    while pick_loop:
        # ask if they want pickup or delivery
        choice = input("Would you like to pickup (p) or get your food delivered (d)").lower()
        # if the user chose pickup
        if choice == "p" or choice == "pickup":
            pick_loop = False
        # if the user chose delivery
        elif choice == "d" or choice == "delivered":
            address = input("What is your address")
            print("Your order will be delivered to {}.".format(address))
            pick_loop = False
            # add three dollers to order
