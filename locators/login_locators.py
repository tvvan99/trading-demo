from selenium.webdriver.common.by import By


class LoginLocators:
    USERNAME_INPUT = (By.CSS_SELECTOR, '[data-testid="login-user-id"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[data-testid="login-password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-testid="login-submit"]')
