from selenium import webdriver
import urllib.request
import os
import json
import time
import pandas as pd

def products(driver, links, itr):
    time.sleep(5)
    for product_base in driver.find_elements_by_class_name('product-base'):
        try:
            links.append( product_base.find_element_by_xpath('./a').get_attribute("href"))
            itr = itr+1
            print(itr)

        except:
            print("Error occured with ", product_base)

    return links, itr

def getlinks(search_string):
    links=[]
    itr = 0
    driver = webdriver.Chrome('chromedriver')
    #driver.get('https://www.myntra.com/')
    driver.get('https://www.myntra.com/women-shorts-skirts')
    time.sleep(4)

    #driver.find_element_by_class_name('desktop-searchBar').send_keys(search_string)
    #driver.find_element_by_class_name('desktop-submit').click()

    while(True):
        if itr>500:
            break
        links, itr = products(driver, links, itr)
        time.sleep(5)
        try:
            driver.find_element_by_class_name('pagination-next').click()
        except:
            driver.close()
            driver.quit()
            break

    print(links)
    print(len(links))
    return links

search_string = "Women Tops, T-Shirts & Shirts"
links = getlinks(search_string)
#find_element_by_class_name('pdp-name').get_attribute("innerHTML")metadata['price'] = driver.find_element_by_class_name('pdp-price').find_element_by_xpath('./strong').get_attribute("innerHTML")

df = pd.DataFrame(links,columns=['link'])
print(df)
df.to_csv('data/links/womenskirtlinks.csv', index=False)
