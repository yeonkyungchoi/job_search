import requests
from bs4 import BeautifulSoup
import csv

keyword = '데이터분석'
page = '50'
data_list = []

for n in range(1, int(page)+1):

    response = requests.get(f'https://www.jobkorea.co.kr/Search/?stext={keyword}&tabType=recruit&Page_No={n}')
    soup = BeautifulSoup(response.text,'html.parser').select_one('div.list-default')
    jobs = soup.select('li.list-post')
    
    #number = soup.select_one('li.list-post')['data-listno']

    for job in jobs:
        company = job.select_one('a.name').text.strip()
        detail = job.select_one('a.title').text.strip()
        experience = job.select_one('span.exp').text.strip()
        location = job.select_one('span.loc').text.strip()
        number = job['data-listno'].strip()
        data_list.append([company, detail, experience, location, number])

        # for tbcol in job:
        #     tbnum = requests.get(f'https://www.jobkorea.co.kr/Recruit/GI_Read/42584617?Oem_Code=C1&logpath=1&stext={keyword}&listno={number}')
        #     soupp = BeautifulSoup(tbnum.text,'html.parser')
        #     #tbList = soupp.select_one('dl.tbList')
        #     print(soupp)
            
#print(company, detail, experience, location, number)
csv_file_path = "/Users/yily/Documents/GitHub/job_search/job_data.csv"
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['회사', '상세정보', '경력', '지역', '번호']) 
    writer.writerows(data_list)  

print("CSV 파일 생성 완료:", csv_file_path)