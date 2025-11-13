'''
Stonk Market Cap Calulator

'''
price = float(input(f"Enter the price of the stonk: "))
supply = float(input(f"Enter the supply of the stonk: "))
market_cap = price * supply
print(f"The market cap is", market_cap )

# or

def market_cap(price, supply):
  return price * supply

price = int(input("Enter the price of the stonk: "))
supply = int(input("Enter the supply of the stonk: "))

print(market_cap(price, supply))
