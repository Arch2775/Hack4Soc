class StockMarketGame:
    def __init__(self, initial_stocks, predicted_values_dict):
        self.stocks = initial_stocks
        self.predicted_values_dict = predicted_values_dict
        self.balance = 100000  # Initial balance for the user
        self.current_day = 0

    def display_menu(self):
        print("\nStock Market Game Menu:")
        print("1. Buy Stocks")
        print("2. Sell Stocks")
        print("3. Hold Stocks")
        print("4. Display Portfolio")
        print("5. Display Predicted Values")
        print("6. Next Day")
        print("7. Exit")

    def buy_stocks(self, stock_symbol, quantity):
        if stock_symbol not in self.stocks:
            print("Invalid stock symbol.")
            return

        stock_price = self.stocks[stock_symbol]['price']
        cost = stock_price * quantity

        if self.balance >= cost:
            self.stocks[stock_symbol]['quantity'] += quantity
            self.balance -= cost
            print(f"You bought {quantity} shares of {stock_symbol} at ${stock_price} each on Day 0.")
        else:
            print("Insufficient balance to buy stocks.")

    def sell_stocks(self, stock_symbol, quantity):
        if stock_symbol not in self.stocks:
            print("Invalid stock symbol.")
            return

        if self.stocks[stock_symbol]['quantity'] >= quantity:
            stock_price = self.predicted_values_dict[stock_symbol][self.current_day][0]
            earnings = stock_price * quantity
            self.stocks[stock_symbol]['quantity'] -= quantity
            self.balance += earnings
            print(f"You sold {quantity} shares of {stock_symbol} at ${stock_price} each on Day {self.current_day + 1}.")
        else:
            print("Insufficient quantity of stocks to sell.")

    def hold_stocks(self):
        print("You chose to hold your stocks for the day.")

    def display_portfolio(self):
        print("\nPortfolio:")
        for stock_symbol, stock_info in self.stocks.items():
            if stock_info['quantity'] > 0:
                print(f"{stock_symbol}: {stock_info['quantity']} shares - Total Value: ${stock_info['quantity'] * self.predicted_values_dict[stock_symbol][self.current_day][0]}")

        print(f"Balance: ${self.balance}")

    def display_predicted_values(self):
        print(f"\nPredicted Values for Day {self.current_day + 1}:")
        for stock_symbol, values in self.predicted_values_dict.items():
            print(f"{stock_symbol}: ${values[self.current_day][0]}")

    def run_game(self):
        print("\nDay 0 - Initial Purchase")
        for stock_symbol, stock_info in self.stocks.items():
            if stock_info['quantity'] > 0:
                bought_price = stock_info['price']
                print(f"You initially bought {stock_info['quantity']} shares of {stock_symbol} at ${bought_price} each.")

        while True:
            print(f"\nDay {self.current_day + 1}")
            self.display_menu()

            choice = input("Enter your choice (1-7): ")
            if choice == '1':
                stock_symbol = input("Enter stock symbol to buy: ").upper()
                quantity = int(input("Enter quantity to buy: "))
                self.buy_stocks(stock_symbol, quantity)
            elif choice == '2':
                stock_symbol = input("Enter stock symbol to sell: ").upper()
                quantity = int(input("Enter quantity to sell: "))
                self.sell_stocks(stock_symbol, quantity)
            elif choice == '3':
                self.hold_stocks()
            elif choice == '4':
                self.display_portfolio()
            elif choice == '5':
                self.display_predicted_values()
            elif choice == '6':
                self.current_day += 1
                print(f"Moving to Day {self.current_day + 1}")
            elif choice == '7':
                print("Exiting the game.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

            # Calculate daily total profits/losses based on the difference between bought price and predicted value
            if self.current_day < len(list(self.predicted_values_dict.values())[0]):
                for stock_symbol, stock_info in self.stocks.items():
                    if stock_info['quantity'] > 0:
                        bought_price = stock_info['price']
                        predicted_price = self.predicted_values_dict[stock_symbol][self.current_day][0]
                        profit_loss = stock_info['quantity'] * (predicted_price - bought_price)
                        print(f"Total Profit/Loss for {stock_symbol} on Day {self.current_day + 1}: ${profit_loss}")

if __name__ == "__main__":
    initial_stocks = {
        'AAPL': {'price': 192.5299988, 'quantity': 0},
        'AMZN': {'price': 151.9400024, 'quantity': 0},
        'JPM': {'price': 170.1000061, 'quantity': 0},
        'PEP': {'price': 169.8399963, 'quantity': 0},
        'GOOGL': {'price': 131.97787, 'quantity': 0},
    }

    predicted_values_dict = {
        'AAPL': [[187.61243], [184.9588], [182.58821], [180.45682], [178.5297], [176.77849], [175.18002]],
        'JPM': [[165.1458], [162.95236], [160.90916], [158.99799], [157.20361], [155.51308], [153.91539]],
        'AMZN': [[152.6304], [151.55273], [150.54767], [149.608], [148.72746], [147.90054], [147.12251]],
        'PEP': [[153.7913], [144.70518], [137.5918], [131.824], [127.02233], [122.94192], [119.416916]],
        'GOOGL': [[131.97787], [127.49505], [123.81113], [120.72599], [118.10277], [115.844345], [113.87967]],
    }
    game = StockMarketGame(initial_stocks, predicted_values_dict)
    game.run_game()