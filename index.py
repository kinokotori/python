import requests
from bs4 import BeautifulSoup
from connect import start
from selenium.webdriver.common.by import By
import hashlib
import os

driver = start('https://juejin.cn/post/6844903697047257101')

driver.implicitly_wait(10)
imgs = driver.find_elements(By.CLASS_NAME,'medium-zoom-image')


os.mkdir(os.path.join(os.getcwd(), 'imgs'))
for img in imgs:
    src = img.get_attribute('src')
    blob = requests.get(src).content
    target_img = open('imgs/'+hashlib.sha256(src.encode()).hexdigest()+'.png','wb')
    target_img.write(blob)
    target_img.close
    


