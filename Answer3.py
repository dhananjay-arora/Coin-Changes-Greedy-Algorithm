# Assumption: One coin_denominations should be penny.
# O(nk)-time algorithm that makes change for any set of k different coin denominations
n = int(input("Enter the value in cents you want change for:"))
denomination_number = int(input("Enter how many coin_denominations you want to enter: "))

print("Enter the coin_denominations: ")
coin_denominations = [int(input()) for c in range(denomination_number)] 
# order will be sorted in decreasing order
coin_denominations = sorted(coin_denominations, reverse=True)      
number_of_coins = []                                            
# Loop will run k times
for c in range(denomination_number):                               
    number_of_coins.append(0)
    while(n >= coin_denominations[c]):
        n -= coin_denominations[c]
        number_of_coins[c]+=1
print("Denomination value in Descending order                    : ",coin_denominations)
print("Number of times each denomination is occuring respectively: ",number_of_coins)