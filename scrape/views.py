from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

from .models import ProxyList


def scrape_proxy_list():
    driver = webdriver.Chrome()
    driver.get("https://geonode.com/free-proxy-list")
    sleep(10)

    page = driver.page_source
    soup = BeautifulSoup(page, 'lxml')

    excluded_headings = ['ANONYMITY', 'ORG & ASN', 'SPEED', 'RESPONSE', 'GOOGLE', 'LATENCY', 'UPDATED']
    headings = [th.text.strip() for th in soup.find('thead').find_all('th') if th.text.strip() not in excluded_headings]

    data = []
    for row in soup.find('tbody').find_all('tr'):
        row_data = [td.text.strip() for td in row.find_all('td')]
        data.append(row_data)

    result = []
    for row in data:
        row_dict = {}
        for i in range(len(headings)):
            row_dict[headings[i]] = row[i]
        result.append(row_dict)

    for entry in data:
         ProxyList.objects.create(
                ip_address=entry.get('IP address'),
                port=entry.get('Port'),
                protocol=entry.get('Protocols'),
                country=entry.get('Country'),
                uptime=entry.get('Uptime')
                ) 
    driver.close()
