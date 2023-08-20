import requests
from bs4 import BeautifulSoup
import pymysql
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()
drive = webdriver.Chrome()

keyword = '데이터분석'
page = '1'

response = drive.get(f'https://www.jobkorea.co.kr/Recruit/GI_Read/42584617?Oem_Code=C1&logpath=1&stext={keyword}&listno={page}')
page_source = drive.page_source
soup = BeautifulSoup(page_source, 'html.parser')
tbList = soup.select_one('dl.tbList')
print(tbList)
# for job in jobs:
#     company = job.select_one('a.name').text.strip()
#     detail = job.select_one('a.title').text.strip()
#     experience = job.select_one('span.exp').text.strip()
#     location = job.select_one('span.loc').text.strip()
#     number = job['data-listno'].strip()
#     print(company, detail, experience, location, number)
