# Binance Futures Testnet Trading Bot

A simple Python CLI application that places **Market** and **Limit** orders on the **Binance Futures Testnet**. The project demonstrates clean code structure, input validation, logging, and error handling.

---

## Features

- Place **MARKET** orders
- Place **LIMIT** orders
- Supports **BUY** and **SELL**
- Command-line interface using `argparse`
- Input validation
- Logging of requests, responses, and errors
- Exception handling for invalid input, API errors, and network failures
- Modular project structure

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
├── logs/
│   └── trading.log
│
├── cli.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Requirements

- Python 3.10+
- Binance Futures Testnet account
- Binance Testnet API Key
- Binance Testnet Secret Key

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd trading_bot
```

### 2. Create a virtual environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
API_KEY=YOUR_BINANCE_API_KEY
API_SECRET=YOUR_BINANCE_API_SECRET
```

**Do not commit the `.env` file to GitHub.**

---

## Usage

### Place a MARKET BUY order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Place a MARKET SELL order

```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

### Place a LIMIT BUY order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

### Place a LIMIT SELL order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 200000
```

---

## Sample Output

### MARKET Order

```
SUCCESS
========================================
Order ID       : 27777669143
Symbol         : BTCUSDT
Side           : BUY
Order Type     : MARKET
Status         : FILLED
Original Qty   : 0.0010
Executed Qty   : 0.0010
Cumulative Qty : 0.0010
Average Price  : 62673.800000
========================================
```

### LIMIT Order

```
SUCCESS
========================================
Order ID       : 27777669461
Symbol         : BTCUSDT
Side           : SELL
Order Type     : LIMIT
Status         : NEW
Original Qty   : 0.0010
Executed Qty   : 0.0000
Cumulative Qty : 0.0000
Average Price  : 0.00
========================================
```

---

## Validation

The application validates:

- Symbol
- Order Side (BUY/SELL)
- Order Type (MARKET/LIMIT)
- Quantity
- Price for LIMIT orders

Example validation errors:

```
Price is required for LIMIT orders.
```

```
Side must be BUY or SELL.
```

```
Order type must be MARKET or LIMIT.
```

```
Quantity must be greater than zero.
```

---

## Logging

Logs are stored in:

```
logs/trading.log
```

The log file records:

- Order requests
- API responses
- Validation failures
- Exceptions
- API errors

---

## Assumptions

- Uses the Binance Futures Testnet environment.
- LIMIT orders remain in the `NEW` state until the market reaches the specified price.
- MARKET orders are expected to be filled immediately under normal market conditions.
- API credentials are loaded securely from a local `.env` file.

---

## Technologies Used

- Python 3
- python-binance
- python-dotenv
- argparse
- logging

---

## Author

Akanksha Patil

GitHub: https://github.com/akankshapatil2015