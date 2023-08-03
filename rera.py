import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


def main():
    code = 519
    district_name = 'Mumbai City'
    options = Options()
    ua = UserAgent()
    userAgent = ua.random
    print(userAgent)
    options.add_argument(f'user-agent={userAgent}')
    browser = webdriver.Chrome(options=options)
    action = ActionChains(browser)
    url = "https://maharera.mahaonline.gov.in/"
    browser.get(url)
    browser.find_element(By.LINK_TEXT,'English').click()
    browser.find_element(By.LINK_TEXT,"Registration").click()
    browser.find_element(By.LINK_TEXT,"Registered Projects").click()
    obj = browser.switch_to.alert
    obj.accept()
    w=browser.window_handles
    browser.switch_to.window(w[1])

    #browser.find_element(By.CSS_SELECTOR,"input[type='radio'][value='Promoter']").click()
    element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[type='radio'][value='Promoter']")))
    element.click()
    #browser.find_element_by_xpath(".//input[type='radio'] [name='Type']")[0].click()
    #Select District and State
    browser.find_element(By.ID,'btnAdvance').click()
    #state
    selectSta = Select(browser.find_element(By.ID,'State'))
    selectSta.select_by_value('27')
    time.sleep(3)
    #  district 
    selectDis = Select(browser.find_element(By.ID,'District'))
    selectDis.select_by_value('519')
    time.sleep(3)
    # browser.find_element(By.ID, 'District').send_keys('519')
    browser.find_element(By.ID,'btnSearch').click()

    time.sleep(3)



    #Getting total number of pages

    total_pgs= browser.find_element(By.ID,'TotalPages').get_attribute('value')

    view_lists = browser.find_elements(By.XPATH, "(//tr[@class='grid-row '])/td[7]/b/a[2]")
    for rec in view_lists:
        print("Document Name__________________-", rec.get_attribute('data-docname'))
    

    time.sleep(5)
    print('District Scrapped')
    browser.quit()

    # driver.close()
    
run = None
if __name__ == '__main__':
    run = main()