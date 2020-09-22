"""
This program asks the user for the initial balance or principal (e.g. $1234.56),
the interest rate (as a percentage but without the % sign), number of years, and
how frequently compounded (supports the words "daily" for 365, "weekly" for 52,
"monthly" for 12, "quarterly" for 4, and "annually" for 1.

If then displays the total accrued amount (i.e. the principal plus the interest).

The output should look exactly like money.

Make sure you create each of the functions appropriately. All input() and
print() calls are in main() [do NOT use input() or print() in any other function].

HINT 1: For get_number_of_compounds() look back at homework #4.

HINT 2: For compound_interest() look back at lab #3.


EXAMPLE 1:
Principal: $10000.00
Interest Rate: 3.875
Number of Years: 7.5
Frequency of Compounds (daily, weekly, monthly, quarterly, or annually): monthly
You will have accrued $13366.37


EXAMPLE 2:
Principal: $5000.00
Interest Rate: 2.5
Number of Years: 7
Frequency of Compounds (daily, weekly, monthly, quarterly, or annually): daily
You will have accrued $5956.20


AUTHOR:
"""


def get_number_of_compounds(frequency):
    """
    This function takes one of the strings "daily", "weekly", "monthly",
    "quarterly", or "annually" as a parameter and returns the number of times per year it
    represents (365, 52, 12, 4, and 1 respectively). This can be easily done
    with one of the collection types we discussed that allows you to associate
    things.
    """
    # TODO: *remove* this line and the dummy return line then write the correct code
    return -1


def compound_interest(principal, rate, years, num_compounds):
    """
    Computes the compound interest on an account that starts with `principal`
    amount of money, the given interest `rate` (as a percentage, i.e. not
    divided by 100), over the number of `years`, and compounding the given
    *number* of times. Return the computed accrued amount.
    """
    # TODO: *remove* this line and the dummy return line then write the correct code
    return -1


def main():
    # TODO: *remove* this line and the pass line then write the correct code
    # Get all the variables

    principal = int(input('Principal: '))
    rate = int(input('Interest Rate: '))
    