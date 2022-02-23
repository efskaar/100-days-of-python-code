from selenium import webdriver
from selenium.webdriver.common.by import By



chrome_driver_path = "C:/Users/skaar/.wdm/drivers/chromedriver/win32/98.0.4758.102/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
url = 'https://orteil.dashnet.org/cookieclicker/'
driver.get(url)
cookie = driver.find_element(By.XPATH,'//*[@id="bigCookie"]')

def gameLogic():
  #upgradesFirst
  buyUpgrade()

  #buy products second
  buyProducts()

def buyUpgrade():
  for i in range(3):
    try:
      upgrade = driver.find_element(By.XPATH,'//*[@id="upgrade0"]')
      upgrade.click()
    except:
      None

def buyProducts():
  for i in range(18,-1,-1):
    try:
      product = driver.find_element(By.XPATH,f'//*[@id="product{i}"]')
      for i in range(3):
        product.click()
    except:
      None

def clickGoldenCookie():
  try:
    golden_cookie = driver.find_element(By.XPATH,f'//*[@id="shimmers"]')
    golden_cookie.click()
  except:
    None

counter = 1
while True:
  if counter%1000 == 0:
    gameLogic()
    counter = 1
  elif counter%499 == 0:
    clickGoldenCookie()
  else:
    cookie.click()
  counter += 1