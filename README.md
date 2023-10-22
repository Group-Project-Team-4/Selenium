# Selenium Lab

<h3>1. Introduction</h3>

**1.1. Purpose:** This repository contains a web automation program designed to navigate and interact with different parts of a given website. This system will test to ensure that all automation, UI, and navigation have the proper functionality.

**1.2. Scope:** *In Scope*: Web browser automation, UI element interaction, validation, reporting.
*Out-of-Scope*: Future expansions, though we are creating this program with the ability to easily add on.

**1.3. Definitions and Acronyms:**
+ **UI**: User Interface
+ **WebDriver**: A collection of open-source APIs used for automating web application testing. 

<h3>2. System Overview</h3>

**2.1 Tools & Technologies**
+ Python
+ Selenium WebDriver
+ ChromeDriver
+ Supported browsers: Firefox, Chrome, Safari, & Edge


<b>Python:</b> Download and install the latest version of Python. Python can not be downloaded through the command prompt itself, yet installation can be verified through the command prompt: [https://www.python.org]

<b>Google Chrome</b>: Default browser that is being used with Selenium. Make sure the latest version is installed.
ChromeDriver: [https://googlechromelabs.github.io/chrome-for-testing/#stable].


<h3>Installation</h3>
<b>Set up to run selenium_tests.py test.</b>

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

   
