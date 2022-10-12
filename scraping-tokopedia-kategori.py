"""
ini adalah program scrapping data kategori di tokopedia. 
Program ini membutuhkan file geckodriver.exe dan browser firefox untuk dapat dijalankan.
Hasilnya ditampung dalam list, lalu diubah ke format json untuk disimpan dalam file.
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

options1 = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options1)
driver.get("https://www.tokopedia.com/")
a = ActionChains(driver)
b = driver.find_element(By.CSS_SELECTOR, ".css-1iy09lx")
a.move_to_element(b).perform()
WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".css-12nkv7")))

category = driver.find_elements(By.CSS_SELECTOR, ".css-me46ht")

list_of_category = []
list_of_category_full = []

for x in category:
    x_innerHTML = x.get_attribute("innerHTML").replace("&amp;", "&")
    list_of_category.append(x_innerHTML)
    dict = {"name" : x_innerHTML, "childs" : []}
    list_of_category_full.append(dict)

pointer1 = 0

for x in list_of_category:

    if pointer1 != 0:
        driver.execute_script("return arguments[0].scrollIntoView(true);", category[pointer1])
        a.move_to_element(category[pointer1]).perform()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".css-5j1t1q")))

    sub_category_name = driver.find_elements(By.CSS_SELECTOR, ".css-1qaqbbz")
    sub_category_parent = driver.find_elements(By.CSS_SELECTOR, ".css-1owj1eu")
    pointer2 = 0

    for y in sub_category_name:
        y_innerHTML = y.get_attribute("innerHTML").replace("&amp;", "&")
        dict = {"name" : y_innerHTML, "childs" : []}
        list_of_category_full[pointer1]["childs"].append(dict)
        sub_category_child = sub_category_parent[pointer2].find_elements(By.CSS_SELECTOR, ".css-1nykm5o")

        for z in sub_category_child:
            z_innerHTML = z.get_attribute("innerHTML").replace("&amp;", "&")
            dict = {"name" : z_innerHTML}
            list_of_category_full[pointer1]["childs"][pointer2]["childs"].append(dict)
            
        pointer2 = pointer2 + 1

    pointer1 = pointer1 + 1

json_decode = json.dumps(list_of_category_full, indent=4)

with open("json-file-tokopedia-kategori.json", "w") as outfile:
    outfile.write(json_decode)