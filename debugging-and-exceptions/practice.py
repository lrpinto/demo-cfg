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