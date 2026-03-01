import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://www.google.com")
HEADLESS = os.getenv("HEADLESS", "TRUE").upper() == "TRUE"
LOGIN_USERNAME = os.getenv("LOGIN_USERNAME")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")
WAIT_TIMEOUT = int(os.getenv("WAIT_TIMEOUT", "10"))
DEFAULT_ORDER_TYPE = os.getenv("DEFAULT_ORDER_TYPE", "Market")
