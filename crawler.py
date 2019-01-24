from selenium import webdriver
import time
from bs4 import BeautifulSoup
import urllib


driver = webdriver.Chrome('/Users/mac/projects/ChromeWebDriver/chromedriver')
driver.implicitly_wait(3)
#NBA 들어가기
driver.get('http://www.nba.com/teams/')


time.sleep(3)
# 팀별 url 필터링
team_url_list = driver.find_elements_by_xpath("//div/div/div[@class='team__list']/a")
detail_urls = [url.get_attribute("href") for url in team_url_list]

time.sleep(3)
# 팀별 이름 필터링
team_name = [url.get_attribute("innerText") for url in team_url_list]

time.sleep(3)
# 팀별 이미지
team_img = driver.find_elements_by_xpath("//div/div/div[@class='team__list']/img")
detail_team_img = [url.get_attribute("src") for url in team_img]

