# Crypto Worth

A Python script to calculate and track the total net worth of your cryptocurrency investment portfolio in real-time.

## 📋 Features

- **Real-time Portfolio Tracking**: Fetches current cryptocurrency prices from CoinMarketCap
- **Multi-Currency Support**: Track holdings across multiple cryptocurrencies
- **Net Worth Calculation**: Automatically calculates total portfolio value in USD
- **Simple Configuration**: Easy-to-edit Python dictionary for managing your holdings
- **Individual Asset Breakdown**: View the worth of each cryptocurrency separately

## 🔧 Prerequisites

- Python 2.7 or Python 3.x
- pip (Python package installer)
- Internet connection (to fetch real-time prices)

## 📥 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/isinghmitesh/crypto_worth.git
   ```

2. **Navigate to the project directory**

   ```bash
   cd crypto_worth
   ```

3. **Install required dependencies**

   ```bash
   pip install -r requriments.py
   ```

   Or install packages individually:
   ```bash
   pip install requests bs4 lxml
   ```

## ⚙️ Configuration

Edit the `feeder.py` file to add your cryptocurrency holdings. The file contains a list of dictionaries, where each dictionary represents one cryptocurrency holding.

**Structure of each entry:**

```python
{
    "s_no": 1,              # Serial number (for tracking purposes)
    "currency": "bitcoin",  # Currency name (must match CoinMarketCap URL slug)
    "holding": 0.5          # Quantity of the cryptocurrency you own
}
```

**Example configuration:**

```python
fetch = [
    {
        "s_no": 1,
        "currency": "bitcoin",
        "holding": 0.010555
    },
    {
        "s_no": 2,
        "currency": "ethereum",
        "holding": 2.25488594
    },
    {
        "s_no": 3,
        "currency": "ripple",
        "holding": 2266.55
    }
]
```

### Finding the correct currency name

The `currency` field must match the URL slug used by CoinMarketCap. For example:
- Bitcoin: `bitcoin` (from https://coinmarketcap.com/currencies/bitcoin/)
- Ethereum: `ethereum` (from https://coinmarketcap.com/currencies/ethereum/)
- Ripple (XRP): `ripple` (from https://coinmarketcap.com/currencies/ripple/)

## 🚀 Usage

Run the script to calculate your portfolio's net worth:

```bash
python fetch.py
```

### Example Output

```
1   tron   :  1234.56
2   cardano   :  5678.90
3   bitcoin   :  10000.00
4   ethereum   :  3456.78


Net Worth  :  20370.24
```

The script will:
1. Fetch current prices for each cryptocurrency from CoinMarketCap
2. Calculate the worth of each holding (quantity × current price)
3. Display individual cryptocurrency values
4. Show the total net worth of your portfolio in USD

## 📝 Notes

- **Holding**: The "holding" value represents the **quantity** of the cryptocurrency you own (not the purchase price)
- **Currency Names**: Ensure the currency name matches exactly with CoinMarketCap's URL slug (usually lowercase with hyphens)
- **Update Frequency**: Run the script anytime to get updated portfolio values based on current market prices
- **Privacy**: Your holdings are stored locally in `feeder.py` and are never transmitted anywhere except for price lookups

## 🔍 Troubleshooting

**Issue: Script fails to fetch price**
- Verify the currency name matches CoinMarketCap's URL slug
- Check your internet connection
- Ensure CoinMarketCap website is accessible

**Issue: Import errors**
- Make sure all dependencies are installed: `pip install requests bs4 lxml`

**Issue: Incorrect calculations**
- Double-check your holding quantities in `feeder.py`
- Ensure numeric values don't have formatting issues (no commas, use dots for decimals)

## 📄 License

This project is open source and available for personal use.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.
