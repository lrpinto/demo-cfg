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
    print(new_prices)
    return new_prices

add_vat(10, 1000)