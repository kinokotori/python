import requests
from bs4 import BeautifulSoup
from connect import start
from selenium.webdriver.common.by import By
import hashlib

driver = start()

driver.implicitly_wait(10)
imgs = driver.find_elements(By.CLASS_NAME,'medium-zoom-image')


for img in imgs:
    src = img.get_attribute('src')
    blob = requests.get(src).content
    target_img = open('imgs/'+hashlib.sha256(src.encode()).hexdigest()+'.png','wb')
    target_img.write(blob)
    target_img.close
    


