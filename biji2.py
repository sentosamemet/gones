from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

options = {
    'proxy': {
        'http': 'http://bc29ed51a4090debc81d__cr.pe:83cab51ab3cc7226@gw.dataimpulse.com:10002',
        'https': 'https://bc29ed51a4090debc81d__cr.pe:83cab51ab3cc7226@gw.dataimpulse.com:10002',
        'no_proxy': 'localhost,127.0.0.1'
    }
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--verbose")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(seleniumwire_options=options, options=chrome_options)

driver.get("https://sepolia-faucet.pk910.de/#/mine/a83ba048-fff7-40ea-983b-f4f2b8970864")
time.sleep(50000)

div_element = driver.find_element(By.CLASS_NAME, "col-3")
content_text = div_element.text
print(content_text)

#WAKTU MENUNGGU MINING SELESAI
time.sleep(15000)

# Tutup browser
driver.quit()
