from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException, WebDriverException
import random
from random import randint
from time import sleep

# set path of chrome driver
s = Service('/usr/local/bin/chromedriver')

# selenium chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('--disable-dev-shm-usage')

# selenium loop to generate realistic traffic
while True:
    try:
        # sets random URL from url.txt
        url = random.choice(open('url.txt').readlines())

        # set webdriver
        driver = webdriver.Chrome(service=s, options=chrome_options)

        # set timeout to 25 on page load
        driver.set_page_load_timeout(25)

        # open page and maximize window
        driver.get(url)
        driver.maximize_window()

        # print URL and page title
        print(url)
        print(driver.title)

        # wait random time between 15-45 seconds before restarting loop
        sleep(randint(15,45))

        # quit driver
        driver.quit()

    # if timeout reached, quit loop and restart    
    except TimeoutException as e:
        print("Timeout on", url, "Restarting loop\n")
        sleep(randint(15,45))
        driver.quit()

    # if WebDriverException (connection loss), restart loop
    except WebDriverException as e:
        print("WebDriverException, restarting loop")
        sleep(randint(15,45))
        driver.quit()