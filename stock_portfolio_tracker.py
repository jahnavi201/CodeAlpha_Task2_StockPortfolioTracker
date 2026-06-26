# Stock Portfolio Tracker

# Dictionary of stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "AMZN": 200,
    "MSFT": 300
}

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available Stocks:")

for stock, price in stock_prices.items():
    print(f"{stock} : ₹{price}")

total = 0

while True:
    stock_name = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity

        total += investment

        print(f"{stock_name} Investment = ₹{investment}")

    else:
        print("Stock not found!")

print("\n==============================")
print("Total Investment Value = ₹", total)
print("==============================")