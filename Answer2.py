n = int(input("Enter the value in cents you want change for:"))
denomination_number = int(input("Enter the number of denominations you want: "))

print("Enter the denominations as in c^0 , c^1, c^2 and so on: ")
coin_denominations = [int(input()) for c in range(denomination_number)] 
# order will be sorted in decreasing order
coin_denominations = sorted(coin_denominations, reverse=True)      
number_of_coins = []

for c in range(len(coin_denominations)):
    number_of_coins.append(int(n / coin_denominations[c]))
    n = n % coin_denominations[c]

print("Denominations in Descending order                         : ",coin_denominations)
print("Number of times each denomination is occuring respectively: ",number_of_coins)