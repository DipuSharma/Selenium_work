import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
def main():
    driver = webdriver.Chrome()
    action = ActionChains(driver)

    # Login code test start

    # url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    # driver.get(url=url)
    # time.sleep(2)

    # driver.find_element(By.NAME, 'username').send_keys("Admin")
    # driver.find_element(By.NAME, 'password').send_keys('admin123')
    # driver.find_element(By.XPATH, "(//button[normalize-space()='Login'])[1]").click()

    # current_title = driver.title
    # expt_title = "OrangeHRM"

    # if current_title == expt_title:
    #     print("Login successfully")
    # else:
    #     print("You are not logged in")

    # Login code test end



    # Click on LinkText code start
    # url = 'https://demo.nopcommerce.com/'
    # driver.get(url=url)
    # driver.maximize_window()
    # time.sleep(1)
    # # driver.find_element(By.LINK_TEXT, 'Register').click()
    # driver.find_element(By.PARTIAL_LINK_TEXT, 'Reg').click()

    # Click on LinkText code end


    # listing code start
    # url = 'https://www.shoppersstop.com/'
    # driver.get(url=url)
    # driver.maximize_window()

    # slider_list = driver.find_elements(By.CLASS_NAME, 'slick-track')
    # print(len(slider_list))  # Total number of slider
    # anchor_lists = driver.find_elements(By.TAG_NAME, 'a')
    # print(len(anchor_lists))  # Total number of a tag

    # tag & id combination
    # driver.find_element(By.CSS_SELECTOR, 'tag_name#id_name')

    # Tag & class combination 
    # driver.find_element(By.CSS_SELECTOR, 'tag_name.class_name')

    # Tag & attribute
    # driver.find_element(By.CSS_SELECTOR, 'tag_name[attr_name=value]')

    # Combination of Tag class and attribute
    # driver.find_element(By.CSS_SELECTOR, 'tag_name.classname[attr_name=attr_value]')

    # #Xpath 
    # Absolute/Full xpath 
        #  Ex: html/body/nav/div/div[1]/ul[3]/li[1]/a

    #  Relative/Partial xpath
        #  Ex: "//*[@id-'header-navbar']/ul[3]/li[1]/a"

    # # Find with Or operation
    # driver.find_element(By.XPATH, "tag_name[@attr_name1='attr_value1' or @attr_name2='attr_value2']")

    # Find with And operation
    # driver.find_element(By.XPATH, "tag_name[@attr_name1='attr_value1' annd @attr_name2='attr_value2']")

    # # Parent and Chile xpath
    # url = 'https://money.rediff.com/gainers/bse/daily/groupa'
    # driver.get(url=url)
    # driver.maximize_window()
    # self
    # element = driver.find_element(By.XPATH, "//a[contains(text(), 'India Cements Lt')]/self::a").text
    # print(element)

    # # Parent
    # element = driver.find_element(By.XPATH, "//a[contains(text(), 'India Cements Lt')]/parent::td").text
    # print(element)


    # # Child
    # element = driver.find_element(By.XPATH, "//a[contains(text(), 'India Cements Lt')]/ancestor::tr/child::td").text
    # print(element)

    # # Row data in list 
    # elements = driver.find_elements(By.XPATH, "//a[contains(text(), 'India Cements Lt')]/ancestor::tr/child::td")
    # for data in elements:
    #     print(data.text, end=' ')

    # # Ancestor 
    # element = driver.find_element(By.XPATH, "//a[contains(text(), 'India Cements Lt')]/ancestor::tr").text
    # print(element)

    # # Descendant 
    # descendants = driver.find_elements(By.XPATH, "//a[contains(text(), 'India Cements Lt')]/ancestor::tr/descendant::*")
    # print("Number of Decendant :", len(descendants))

    # # Following 
    # followings = driver.find_elements(By.XPATH, "//a[contains(text(), 'India Cements Lt')]/ancestor::tr/following::*")
    # print("Number of Following :", len(followings))

    # # Following Sibling
    # following_siblings = driver.find_elements(By.XPATH, "//a[contains(text(), 'India Cements Lt')]/ancestor::tr/following-sibling::*")
    # print("Number of Following Sibling:", len(following_siblings))

    # # Preceding
    # precedings = driver.find_elements(By.XPATH, "//a[contains(text(), 'India Cements Lt')]/ancestor::tr/preceding::*")
    # print("Number of Following Sibling:", len(precedings))

    # # On Selection field
    # checkbox = driver.find_element(By.XPATH, "//tag_name[@attr_name='attr_value']")
    # print("Checkbod Status :", checkbox.is_enabled())
    # print("Checkbod Selection Status:", checkbox.is_selected())


    # listing code end

    url = 'https://maharerait.mahaonline.gov.in/searchlist/search?MenuID=1069'
    driver.get(url=url)
    driver.maximize_window()
    time.sleep(2)

    driver.close()
    
run = None
if __name__ == '__main__':
    run = main()


# browser.quit()