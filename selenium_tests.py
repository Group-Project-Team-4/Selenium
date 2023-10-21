"""
   - Example use case of selenium feel free to add onto this to test more feature of selenium.
   - Please make a new branch to make any changes!
   - Then when you are sure there are no bugs and your code is to Pylint standard, 
         you should make a pull request.
   - We should be utilizing all the tools GitHub has to offer us.
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


# Make sure to download ChromeDriver and add to PATH or if using Firefox see selenium documentation
# ChromeDriver: https://googlechromelabs.github.io/chrome-for-testing/#stable

def main() -> None:
    """Web Driver Function"""
    driver = webdriver.Chrome()
    driver.get('https://www.google.com/')  # Enter webapp url

    try:
        google_search = driver.find_element(By.ID, "APjFqb")
        google_search.send_keys("How to use selenium like a pro")
        google_search.send_keys(Keys.ENTER)

        videos_button = driver.find_element(By.XPATH, "//div[@jsname = 'bVqjv']")
        videos_button.click()

    except NoSuchElementException as err:
        print(err)

    time.sleep(60)  # This is here as temp
    driver.quit()


if __name__ == "__main__":
    main()
