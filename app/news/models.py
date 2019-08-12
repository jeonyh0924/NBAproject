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
        driver.close()
        # news anchor
        # news_title_list_name = driver.find_elements_by_xpath(
        #     '//*[@id="main-container"]/div/section[3]/div[1]/section/ul/li/a')
        # [url.get_attribute("href") for url in news_title_list_name]


class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
