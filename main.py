import tkinter as tk
from tkinter import ttk
import requests
from datetime import datetime


class CryptoPriceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crypto Price Tracker")

        self.price_label_btc = ttk.Label(root, text="Bitcoin (BTC) Fiyatı:")
        self.price_label_btc.grid(row=0, column=0, padx=10, pady=10)

        self.price_value_btc = tk.StringVar()
        self.price_entry_btc = ttk.Entry(root, textvariable=self.price_value_btc, state="readonly")
        self.price_entry_btc.grid(row=0, column=1, padx=10, pady=10)

        self.last_updated_label_btc = ttk.Label(root, text="Son Güncelleme:")
        self.last_updated_label_btc.grid(row=0, column=2, padx=10, pady=10)

        self.price_label_eth = ttk.Label(root, text="Ethereum (ETH) Fiyatı:")
        self.price_label_eth.grid(row=1, column=0, padx=10, pady=10)

        self.price_value_eth = tk.StringVar()
        self.price_entry_eth = ttk.Entry(root, textvariable=self.price_value_eth, state="readonly")
        self.price_entry_eth.grid(row=1, column=1, padx=10, pady=10)

        self.last_updated_label_eth = ttk.Label(root, text="Son Güncelleme:")
        self.last_updated_label_eth.grid(row=1, column=2, padx=10, pady=10)

        self.update_button = ttk.Button(root, text="Güncelle", command=self.update_prices)
        self.update_button.grid(row=2, column=0, columnspan=3, pady=10)

        # İlk güncelleme yap
        self.update_prices()

    def update_prices(self):
        crypto_symbols = {"bitcoin": "BTC", "ethereum": "ETH"}

        for symbol, display_name in crypto_symbols.items():
            api_url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
            try:
                response = requests.get(api_url)
                data = response.json()

                # Kontrol et
                if symbol not in data:
                    raise ValueError(f"{symbol} sembolü bulunamadı.")

                price = data[symbol]["usd"]

                if symbol == "bitcoin":
                    self.price_value_btc.set(f"${price}")
                    self.last_updated_label_btc.config(
                        text=f"Son Güncelleme: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                elif symbol == "ethereum":
                    self.price_value_eth.set(f"${price}")
                    self.last_updated_label_eth.config(
                        text=f"Son Güncelleme: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            except (requests.RequestException, ValueError) as e:
                print(f"Hata oluştu: {e}")
                self.price_value_btc.set("Hata")
                self.price_value_eth.set("Hata")


if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoPriceApp(root)
    root.mainloop()
