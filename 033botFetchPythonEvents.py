from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = ""
driver = webdriver.Chrome(executable_path=chrome_driver_path)
url = 'https://www.python.org/'
driver.get(url)
upcoming_events = driver.find_element(By.XPATH,'//*[@id="content"]/div/section/div[2]/div[2]/div')
times = upcoming_events.find_elements(By.CSS_SELECTOR,'li time')
titles = upcoming_events.find_elements(By.CSS_SELECTOR,'li a')
events = {}

for i in range(len(times)):
  events[i] = {
    'time':times[i].text,
    'titles':titles[i].text
  }

for event in events:
  print(event)