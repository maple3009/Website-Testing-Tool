# Website-Testing-Tool
Using selenium webdriver to automate website testing for specific a website. No exception handling has been implemented as of now.

Before running program:
pip install selenium in cmd or terminal
AND
download the cooresponding webdriver for the browser being implemented. I used Chrome WebDriver.
https://sites.google.com/a/chromium.org/chromedriver
Either place WebDriver in \venv\Scripts or reference the PATH.

I made a testcase_info.py for inputs. Can change its values to suit your needs.
name = "name"
email = "example@email.com"
subject = "subject"
message = "message"

In case some of the code do not work, replace most of them with the commented out code.
driver.execute_script("document.getElementById('yourElementId').value='yourValue';") has been giving me varying results.
