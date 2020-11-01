from selenium import webdriver
import urllib.request
import os
import json
import time
import pandas as pd

link = "https://www.myntra.com/jackets/campus-sutra/campus-sutra-men-off-white-solid-tailored-jacket/10890976/buy"
driver = webdriver.Chrome('chromedriver')
dfl = pd.read_csv("data/links/womenskirtlinks.csv")

column_names = ["title", "name", "price", "Waist Rise", "Length", "Fit", "Brand Fit Name", "Print or Pattern Type", "Closure", "Type of Pleat", "Weave Type", "Fly Type", "productId"]

df = pd.DataFrame(columns = column_names)

i=0

for link in dfl["link"].tolist():
    if i==350:
        break

    try:
        metadata = {}
        driver.get(link)
        metadata['title'] = driver.find_element_by_class_name('pdp-title').get_attribute("innerHTML")
        metadata['name'] = driver.find_element_by_class_name('pdp-name').get_attribute("innerHTML")
        metadata['price'] = driver.find_element_by_class_name('pdp-price').find_element_by_xpath('./strong').get_attribute("innerHTML")

        try:
            driver.find_element_by_class_name('index-showMoreText').click()
        except:
            j = 0;
        metadata['specifications'] = {}

        #commmment
        for index_row in driver.find_element_by_class_name('index-tableContainer').find_elements_by_class_name('index-row'):
            metadata[index_row.find_element_by_class_name('index-rowKey').get_attribute("innerHTML")] =  index_row.find_element_by_class_name('index-rowValue').get_attribute("innerHTML")
        metadata['productId'] = driver.find_element_by_class_name('supplier-styleId').get_attribute("innerHTML")

        df = df.append(metadata, ignore_index=True)
        #neech ka images ke liye hai

        base = "C:\\Users\\Ipshita\\Desktop\\github\\Myntra"
        itr = 1

        for image_tags in driver.find_elements_by_class_name('image-grid-image'):
            image_path = os.path.join("images//wskirts//" + metadata['productId'] + '_'+str(itr)+".jpg")
            urllib.request.urlretrieve( image_tags.get_attribute('style').split("url(\"")[1].split("\")")[0], image_path)
            itr +=1

        #print(metadata)
        i = i+1
        print(str(i) + " of 17,000 products")

    except:
        i = i+1
        print(str(i) + " of 17,000 products - error")

df.to_csv("data/wskirts.csv")

driver.close()
driver.quit()
