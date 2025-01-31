from selenium import webdriver
import time
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from image import ImageManupulation
from content import generate_post_meta
import schedule
load_dotenv()
# Initialize WebDriver with a custom user agent (to simulate mobile view)
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/15.0 Mobile/15A372 Safari/537.36")
def upload_post():
    try:
        driver = webdriver.Chrome(options=options)
        driver.get("https://x.com/")  # Open the website

        # Wait for the login button to be clickable
  # Wait for the page to load
        login_button =  WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="loginButton"]'))
        )

        # Click the login button
        login_button.click()
        
        text_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="text"]'))
        )

        text_box.send_keys(os.getenv("USER"))
        nesxt_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']"))
        )
        nesxt_button.click()
        # Optionally, submit the form (if it's part of a form)
        # text_box.send_keys(Keys.RETURN)

        time.sleep(2)
        password_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]'))
        )
        password_box.send_keys(os.getenv("PASSWORD"))
        # login_button = driver.find_element(By.XPATH, "//span[text()='Log in']")
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Log in']"))
        )
        login_button.click()
        time.sleep(3)
        post_area = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]'))
        )
        
        post_content = generate_post_meta()
        post_area.send_keys(post_content['post_content'])
        time.sleep(2)
        file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        obj = ImageManupulation()
        file_path = obj.save_image(post_content['image_prompt'])
        file_input.send_keys(file_path)
        send_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')
        # Locate the disabled tweet button
        time.sleep(4)
        tweet_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetButtonInline"]')
        tweet_button.click()
        time.sleep(3)
          # Keeps the browser open
        driver.quit()
    except:
        time.sleep(5)
        driver.quit() 
        upload_post()
def test():
    print("HEllo")
schedule.every().day.at("7:14").do(upload_post)
schedule.every().day.at("12:14").do(upload_post)
schedule.every().day.at("18:14").do(upload_post)


while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute