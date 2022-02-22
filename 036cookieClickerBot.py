from time import sleep
import os
from matplotlib.style import available
from selenium import webdriver
from selenium.webdriver.common.by import By



chrome_driver_path = ""
driver = webdriver.Chrome(executable_path=chrome_driver_path)
url = 'https://orteil.dashnet.org/cookieclicker/'
driver.get(url)
# print(driver.find_element(By.ID,'productTitle').text)
# print(driver.find_element(By.CSS_SELECTOR,'.documentation-widget a').text)
# print(driver.find_element(By.XPATH,'//*[@id="container"]/li[2]/a').click())
cookie = driver.find_element(By.XPATH,'//*[@id="bigCookie"]')

def gameLogic():
  upgrade = driver.find_elements(By.XPATH,'//*[@id="upgrade*"]')
  # products = driver.find_element(By.ID,'#product0')
  # print(len(products))
  print(len(upgrade))
  # try:
  #   upgrade.click()
  # except:
  #   None
  # for product in products:
  #   try:
  #     product.click()
  #   except:
  #     None

counter = 0
while True:
  if counter%100 == 0:
    gameLogic()
    sleep(2)
    os.system('cls')
  else:
    cookie.click()
  counter += 1