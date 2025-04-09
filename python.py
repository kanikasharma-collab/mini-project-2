# Currency Converter

# A dictionary with exchange rates to USD (1 USD = exchange_rate of another currency)
exchange_rates = {
    'USD': 1.0,  # Base currency (1 USD)
    'EUR': 0.85,  # 1 USD = 0.85 EUR
    'GBP': 0.75,  # 1 USD = 0.75 GBP
    'INR': 74.85,  # 1 USD = 74.85 INR
    'AUD': 1.34,  # 1 USD = 1.34 AUD
    'CAD': 1.26,  # 1 USD = 1.26 CAD
    'JPY': 110.56,  # 1 USD = 110.56 JPY
}

# Function to display available currencies
def display_currencies():
    print("\nAvailable currencies to convert:")
    for currency in exchange_rates.keys():
        print(currency)

# Function to convert currency
def convert_currency(amount, from_currency, to_currency):
    # Check if the currencies are in the exchange rates dictionary
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        print(f"Sorry, we don't support conversion between {from_currency} and {to_currency}.")
        return None

    # Convert the amount to USD first, then convert it to the target currency
    amount_in_usd = amount / exchange_rates[from_currency]
    converted_amount = amount_in_usd * exchange_rates[to_currency]
    
    return converted_amount

# Main function to run the program
def main():
    print("Welcome to the Currency Converter!")

    # Loop to continuously run the program until the user decides to exit
    while True:
        display_currencies()
        
        from_currency = input("\nEnter the currency you want to convert from (or type 'exit' to quit): ").upper()
        if from_currency == 'EXIT':
            print("Goodbye!")
            break

        if from_currency not in exchange_rates:
            print("Currency not supported. Please try again.")
            continue
        
        to_currency = input("Enter the currency you want to convert to: ").upper()
        if to_currency == 'EXIT':
            print("Goodbye!")
            break

        if to_currency not in exchange_rates:
            print("Currency not supported. Please try again.")
            continue
        
        amount = float(input(f"Enter the amount in {from_currency}: "))
        
        converted_amount = convert_currency(amount, from_currency, to_currency)
        
        if converted_amount is not None:
            print(f"\n{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")

# Run the application
if __name__ == "__main__":
    main()