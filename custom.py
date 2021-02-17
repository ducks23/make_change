from math import ceil


def makeChange(change, denominations):
    """Make change with custom coins.

    Supply change you want to be tendered and a space seperated list
    of denominations you wish to be printed.
    """
    temp = ceil(float(change) * 100)
    coins = sorted(map(int, denominations.split()), reverse=True)

    for coin in coins:
        num_coins = temp / coin
        temp = temp % coin
        print(f"Coin {coin} cents: {int(num_coins)}")

if __name__ == "__main__":
    change = input("Enter Change Amount: ")
    denominations = input("Enter Custom Denominations with space seperated numbers: ")
    
    makeChange(change, denominations)
