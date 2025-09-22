# basics 
from time import sleep # for timing
from random import uniform, randint # to mimic human typinf sped
from os import system, name # to call clear cmd 

# selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# setup 
path = 'PATH TO CHROMEDRIVER HERE' # replace inside the quotes the path to your chromedriver. do not delete the quotes.
options = Options()
options.add_experimental_option('detach', True)
options.page_load_strategy = 'eager'
service = Service(path)

driver = webdriver.Chrome(options=options, service=service)



def nitro():

    system('cls' if name == 'nt' else 'clear')

    driver.get('https://www.nitrotype.com/login')

    while True:

        system('cls' if name == 'nt' else 'clear')
        
        # DETECT RACE

        try:

            print("Detecting Race..")

            WebDriverWait(driver, 120).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.dashShield-layer .dashShield-layer--top'))
            )

            print("Race detected!")
            
            

        except:
            continue

        
        # GET LETTERS

        try:

            letters = WebDriverWait(driver, 30, poll_frequency=0.2).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.dash-letter'))
            )

            sentence = ''.join([l.get_attribute("textContent") for l in letters])
            sentence = sentence.replace("\xa0", " ")
            print(f'\n{sentence}')
        
        except:

            print('Failed to get paragraph, refreshing..')
            driver.refresh()
            continue

    
        # DETECT RACE START

        try:
            action = ActionChains(driver)
            print("Waiting for start..")

            WebDriverWait(driver, 15).until_not(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.dashShield-layer .dashShield-layer--top'))
            )

            sleep(0.75)

            action.send_keys(Keys.ENTER)
            action.perform()

            for char in sentence:

                action.send_keys(char)
                action.pause(0.06 + uniform(0.005, 0.025))  # CHANGE 0.06 TO WHATEVER YOU WANT, FASTER WOULD BE LESS THAN 0.06 AND SLOWER WOULD BE GREATER!
            
            action.perform()

        except:
            print('Unexpected error, refreshing')
            driver.refresh()
            continue

        
        # DETECT RACE END

        try:
            
            print("Waiting for next race")

            button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn--primary.btn--fw.btn--gloss.animate--iconSlam.dhf'))
            )
            button.click()

            continue

        except:

            print("Unexpected Error, refreshing.. ")

            driver.refresh()
            continue


if __name__ == '__main__':
    nitro()
