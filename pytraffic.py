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

# random number for log file
file_name = str(randint(500000,10000000))

# selenium loop to generate realistic traffic
while True:
    try:
        # sets random URL from url.txt
        #url = random.choice(open('url.txt').readlines())
        url = random.choice(open('url.txt').readlines())

        # open logfile
        logfile = open("/logs/"+file_name+".log", "a")

        # log attempt
        logfile.write(str("Attempting to access " +str(url)))

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

        # after successful page load, close log file for write
        logfile.close()

        # wait random time between 15-45 seconds before restarting loop
        sleep(randint(15,45))

        # quit driver
        driver.quit()

    # if timeout reached, restart loop    
    except TimeoutException as e:

        # log TimeoutException, close log file
        logfile.write(str("TimeoutException: 25 second timeout reached on " +str(url)))
        logfile.close()

        # print TimeoutException to docker logs and quit driver
        print("Timeout on", url, "Restarting loop")
        sleep(randint(15,45))
        driver.quit()

    # if WebDriverException (connection loss), restart loop
    except WebDriverException as e:

        # log WebDriverException, close log file
        logfile.write(str("WebDriverException: connection dropped on " +str(url)))
        logfile.close()

        # print WebDriverException to docker logs and quit driver
        print("WebDriverException, restarting loop")
        sleep(randint(15,45))
        driver.quit()