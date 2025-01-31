from selenium import webdriver
import time
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from image import ImageManupulation
from content import generate_post_meta
import logging

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)

# Initialize WebDriver with a custom user agent (to simulate mobile view)
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/15.0 Mobile/15A372 Safari/537.36")

def upload_post():
    try:
        driver = webdriver.Chrome(options=options)
        driver.get("https://x.com/")  # Open the website

        # Wait for the login button to be clickable
        logging.info("Waiting for the login button...")
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="loginButton"]'))
        )
        login_button.click()
        logging.info("Login button clicked.")
        
        # Enter username
        text_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="text"]'))
        )
        text_box.send_keys(os.getenv("USER"))
        
        # Click next button
        nesxt_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']"))
        )
        nesxt_button.click()

        # Enter password
        password_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]'))
        )
        password_box.send_keys(os.getenv("PASSWORD"))
        
        # Click login button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Log in']"))
        )
        login_button.click()

        logging.info("Successfully logged in.")
        
        # Wait for the post area to be visible
        post_area = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]'))
        )

        # Generate post content
        post_content = generate_post_meta()
        post_area.send_keys(post_content['post_content'])
        
        # Handle image upload
        file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        obj = ImageManupulation()
        file_path = obj.save_image(post_content['image_prompt'])
        file_input.send_keys(file_path)
        time.sleep(2)
        # Locate the tweet button
        tweet_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="tweetButtonInline"]'))
        )
        
        # Click the tweet button
        tweet_button.click()
        logging.info("Tweet posted successfully.")

        input("Press Enter to close...")  # Keeps the browser open
        driver.quit()

    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        driver.quit()
        time.sleep(5)
        logging.info("Retrying upload...")
        upload_post()

upload_post()
