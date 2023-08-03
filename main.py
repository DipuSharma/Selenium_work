import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
product_type = []
product_dict = {}

def main():
    try:
        driver = webdriver.Chrome()
        action = ActionChains(driver)

        url = 'https://www.flipkart.com/'
        driver.get(url=url, 'html.parser')
        # Get all Product Type
        # close_login_model = driver.find_element(By.CLASS_NAME, '_2KpZ6l').click()
        product_type_list = driver.find_elements(By.XPATH, "//div[@class='eFQ30H']")
        for elements_type in product_type_list:
            product_type.append(elements_type.text)
            action.move_to_element(elements_type).perform()
            type_data_list = elements_type.find_elements(By.CLASS_NAME, "_6WOcW9")
            if type_data_list:
                product_dict[elements_type.text] = type_data_list
                print(len(type_data_list))
            else:
                print("List Empty")

            time.sleep(1)
        # print(type(product_dict), end=' ')

        # print(product_dict.keys())
        driver.close()
    except:
        print("Please try after some time")
    
run = None
if __name__ == '__main__':
    run = main()


# browser.quit()