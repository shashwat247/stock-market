def stock_portfolio_tracker():
    # Hardcoded stock prices (in USD)
    stock_prices = {
        "AAPL": 180.50,   # Apple
        "MSFT": 330.75,   # Microsoft
        "GOOGL": 140.25,  # Alphabet (Google)
        "AMZN": 145.18,   # Amazon
        "TSLA": 250.30,   # Tesla
        "NVDA": 430.82,   # NVIDIA
        "META": 310.64,   # Meta (Facebook)
        "JPM": 145.90,    # JPMorgan Chase
        "V": 240.77,      # Visa
        "WMT": 60.45      # Walmart
    }
    
    portfolio = {}
    total_value = 0
    
    print("Stock Portfolio Tracker")
    print("======================")
    print("Available stocks and their current prices:")
    
    # Display available stocks
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price:.2f}")
    
    print("\nEnter your stock holdings (type 'done' when finished):")
    
    # Get user input for stock holdings
    while True:
        stock = input("\nEnter stock symbol: ").upper().strip()
        
        if stock == 'DONE':
            break
            
        if stock not in stock_prices:
            print(f"'{stock}' is not in our database. Available stocks: {', '.join(stock_prices.keys())}")
            continue
            
        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
            if quantity <= 0:
                print("Quantity must be a positive number.")
                continue
        except ValueError:
            print("Please enter a valid number for quantity.")
            continue
            
        portfolio[stock] = {
            'quantity': quantity,
            'price': stock_prices[stock],
            'value': quantity * stock_prices[stock]
        }
        
        total_value += portfolio[stock]['value']
        print(f"Added {quantity} shares of {stock} at ${stock_prices[stock]:.2f} each")
    
    # Display portfolio summary
    print("\n" + "="*50)
    print("PORTFOLIO SUMMARY")
    print("="*50)
    
    for stock, details in portfolio.items():
        print(f"{stock}: {details['quantity']} shares × ${details['price']:.2f} = ${details['value']:.2f}")
    
    print("-"*50)
    print(f"TOTAL PORTFOLIO VALUE: ${total_value:.2f}")
    
    # Option to save to file
    save_option = input("\nWould you like to save this portfolio to a file? (y/n): ").lower()
    if save_option in ['y', 'yes']:
        filename = input("Enter filename (without extension): ").strip()
        if not filename:
            filename = "portfolio"
        
        # Save as TXT file
        with open(f"{filename}.txt", "w") as file:
            file.write("STOCK PORTFOLIO TRACKER\n")
            file.write("="*50 + "\n")
            for stock, details in portfolio.items():
                file.write(f"{stock}: {details['quantity']} shares × ${details['price']:.2f} = ${details['value']:.2f}\n")
            file.write("-"*50 + "\n")
            file.write(f"TOTAL PORTFOLIO VALUE: ${total_value:.2f}\n")
        
        # Save as CSV file
        with open(f"{filename}.csv", "w") as file:
            file.write("Stock,Quantity,Price,Value\n")
            for stock, details in portfolio.items():
                file.write(f"{stock},{details['quantity']},{details['price']:.2f},{details['value']:.2f}\n")
            file.write(f"TOTAL,,,{total_value:.2f}\n")
        
        print(f"Portfolio saved to {filename}.txt and {filename}.csv")

# Run the portfolio tracker
if __name__ == "__main__":
    stock_portfolio_tracker()