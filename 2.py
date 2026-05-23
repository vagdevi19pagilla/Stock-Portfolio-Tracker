# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130,
    "MSFT": 320
}

total_investment = 0

print("📈 Stock Portfolio Tracker")

while True:
    stock = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input(f"Enter quantity for {stock}: "))

        investment = stock_prices[stock] * quantity
        total_investment += investment

        print(f"✅ Added {quantity} shares of {stock}")
        print(f"💰 Investment for {stock}: ${investment}")
    else:
        print("❌ Stock not available.")

print("\n📊 Total Investment Value: $", total_investment)

# Save result to file
save = input("Do you want to save the result? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write(f"Total Investment Value: ${total_investment}")

    print("✅ Result saved in portfolio.txt")