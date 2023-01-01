import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create a new Chromium browser instance
driver = webdriver.Chrome()

# Go to Google's homepage
driver.get("http://www.google.com")

# Take a screenshot of the page and save it in the images folder
driver.save_screenshot('images/screenshot.jpg')

# Go to Imgur's homepage
driver.get("https://imgur.com")

# Find the login button and click it
login_button = driver.find_element_by_css_selector('a[href="/login"]')
driver.get(login_button.get_attribute('href'))

# Find the username and password fields and enter your login credentials
username_field = driver.find_element_by_css_selector('input[name="username"]')
username_field.send_keys("YourUsername")
password_field = driver.find_element_by_css_selector('input[name="password"]')
password_field.send_keys("YourPassword")

# Find the login form and submit it
login_form = driver.find_element_by_css_selector('form[action="/login"]')
login_form.submit()

# Wait for the page to load
time.sleep(5)

# Find the "New Post" button and click it
new_post_button = driver.find_element_by_css_selector('a[href="/upload"]')
driver.get(new_post_button.get_attribute('href'))

# Find the file input field and enter the file path to the screenshot
file_input = driver.find_element_by_css_selector('input[type="file"]')
file_input.send_keys(os.getcwd() + '/images/screenshot.jpg')

# Wait for the upload to complete
time.sleep(5)

# Find the submit button and click it to finish the upload
submit_button = driver.find_element_by_css_selector('button[type="submit"]')
submit_button.click()

# Close the browser
driver.close()
