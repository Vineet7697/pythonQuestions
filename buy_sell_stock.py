prices = [7, 1, 5, 3, 6, 4]

min_price = float('inf')   #infinite
max_profit = 0

for i in prices:
    if i < min_price:
        min_price = i  # Buy at lowest price so far
    elif i - min_price > max_profit:
        max_profit = i - min_price  # Sell at highest profit
 
print("Maximum Profit:", max_profit)