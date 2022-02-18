from bs4 import BeautifulSoup
from getpass import getpass
import requests
import smtplib

#http://myhttpheader.com/
url = 'https://www.amazon.com/dp/B07YGZL8XF/ref=va_live_carousel?pf_rd_r=PKW0JYTYJ1VT9ZN8J58N&pf_rd_p=a442218d-a569-4a1f-9e38-c8621a089b60&pf_rd_m=ATVPDKIKX0DER&pf_rd_t=HighVelocityEvent&pf_rd_i=deals_1_desktop&pf_rd_s=slot-13&asc_contentid=amzn1.amazonlive.broadcast.678c025c-9970-4085-8e0d-bb5591d9ae97&pd_rd_i=B07YGZL8XF&th=1&psc=1'
user_agent = ''
accept_language = ''

webpage = requests.get(url,
                    headers={'Accept-Language':accept_language,
                              'User-Agent':user_agent})
soup = BeautifulSoup(webpage.text,'html.parser')
print(soup.find('span',class_='a-offscreen').text)
price = float(soup.find('span',class_='a-offscreen').text[1:])
print(price)


title = soup.find(id="productTitle").get_text().strip()
print(title)
BUY_PRICE = 300
YOUR_EMAIL = ''
if price < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, getpass())
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
else:
  print('Not low enough')