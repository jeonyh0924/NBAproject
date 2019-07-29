from django.db import models


# Create your models here.
class newsHeadlines(models.Model):
    title = models.CharField('기사 명', max_length=50)

    @classmethod
    def crawler(cls):
        from selenium import webdriver
        from bs4 import BeautifulSoup
        import urllib.request as rq
        # django model import

        driver = webdriver.Chrome('/Users/mac/projects/ChromeWebDriver/chromedriver')
        driver.get('https://www.espn.com/nba/')

        news_title_list = driver.find_elements_by_xpath('//*[@id="main-container"]/div/section[3]/div[1]/section/ul/li')

        for url in news_title_list:
            news_title = url.get_attribute("innerText")
            newsHeadlines.objects.create(
                title=news_title,
            )
        # driver.close()
        # news anchor
        # news_title_list_name = driver.find_elements_by_xpath(
        #     '//*[@id="main-container"]/div/section[3]/div[1]/section/ul/li/a')
        # [url.get_attribute("href") for url in news_title_list_name]
