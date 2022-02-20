from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver_path = ""
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = 'https://en.wikipedia.org/wiki/Main_Page'
driver.get(url)

nr_articles = driver.find_element(By.XPATH,'//*[@id="articlecount"]/a[1]')
nr_articles = driver.find_element(By.CSS_SELECTOR,'#articlecount a')
print(nr_articles.text)

#interaction with wikipedia
search_field = driver.find_element(By.XPATH, '//*[@id="searchInput"]')
search_field.send_keys('Python')
search_field.send_keys(Keys.ENTER)

driver.quit()