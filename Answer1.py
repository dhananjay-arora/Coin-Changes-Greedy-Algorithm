n = int(input("Enter the value in cents you want change for: "))
coin_denominations = [25,10,5,1]
number_of_coins = []
for c in range(len(coin_denominations)):
    number_of_coins.append(int(n/coin_denominations[c]))
    n = n%coin_denominations[c]
print("coin denominations in quarters, dimes, nickels, and pennies respectively is as follows")
print(number_of_coins)