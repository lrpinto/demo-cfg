# DEMO EXAMPLES TO SUPPORT SLIDES
# student's do not have these examples in their version
# all examples can be shared via GitHub at the end of the session.

"""
Example 1

Copy over the inputs to demo the function.
GOOD INPUT: add_vat(vat=20, prices=[24, 0.15, 32.45, 0])
BAD INPUT: add_vat(vat=20, prices=[24, 0.15, '10', 32.45]) --> it has a string in the list, hence it fails.

You can also discuss what would happpen if there is None, string, int, float or even a data structure like another list,
tuple, dict.
"""

def add_vat(vat, prices):
    """
    Add commission to every price item in the provided iterable.

    :param vat: float, vat percentage
    :param prices: iterable, net prices as per customers' receipt
    :return: list of prices with added vat
    """
    new_prices = [(price / 100 * vat) + price for price in prices]
    return new_prices


def apply_discount(product, discount):
    """
    Add a discount to the price.
    :param product: dict obj, item spec including price
    :param discount: float discount expressed in percent
    :return: float new price
    """
    price = round(product['price'] * (1.0 - (discount / 100)), 2)
    assert 0 <= price <= product['price']
    return price


#### VALID INPUT (comment / uncomment  to use as necessary)###
# trainers = {'name': 'Running Trainers', 'price': 79.99}
# discount  = 25 #(represents 25%)
# print(apply_discount(trainers, discount))


#### INVALID INPUT (comment / uncomment to use  as necessary)###
# trainers = {'name': 'Running Trainers', 'price': 79.99}
# discount  = 200 #(represents 200%) --> Assertion Error will be raised
# print(apply_discount(trainers, discount))


################## MORE DEMO EXAMPLES ########################


class AuthorisationError(Exception):
    pass


gym_members = []


def cancel_membership(membership_id, user):
    """
    Canel Gym membership for an existing member.
    """
    if not user.is_admin():
        raise AuthorisationError('Must be admin to cancel')
    if not gym_members.membership_exists(membership_id):
        raise ValueError('Unknown id')

    gym_members.find_membership(membership_id).delete()


"""
Comment or uncomment the below examples as required
"""

# EXAMPLE 1 - try / except

# denominator = int(input("Please eneter a number to divide by: "))
# try:
#     division_result = 100 / number
#     print(division_result)
#
# except ZeroDivisionError:
#     print("You cannot divide by 0, please try gain")


# EXAMPLE 2 -- raise exception

# number = int(input('Enter a number in the range 5-10: '))
#
# try:
#     if number < 5 or number > 10:
#         raise Exception
#
#     division_result = 100 / number
#     print(division_result)
#     print("Well Done")
#
# except:
#     print("Your number is NOT in the requested range")
#
#

# EXAMPLE 3 - user defined errors

class ValueIsBelowHundredError(ValueError):
    """Raised when value is below 100"""
    pass


# EXAMPLE 4 - debugging

def debugging_n_breakpoints():
    my_list = []
    for i in range(10):
        new_i = 10 + i

        import pdb
        pdb.set_trace()

        print('new value is: ', i)
        my_list.append((new_i))
    return my_list

# debugging_n_breakpoints()



#########################################################
###                     PRACTICE                      ###
#########################################################

"""
Start coding this example from scratch with students
"""


def age_validated(age):
    if age < 0:
        raise ValueError("Only positive integers are allowed")

    assert 12 < age <= 19

    return True


def name_validated(name_string):
    if ',' not in name_string:
        raise ValueError("Incorrect input: missing ',' to separate name and surname")

    name, surname = name_string.split(',')

    if not len(name) or not len(surname):
        raise ValueError("Incorrect input: missing name or surname values")

# Flag
isSuccessful = False

try:
    name = input("Please enter your name and surname separated by coma: ")
    name_validated(name)
    age = int(input("Enter your age: "))
    age_validated(age)

except ValueError as exc:
    print("Invalid input: %s" % exc)

except AssertionError as exc:
    print("The age is not within the 'teenager' category")

else:
    with open("registraton_file.txt", 'a+') as file:
        file.write("New member name: {} and age {}. \n".format(name, age))
    isSuccessful = True

finally:
    if isSuccessful:
        print("Registration Process completed SUCCESSFULLY!")
    else:
        print("Could not complete registration. Please try again. ")

#########################

def readFile(file_name):
    try:
        with open(file_name, 'r') as f:  # Open a file as read-only
            print(f.readlines())

    except FileNotFoundError as exc:
        print(exc)

readFile('registraton_file.txt')