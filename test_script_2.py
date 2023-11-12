
"""
This script automates a series of web interactions on a specified web application using Selenium WebDriver with Chrome.
It performs the following tasks:
1. Opens the web application and takes screenshots at various stages.
2. Registers a new user with a randomly generated username.
3. Logs in with the newly created user credentials.
4. Navigates through the web application, simulating a shopping process by adding items to the cart and then removing them.
5. Attempts a checkout operation, handling alert pop-ups for test verification.
6. Logs out after completing the tests.
7. Measures and prints the total execution time of the script.

Note: ChromeDriver needs to be installed and added to the system PATH.
ChromeDriver: https://googlechromelabs.github.io/chrome-for-testing/#stable
"""

import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


USERNAME = f"user{random.randint(1, 100)}"
PASSWORD = "12345"


def main() -> None:
# Record start time of test
    start_time = time.time()

# Instantiate a Chrome WebDriver instance    
    driver = webdriver.Chrome()

# Enter the webapp's url (localhost doesn't work so used full url instead)
    driver.get('http://127.0.0.1:5000')
    driver.save_screenshot("./screenshots_test2/landing-page.png")
    time.sleep(0.5)

    try:
    # Enter site
        shop = driver.find_element(By.LINK_TEXT, "Shop Now")
        shop.click()
        time.sleep(0.25)
        driver.save_screenshot("./screenshots_test2/enter_site.png")
        
    
    # Register
        register = driver.find_element(By.LINK_TEXT, "Register")
        register.click()
        time.sleep(0.25)
        driver.save_screenshot("./screenshots_test2/register_page.png")
        

        username_input = driver.find_element(By.ID, "register_username_textinput")
        username_input.send_keys(USERNAME)
        time.sleep(0.25)

        password_input = driver.find_element(By.ID, "register_password_textinput")
        password_input.send_keys(PASSWORD)
        time.sleep(0.25)

        driver.save_screenshot("./screenshots_test2/register.png")
        password_input.send_keys(Keys.ENTER)
        time.sleep(0.25)
        driver.save_screenshot("./screenshots_test2/register_success.png")
        

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

        driver.save_screenshot("./screenshots_test2/login.png")
        login_button = driver.find_element(By.ID, "login_submit_button")
        login_button.click()
        time.sleep(0.25)
        driver.save_screenshot("./screenshots_test2/login_success.png")
        

    # Shop for multiple items
        enter_shop = driver.find_element(By.LINK_TEXT, "Shop Now")
        enter_shop.click()
        time.sleep(0.25)
        driver.save_screenshot("./screenshots_test2/enter_shop.png")
        
        # Select item to add to cart
        url = "/shop/8"
        necklace_item = driver.find_element(By.XPATH, '//a[@href="'+url+'"]')
        necklace_item.click()
        time.sleep(0.25)
        driver.save_screenshot("./screenshots_test2/necklace.png")
        
        # Add more then one item
        add_to_cart = driver.find_element(By.ID, "add-to-cart-button")
        add_to_cart.click()
        time.sleep(0.25)
        driver.back()
        add_to_cart.click()
        time.sleep(0.25)

        driver.save_screenshot("./screenshots_test2/many_necklaces_in_cart.png")

    # Remove items from cart
        remove = driver.find_element(By.CLASS_NAME, "cart-item-remove")
        remove.click()
        time.sleep(0.25)
        driver.save_screenshot("./screenshots_test2/empty-cart.png")
        

    # Checkout
        checkout = driver.find_element(By.LINK_TEXT, "Checkout")
        driver.execute_script('alert("Checkout link should stay on same page while cart is empty!")')
        time.sleep(2)

        # Switches focus to the new alert
        alert = driver.switch_to.alert

        # Presses "OK" to accept alert
        alert.accept()
        time.sleep(0.25)

        checkout.click()
        driver.execute_script('alert("This is the same page")')
        time.sleep(2)
        alert = driver.switch_to.alert
        
        alert.accept()

    # Alert that all tests have completed successfully
        driver.execute_script('alert("All tests are complete, thank you!")')
        time.sleep(2)

        # Switches focus to the new alert
        alert = driver.switch_to.alert

        # Presses "OK" to accept alert
        alert.accept()
        time.sleep(0.25)
        
    # Logout
        logout = driver.find_element(By.ID, "base_logout_anchor")
        logout.click()
        time.sleep(0.25)
        driver.save_screenshot("./screenshots_test2/logout_test_complete.png")

        # Records the end time of the test
        end_time = time.time()

        # Calculates length of time test took to Execute
        execution_time = end_time - start_time
        print(execution_time)

    except NoSuchElementException as err:
        print(err)
    
    # Closes the Chrome WebDriver instance
    driver.quit()


if __name__ == "__main__":
    main()
