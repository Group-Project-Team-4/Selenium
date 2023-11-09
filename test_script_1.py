"""
   - Login and create new post automated test
   - Please make a new branch to make any changes! Do not change this directly
   - Then when you are sure there are no bugs and your code is to Pylint standard, 
         you should make a pull request.
   - We should be utilizing all the tools GitHub has to offer us.
"""
import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# Make sure to download ChromeDriver and add to PATH or if using Firefox see selenium documentation
# ChromeDriver: https://googlechromelabs.github.io/chrome-for-testing/#stable


def generate_random_card_number():
    """Fake Credit Card Generator"""
    credit_card = ""
    for idx in range(16):
        credit_card += random.choice(string.digits)
    return credit_card

USERNAME = f"user{random.randint(1, 100)}"
# USERNAME = "nate123"
PASSWORD = "12345"
EMAIL = USERNAME + "@gmail.com"
FULLNAME = "Ron Swanson"
ADDRESS = f"{random.randint(1000, 10000)} main st, Raleigh, NC"
CARD_NUMBER = generate_random_card_number()
EXPIRATION = "08/25"
CARD_PIN = random.randint(1000, 10000)


def main() -> None:
    start_time = time.time()
    """Web Driver Function"""
    driver = webdriver.Chrome()
# Enter webapp url
    driver.get('http://localhost:5000/')

    try:
        # Enter site
        shop = driver.find_element(By.LINK_TEXT, "Shop Now")
        shop.click()
        driver.save_screenshot("./screenshots_test1/enter_site.png")
        time.sleep(0.25)
    # Register
        register = driver.find_element(By.LINK_TEXT, "Register")
        register.click()
        driver.save_screenshot("./screenshots_test1/register_page.png")
        time.sleep(0.25)

        username_input = driver.find_element(
            By.ID, "register_username_textinput")
        username_input.send_keys(USERNAME)
        time.sleep(0.25)

        password_input = driver.find_element(
            By.ID, "register_password_textinput")
        password_input.send_keys(PASSWORD)
        time.sleep(0.25)

        driver.save_screenshot("./screenshots_test1/register.png")
        password_input.send_keys(Keys.ENTER)
        driver.save_screenshot("./screenshots_test1/register_success.png")
        time.sleep(0.25)

    # Login
        login_link = driver.find_element(By.ID, "base_login_anchor")
        login_link.click()
        time.sleep(0.25)

        username_input = driver.find_element(By.ID, "login_username_textinput")
        username_input.send_keys(USERNAME)
        time.sleep(0.25)

        password_input = driver.find_element(By.ID, "login_password_textinput")
        password_input.send_keys(PASSWORD)
        time.sleep(0.25)

        driver.save_screenshot("./screenshots_test1/login.png")
        login_button = driver.find_element(By.ID, "login_submit_button")
        login_button.click()
        driver.save_screenshot("./screenshots_test1/login_success.png")
        time.sleep(0.25)

    # Shop for an item
        enter_shop = driver.find_element(By.LINK_TEXT, "Shop Now")
        enter_shop.click()
        driver.save_screenshot("./screenshots_test1/enter_shop.png")
        time.sleep(0.25)

        url = "/shop/7"
        watch_item = driver.find_element(By.XPATH, '//a[@href="'+url+'"]')
        watch_item.click()
        driver.save_screenshot("./screenshots_test1/watch.png")
        time.sleep(0.25)

        add_to_cart = driver.find_element(By.ID, "add-to-cart-button")
        add_to_cart.click()
        driver.save_screenshot("./screenshots_test1/watch_in_cart.png")
        time.sleep(0.25)

    # Checkout
        checkout = driver.find_element(By.LINK_TEXT, "Checkout")
        checkout.click()
        driver.save_screenshot("./screenshots_test1/checkout.png")
        time.sleep(0.25)

        email = driver.find_element(By.ID, "email")
        email.send_keys(EMAIL)
        time.sleep(0.25)

        fullname = driver.find_element(By.ID, "name")
        fullname.send_keys(FULLNAME)
        time.sleep(0.25)

        address = driver.find_element(By.ID, "address")
        address.send_keys(ADDRESS)
        time.sleep(0.25)

        card_number = driver.find_element(By.ID, "credit-card")
        card_number.send_keys(CARD_NUMBER)
        time.sleep(0.25)

        expiration = driver.find_element(By.ID, "expiration-date")
        expiration.send_keys(EXPIRATION)
        time.sleep(0.25)

        card_pin = driver.find_element(By.ID, "cvc")
        card_pin.send_keys(CARD_PIN)

        driver.save_screenshot("./screenshots_test1/checkout_form_filled.png")
        purchase = driver.find_element(By.CLASS_NAME, "checkout-button")
        purchase.click()
        driver.save_screenshot("./screenshots_test1/items_purchased.png")
        time.sleep(0.25)

    # Alert that all tests have completed succesfully
        driver.save_screenshot("./screenshots_test1/end_test.png")
        driver.execute_script('alert("All tests are complete, thank you!")')
        time.sleep(3)

        # Switchs focus to the new alert
        alert = driver.switch_to.alert

        # Presses "OK" to accept alert
        alert.accept()
        time.sleep(0.25)

    # Logout
        logout = driver.find_element(By.ID, "base_logout_anchor")
        logout.click()
        time.sleep(0.25)

        end_time = time.time()

        execution_time = end_time - start_time
        print(execution_time)

    except NoSuchElementException as err:
        print(err)

    driver.quit()


if __name__ == "__main__":
    main()
