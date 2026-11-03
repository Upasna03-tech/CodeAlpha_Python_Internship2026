# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400
}

total_investment = 0
stock_records = []

print("Welcome to Stock Portfolio Tracker!")

while True:

    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:

        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity

        total_investment += investment

        stock_records.append(
            f"{stock_name} | Quantity: {quantity} | Investment: {investment}"
        )

        print("Stock:", stock_name)
        print("Investment:", investment)

    else:
        print("Stock not found!")

print("\nTotal Investment:", total_investment)

# Save data in text file

with open("stock_report.txt", "w") as file:

    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("----------------------\n")

    for record in stock_records:
        file.write(record + "\n")

    file.write("\nTotal Investment: " + str(total_investment))

print("\nReport saved successfully!")
print("Thank you!")