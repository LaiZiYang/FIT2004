import math

class CoinChangeProblem:
    def __init__(self, coins, amount) -> None:
        self.coins = []
        self.amount = 0



def coinChangeProblem(coins, amount):
    memo = [math.inf] * (amount + 1)
    memo[0] = 0

    for value in range(1, amount + 1):
        minNumberOfCoins = math.inf
        for coin in coins:
            if coin <= value:
                minNumberOfCoins = min(minNumberOfCoins, memo[value - coin] + 1)
        memo[value] = minNumberOfCoins

    return memo[amount] if memo[amount] != math.inf else -1


coins = [1, 2, 5]
amount = 11
print(coinChangeProblem(coins, amount))  # Output: 3

class item:
    def __init__(self, capacity, value) -> None:
        self.capacity = capacity
        self.value = value

def knapsackProblem(items, capacity):
    memo = [0] * (capacity + 1)
    memo[0] = 0

    for capacity in range(1, capacity + 1):
        maxValue = 0
        for item in items:
            if item.capacity <= capacity:
                maxValue = max(maxValue, memo[capacity - item.capacity] + item.value)
        memo[capacity] = maxValue

    return memo[capacity]


items = [item(9, 550), item(5, 350), item(6, 180), item(1, 40)]
capacity = 5
print(knapsackProblem(items, capacity))  # Output: 8