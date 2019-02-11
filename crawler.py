from selenium import webdriver
import time
from bs4 import BeautifulSoup
import urllib.request
import os
from members.models import *

driver = webdriver.Chrome('/Users/mac/projects/ChromeWebDriver/chromedriver')

driver.implicitly_wait(3)

driver.get('http://www.nba.com/teams/')
time.sleep(3)

### 각 팀별 url 페이지
team_url_list = driver.find_elements_by_xpath("//div/div/div[@class='team__list']/a")
detail_urls = [url.get_attribute("href") for url in team_url_list]


### 각 팀별 이름 출력
team_name = [url.get_attribute("innerText") for url in team_url_list]

### 각 팀별 이미지 출력
team_img_urls = driver.find_elements_by_xpath("//div/div/div[@class='team__list']/img")
team_img_url = [url.get_attribute("src") for url in team_img_urls]

for url, name in zip (team_img_url, team_name):
    dirName = name
    try:
    # Create target Directory
        os.mkdir(f'static/{dirName}')
        print("Directory ", dirName,  " Created ")


    except FileExistsError:
        print("already exists ", dirName)
        pass
    urllib.request.urlretrieve(url, f'static/{name}/{name}.svg')
