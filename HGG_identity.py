"""
  2: Ask for name and address

"""
# create a function that asks for the users details
def identity():
    # set up a loop
    phoneLoop = True
    # ask for name and address
    name = input("Hello Welcome to Home Grown Gill. What is your name?")
    address = input("What is your address?")
    # phone number loop
    while phoneLoop:
        # ask for phone number
        phone = str(input("What is your phone number?"))
        try:
            # convert phone to a number and check it is a number greater than zero
            if int(phone) <0:
                print("Please enter a valid phone number.")
                continue
            # if everything is all good end the loop
            else:
                phoneLoop = False
        # if the phone number is not a number repeat
        except ValueError:
            print("Please enter a valid phone number.")
    return name, address, phone


name, address, phone = identity()
print(name, address, phone)
