from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

options = {
    'proxy': {
        'http': 'http://7f80327c578b86068874__cr.bb:13e3de6667a042d5@gw.dataimpulse.com:10101',
        'https': 'https://7f80327c578b86068874__cr.bb:13e3de6667a042d5@gw.dataimpulse.com:10101',
        'no_proxy': 'localhost,127.0.0.1'
    }
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--verbose")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(seleniumwire_options=options, options=chrome_options)

driver.get("http://217.145.75.33/#/mine/dd2bae4f-da00-4fe4-a3a7-bef7cf2e79e5:8080")
time.sleep(50000)

div_element = driver.find_element(By.CLASS_NAME, "col-3")
content_text = div_element.text
print(content_text)

#WAKTU MENUNGGU MINING SELESAI
time.sleep(15000)

# Tutup browser
driver.quit()
