from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver_path = ""
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = 'http://secure-retreat-92358.herokuapp.com/'
driver.get(url)

#interaction with form
input_fields = driver.find_elements(By.CSS_SELECTOR, 'input')
sign_up_button = driver.find_element(By.XPATH,'/html/body/form/button')
txt_inputs = ['Erik','Skaar','noreply@erik.skaar']

for txt,field in zip(txt_inputs,input_fields):
  field.send_keys(txt)
sign_up_button.click()
sleep(0.5)
driver.quit()