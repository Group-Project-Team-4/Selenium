<h3>Software Requirement Specification - Selenium Lab</h3>

<h3>1. Introduction</h3>

**1.1. Purpose:** This SRS provides a detailed software requirement specification tailored to the Selenium Lab. The web automation program is designed to navigate and interact with different parts of a given website. This system will test to ensure that all automation, UI, and navigation have the proper functionality.

**1.2. Scope:** The scope of this lab includes the setup of Selenium, creating test scripts, and executing them on a sample web application.

**1.3. Definitions and Acronyms:**
+ **UI**: User Interface
+ **WebDriver**: A collection of open-source APIs used for automating web application testing. 

<h3>2. System Overview</h3>

**2.1 Objectives of the Selenium Lab**
+ Automate browser actions for web application testing.
+ Understand and utilize Selenium WebDriver using Python.
+ Validate web application UI elements and functionalities.

**2.2 Tools & Technologies**
+ Python
+ Selenium Web Driver

<h3>3. Functional Requirements **</h3>

**3.1 Web Browser Automation**
+ Automate tasks like opening a web browser, navigating to a webpage, clicking on links, filling forms, and closing the browser.

**3.2 UI Element Interaction**
+ Identify and interact with various UI elements such as search boxes, dropdown lists, and buttons.

**3.3 Validation**
+ Validate webpage elements to ensure that they display the expected values or behaviors.

**3.4 Capture Screen Shots**
+ Implement functionality to capture and store screenshots during test execution for result validation and error analysis.

**3.5. Reporting**
+ Generate test execution logs or reports showcasing the passed, failed, and skipped tests.

<h3>4. Non-functional Requirements</h3>

**4.1. Performance**
+ The web app should load within 3 seconds after clicking a link
+ Test script execution should not exceed 2 minutes per script.

**4.2. Reliability**
+ Test script execution results should be consistent across runs.
+ The framework shall recover gracefully from unexpected failures.

**4.3. Scalability**
+ The framework architecture should support the addition of new test scripts without affecting existing functionality.
+ The system must be compatible with major web browsers such as Chrome, Microsoft Edge, Firefox, IE, and Safari.

<h3>5. Environment & Setup</h3>

**Development & testing environment specifics, such as:**
+ Browsers supported (e.g., Chrome, Firefox, Safari).
+ Selenium WebDriver  4.13.0 or higher.
+ Python 3.12.0 or higher.

<h3>6. Deliverables</h3>

+ Automated test scripts for specified test scenarios.
+ Documentation on:
+ Steps to set up and run the tests.
+ Explanation of each test script and its objectives.
+ Screenshots folder containing the captured images.
+ Test execution report.

<h3>7. Conclusion</h3>

+ The Selenium Testing Framework SRS provides a clear and detailed outline of the functional and non-functional requirements. This framework aims to empower automated testing for web applications, ensuring efficiency, scalability, and reliability in the testing process.

<h3>Appendices</h3>

**8.1 Sample Test Scenarios**

+ **Scenario 1: Register Functionality Test**
**Application/Page:** Cool Clothing Store eCommerce Website

**Steps**

1. Nagigate to the eCommerce site's register page.
2. Enter valid username and password that meets requirements.
3. Click on the "Register" button.
4. Expected Behavior: User should be logged in successfully and redirecteed to the homepage. 

+ **Scenario 2: Login Functionality Test**

**Application/Page:** Cool Clothing Store eCommerce Website

**Steps:**

1. Navigate to the eCommerce site's login page.
2. Enter valid username and password.
3. Click on the "Login" button.
4. Expected Behavior: User should be logged in successfully and redirected to the homepage.

+ **Scenario 3: Cart Addition Test**

**Application/Page:** Cool Clothing Store eCommerce Website

**Steps:**

1. Navigate to a product page. (e.g., shoes page)
2. Click on the "Add to Cart" button
3. Navigate to the cart page. 
4. Expected Behavior: The selected shoes should appear in the cart.

+ **Scenario 4: Check out Test**

**Application/Page:** Cool Clothing Store eCommerce Website

**Steps:**

1. Navigate to shopping cart page.
2. Fill in required shipping/payment details.
3. Click on the "Pay $XX.XX" button. 
4. Expected Behavior: User should be redirected to "Checkout Success" page.