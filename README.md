# Selenium Lab

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

## 4. How to run the program
1. Must have a valid URL or Web application to test
   - You can find one here: [Sample Web Application](https://github.com/Group-Project-Team-4/Web-App)

2. In clone this repository
   - Enter the directory of the cloned repository
   - Open a terminal or command prompt at the directories location

3. Run the program
   - Enter `python nate_login_post_test.py` or `python3 nate_login_post_test.py`
   - Chrome should open and complete the test without any errors

4. Debugging
   - Ensure you have the correct web driver for you browser
   - Ensure it's a environment variable and in your PATH
   - If problems continue, read selenium and your specific  
     webdriver documentation
   - Make an issue on this repository
