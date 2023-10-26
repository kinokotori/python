from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)


    
  
def start(url):
  driver = webdriver.Chrome(options = option)
  driver.implicitly_wait(10)
  driver.get(url)
  return driver

