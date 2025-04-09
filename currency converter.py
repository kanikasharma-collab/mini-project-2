import tkinter as tk
from tkinter import ttk, messagebox

# Exchange rates relative to USD
exchange_rates = {
    'USD': 1.0,
    'EUR': 0.85,
    'GBP': 0.75,
    'INR': 74.85,
    'AUD': 1.34,
    'CAD': 1.26,
    'JPY': 110.56,
}

# Currency symbols
currency_symbols = {
    'USD': '$',
    'EUR': '€',
    'GBP': '£',
    'INR': '₹',
    'AUD': 'A$',
    'CAD': 'C$',
    'JPY': '¥',
}

# Generate currency display options: "USD ($)", etc.
currency_options = [f"{code} ({currency_symbols[code]})" for code in exchange_rates.keys()]

# Helper to extract currency code from formatted selection
def extract_code(selection):
    return selection.split(' ')[0]  # "USD ($)" → "USD"

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("420x350")
        self.root.resizable(False, False)

        # Canvas for gradient background
        self.canvas = tk.Canvas(self.root, width=420, height=350)
        self.canvas.pack(fill="both", expand=True)
        self.draw_gradient()

        # Heading
        self.canvas.create_text(210, 50, text="Currency Converter", font=("Helvetica", 18, "bold"), fill="white")

        # Input fields and labels
        self.amount_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.from_currency = ttk.Combobox(self.root, values=currency_options, state="readonly", font=("Helvetica", 11))
        self.to_currency = ttk.Combobox(self.root, values=currency_options, state="readonly", font=("Helvetica", 11))
        self.result_label = tk.Label(self.root, font=("Helvetica", 12, "bold"), bg="#005588", fg="white")

        # Default values
        self.from_currency.set("USD ($)")
        self.to_currency.set("INR (₹)")

        # Place widgets
        self.place_widgets()

    def draw_gradient(self):
        for i in range(0, 350):
            r = 0
            g = int(85 + (i / 350) * (130 - 85))
            b = int(136 + (i / 350) * (255 - 136))
            color = f'#{r:02x}{g:02x}{b:02x}'
            self.canvas.create_line(0, i, 420, i, fill=color)

    def place_widgets(self):
        self.canvas.create_text(100, 100, text="Amount:", font=("Helvetica", 12, "bold"), fill="white")
        self.canvas.create_window(270, 100, window=self.amount_entry, width=160)

        self.canvas.create_text(100, 140, text="From Currency:", font=("Helvetica", 12, "bold"), fill="white")
        self.canvas.create_window(270, 140, window=self.from_currency, width=160)

        self.canvas.create_text(100, 180, text="To Currency:", font=("Helvetica", 12, "bold"), fill="white")
        self.canvas.create_window(270, 180, window=self.to_currency, width=160)

        convert_button = tk.Button(self.root, text="Convert", command=self.convert_currency, font=("Helvetica", 11))
        self.canvas.create_window(210, 230, window=convert_button)

        self.canvas.create_window(210, 280, window=self.result_label)

    def convert_currency(self):
        try:
            amount_str = self.amount_entry.get().strip()
            if not amount_str:
                messagebox.showwarning("Input Error", "Amount field is empty.")
                return

            amount = float(amount_str)
            if amount < 0:
                raise ValueError

            from_curr = extract_code(self.from_currency.get())
            to_curr = extract_code(self.to_currency.get())

            if from_curr not in exchange_rates or to_curr not in exchange_rates:
                messagebox.showerror("Error", "Currency not supported.")
                return

            amount_in_usd = amount / exchange_rates[from_curr]
            converted = amount_in_usd * exchange_rates[to_curr]

            from_symbol = currency_symbols.get(from_curr, '')
            to_symbol = currency_symbols.get(to_curr, '')

            self.result_label.config(
                text=f"{from_symbol}{amount:.2f} {from_curr} = {to_symbol}{converted:.2f} {to_curr}"
            )

        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid positive number.")

# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()