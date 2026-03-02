# Trading Demo Automation

The code is organized into logical packages:

- `trading_demo.env` – driver/environment helpers
- `trading_demo.page` – page object models
- `trading_demo.action` – high-level user actions built on page objects
- `tests/` – pytest test cases that orchestrate the flows

## Getting Started

1. **Create a virtual environment** (recommended):
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

3. **Run tests**:
   ```powershell
   pytest
   ```

# Requirement met
• Able to place Market with Stop Loss and Take Profit
• Able to edit, partial close and close Open position
• Able to place Limit / Stop order with different types of Expiry
• Able to edit Pending Orders for all values included
