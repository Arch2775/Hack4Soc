import streamlit as st
from StockMarketGame import StockMarketGame

# Define initial stocks and predicted values
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

# Create instance of StockMarketGame
game = StockMarketGame(initial_stocks, predicted_values_dict)

# Streamlit UI
st.title('Stock Market Game')

def display_menu():
    st.write("\nStock Market Game Menu:")
    st.write("1. Buy Stocks")
    st.write("2. Sell Stocks")
    st.write("3. Hold Stocks")
    st.write("4. Display Portfolio")
    st.write("5. Display Predicted Values")
    st.write("6. Next Day")
    st.write("7. Exit")

def display_portfolio():
    st.write("\nPortfolio:")
    for stock_symbol, stock_info in game.stocks.items():
        if stock_info['quantity'] > 0:
            st.write(f"{stock_symbol}: {stock_info['quantity']} shares - Total Value: ${stock_info['quantity'] * game.predicted_values_dict[stock_symbol][game.current_day][0]}")
    st.write(f"Balance: ${game.balance}")

def display_predicted_values():
    st.write(f"\nPredicted Values for Day {game.current_day + 1}:")
    for stock_symbol, values in game.predicted_values_dict.items():
        st.write(f"{stock_symbol}: ${values[game.current_day][0]}")

# Main loop
while True:
    st.write(f"\nDay {game.current_day + 1}")
    display_menu()

    choice = st.text_input("Enter your choice (1-7): ")
    if choice == '1':
        stock_symbol = st.text_input("Enter stock symbol to buy: ").upper()
        quantity = int(st.text_input("Enter quantity to buy: "))
        game.buy_stocks(stock_symbol, quantity)
    elif choice == '2':
        stock_symbol = st.text_input("Enter stock symbol to sell: ").upper()
        quantity = int(st.text_input("Enter quantity to sell: "))
        game.sell_stocks(stock_symbol, quantity)
    elif choice == '3':
        game.hold_stocks()
    elif choice == '4':
        display_portfolio()
    elif choice == '5':
        display_predicted_values()
    elif choice == '6':
        game.current_day += 1
        st.write(f"Moving to Day {game.current_day + 1}")
    elif choice == '7':
        st.write("Exiting the game.")
        break
    else:
        st.write("Invalid choice. Please enter a number between 1 and 7.")

    # Calculate daily total profits/losses based on the difference between bought price and predicted value
    if game.current_day < len(list(game.predicted_values_dict.values())[0]):
        for stock_symbol, stock_info in game.stocks.items():
            if stock_info['quantity'] > 0:
                bought_price = stock_info['price']
                predicted_price = game.predicted_values_dict[stock_symbol][game.current_day][0]
                profit_loss = stock_info['quantity'] * (predicted_price - bought_price)
                st.write(f"Total Profit/Loss for {stock_symbol} on Day {game.current_day + 1}: ${profit_loss}")



