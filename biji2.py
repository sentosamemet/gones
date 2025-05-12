from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

options = {
    'proxy': {
        'http': 'http://b57efbc8a5479b94f272__cr.jm:70f4e3e9fa23895b@gw.dataimpulse.com:10002',
        'https': 'https://b57efbc8a5479b94f272__cr.jm:70f4e3e9fa23895b@gw.dataimpulse.com:10002',
        'no_proxy': 'localhost,127.0.0.1'
    }
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--verbose")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(seleniumwire_options=options, options=chrome_options)

driver.get("https://sepolia-faucet.pk910.de/#/mine/e0b5b0a3-c74e-463a-aa1e-565732750d0f")
time.sleep(50000)

div_element = driver.find_element(By.CLASS_NAME, "col-3")
content_text = div_element.text
print(content_text)

#WAKTU MENUNGGU MINING SELESAI
time.sleep(15000)

# Tutup browser
driver.quit()
