from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)


    
  
def start():
  driver = webdriver.Chrome(options = option)
  driver.implicitly_wait(10)
  driver.get('https://juejin.cn/post/7074779332819812389?searchId=20231026172110E132644A4B6A590E3ADC')
  return driver

