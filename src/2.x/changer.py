import sys

COINS = [200, 100, 50, 20, 10, 5, 2, 1]  # UK coin denominations. Can be adapted to specify coin values as input params.

# ----------------------------------------------------------------------------------------------------------------------


def main():
    """Coin changer puzzle for junior interview candidates, in Python 2.

    Generates the optimal set of change for a given sum of money, using the
    obvious "greedy algorithm". This only works, in terms of producing
    optimal results, for "canonical" coin systems where each coin is at least
    double in value of the next-lowest coin, such as the UK coin system.
    """

    if len(sys.argv) == 1:
        print "Please specify an amount to generate change for."
        sys.exit()

    amount = sys.argv[1]
    if not amount.isdigit():
        print "Please specify a valid number to generate change for."
        sys.exit()

    amount = int(amount) # The initial amount we want to generate change for.

    change = {} # Build up our change collection here

    for coin in COINS:
        if coin <= amount:
            count = amount // coin
            change[coin] = count
            amount = amount % coin

    assert(amount == 0), "Error - outstanding balance remaining!"

    print "Change required:"
    for coin in COINS:
        if change.has_key(coin):
            print coin, ":", change[coin]

# ----------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    main()