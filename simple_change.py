from math import ceil


def makeChange(change):
    """Print correct change.

    Take dollar amount as input
    Returns change in coins
    """
    temp = ceil(change * 100)

    quarters = temp / 25
    left_over = temp % 25

    dimes = left_over / 10
    left_over = left_over % 10

    nickels = left_over / 5
    left_over = left_over % 5

    print(f"quarters: {int(quarters)} \ndimes: {int(dimes)} \nnickels: {int(nickels)} \npennies: {int(left_over)}")

def makeChangeLoop(change):
    """Make change with loop."""
    temp = ceil(float(change) * 100)
    coins = [25, 10, 5, 1]

    for coin in coins:
        num_coins = temp / coin
        temp = temp % coin
        print(f"coin {coin} cents: {int(num_coins)}")


if __name__ == "__main__":
    val = input("Enter change amount: ")
    #makeChange(float(val))
    makeChangeLoop(val)
