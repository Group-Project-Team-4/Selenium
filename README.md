# Selenium Tutorial

## 1. Introduction

**1.1. Purpose:** This repository contains a web automation program designed to navigate and interact with different parts of a given website. This system will test to ensure that all automation, UI, and navigation have the proper functionality.

**1.2. Scope:** *In Scope*: Web browser automation, UI element interaction, validation, reporting.
*Out-of-Scope*: Future expansions, though we are creating this program with the ability to easily add on.

**1.3. Definitions and Acronyms:**
+ **UI**: User Interface
+ **WebDriver**: A collection of open-source APIs used for automating web application testing. 

## 2. System Overview

**2.1 Tools & Technologies**
+ Python
+ Selenium WebDriver
+ ChromeDriver
+ Supported browsers: Firefox, Chrome, Safari, & Edge


**Python:** Download and install the latest version of Python. Python can not be downloaded through the command prompt itself, yet installation can be verified through the command prompt:  
[https://www.python.org]

**Google Chrome**: Default browser that is being used with Selenium. Make sure the latest version is installed.  
[Download here](https://googlechromelabs.github.io/chrome-for-testing/#stable)


## 3. Install Selenium

Selenium requires a web driver to interface with a web browser. 
1. Download ChromeDriver based on platform & add PATH to enviroment variables.
+ Search 'env' through windows search bar, and select 'Edit the system enviroment variables', select Enviroment Variables, select Path, Edit, New, and paste system PATH, select OK.
2. Verify Python installation:  
   `python --version`

3. Install Selenium in command prompt.  
   `pip install selenium`

   **To verify selenium is installed correctly:**
   + type 'python' in cmd prompt to launch python interpreter.
   + type 'import selenium'
   If there are no errors and you are returned to the command prompt without any messages, Selenium is installed correctly.

## 4. How to run the test scripts
1. Must have a valid URL or Web application to test
   - You can find one here: [Sample Web Application](https://github.com/Group-Project-Team-4/Web-App)

2. In clone this repository
   - Enter the directory of the cloned repository
   - Open a terminal or command prompt at the repositories location

3. Run the program
   - Test script `test_script_1.py` accomplishes register, login, adding an item to cart, checking out, and purchasing
   - Test script `test_script_2.py` accomplishes register, login, adding items to cart, removing items from cart, attempt empty checkout, and logout
   - Chrome should automatically open and complete the test without any errors

4. Debugging
   - Ensure you have the correct web driver for you browser
   - Ensure it's a environment variable and in your PATH
   - If problems continue, read selenium and your specific  
     webdriver documentation
   - Make an issue on this repository

5. Start the session
   `driver = webdriver.Chrome()`

6. Take action on browser
   `driver.get('http://localhost:5000/')`

7. Register for an account
   - Find the register link by the link text, then click the link and save a screenshot to verify the register page displayed correctly.
 
   `register = driver.find_element(By.LINK_TEXT, "Register")
   register.click()
   driver.save_screenshot("./screenshots_test1/register_page.png")
   time.sleep(0.25)`

8. Login
   Find the login link by the login text, then click the link and save a screenshot to verify the login page displayed correctly.

   `login_link = driver.find_element(By.ID, "base_login_anchor")
   login_link.click()
   time.sleep(0.25)`

9. Shop for an item
   Enter the shop and click the Shop Now link, proceed to add an item to the cart and save a screen shot to verify the shop page displayed correctly. 

   `enter_shop = driver.find_element(By.LINK_TEXT, "Shop Now")
   enter_shop.click()
   driver.save_screenshot("./screenshots_test1/enter_shop.png")
   time.sleep(0.25)`

   `add_to_cart = driver.find_element(By.ID, "add-to-cart-button")
   add_to_cart.click()
   driver.save_screenshot("./screenshots_test1/watch_in_cart.png")
   time.sleep(0.25)`

10. Checkout
   Find the checkout link by the link text, then click the link and save a screenshot to verify the checkout page displayed correctly.

   `checkout = driver.find_element(By.LINK_TEXT, "Checkout")
   checkout.click()
   driver.save_screenshot("./screenshots_test1/checkout.png")
   time.sleep(0.25)`

11. Alert that all tests have completed successfully.
    Verify the alert message displayed correctly and take a screenshot.

   `driver.save_screenshot("./screenshots_test1/end_test.png")
   driver.execute_script('alert("All tests are complete, thank you!")')
   time.sleep(3)`

12. Logout
   Find the logout link by the link text, then click the link and save a screenshot to verify the log out page displayed correctly.

   `logout = driver.find_element(By.ID, "base_logout_anchor")
   logout.click()
   time.sleep(0.25)`

13. End session
   - `driver.quit()`



