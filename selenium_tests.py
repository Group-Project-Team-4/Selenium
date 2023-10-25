"""
   - Login and create new post automated test
   - Please make a new branch to make any changes! Do not change this directly
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
    driver.get('http://localhost:5000/')  # Enter webapp url

    try:
# Register
        register = driver.find_element(By.ID, "base_register_anchor")
        register.click()
        time.sleep(1.5)
        
        username_input = driver.find_element(By.ID, "register_username_textinput")
        username_input.send_keys("nate")
        time.sleep(1.5)
        
        password_input = driver.find_element(By.ID, "register_password_textinput")
        password_input.send_keys("12345")
        time.sleep(1.5)
        
        password_input.send_keys(Keys.ENTER)
        time.sleep(1.5)

# Login
        login_link = driver.find_element(By.ID, "base_login_anchor")
        login_link.click()
        time.sleep(1.5)

        username_input = driver.find_element(By.ID, "login_username_textinput")
        username_input.send_keys("nate")
        time.sleep(1.5)

        password_input = driver.find_element(By.ID, "login_password_textinput")
        password_input.send_keys("12345")
        time.sleep(1.5)

        login_button = driver.find_element(By.ID, "login_submit_button")
        login_button.click()
        time.sleep(1.5)

# Create a post
        new_post_link = driver.find_element(By.ID, "index_new_post_anchor")
        new_post_link.click()
        time.sleep(1.5)

        title_input = driver.find_element(By.ID, "post_title_textinput")
        title_input.send_keys("How to use selenium for automated testing!")
        time.sleep(1.5)

        body_input = driver.find_element(By.ID, "post_body_textinput")
        body_input.send_keys("Please go to our github repository at this link to learn \
                             how to run automation tests on your web application, \
                             just like this one! \
                             \n https://github.com/Group-Project-Team-4/Selenium")
        time.sleep(1.5)

        # Submit the post
        save_button = driver.find_element(By.ID, "post_submit_button")
        save_button.click()
        time.sleep(1.5)

        # Give time to view post
        time.sleep(2)

# Edit a post
        edit_button = driver.find_element(By.ID, "index_update_post_anchor")
        edit_button.click()
        time.sleep(1.5)
        
        update_title = driver.find_element(By.ID, "update_title_textinput")
        update_title.clear()
        time.sleep(1.5)
        
        update_title.send_keys("Click the link below to get started!")
        time.sleep(1.5)
        
        submit_button = driver.find_element(By.ID, "update_submit_button")
        submit_button.click()
        time.sleep(1.5)
        
# Delete a post
        edit_button = driver.find_element(By.ID, "index_update_post_anchor")
        edit_button.click()
        time.sleep(1.5)
        
        delete_button = driver.find_element(By.ID, "update_delete_button")
        delete_button.click()
        time.sleep(1.5)
        
        # Handle alert
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(1.5)
        
# Alert that all tests have completed succesfully
        driver.execute_script('alert("All tests are complete, thank you!")')
        time.sleep(1.5)

        # Switchs focus to the new alert
        alert = driver.switch_to.alert

        # Presses "OK" to accept alert
        alert.accept()
        time.sleep(1.5)

# Logout
        login_link.click()
        time.sleep(1.5)

    except NoSuchElementException as err:
        print(err)

    driver.quit()


if __name__ == "__main__":
    main()
