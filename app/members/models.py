from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.files import File
from django.db import models
import datetime


def team_path(instance, filename):
    a = f'{instance.name}/{instance.name}.svg'
    return a


def player_path(instance, filename):
    a = f'{instance.team.name}/{instance.name}.png'
    return a


def post_path(instance, filename):
    a = f'{instance.name}/{instance.name}.png'
    return a


class Team(models.Model):
    name = models.CharField(verbose_name='팀 이름', max_length=100)
    team_image = models.ImageField(upload_to=team_path, verbose_name='팀 사진', blank=True, null=True, default=True)

    class Meta:
        verbose_name = 'NBA 팀'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        return self.name

    @staticmethod
    def crawler():

        from selenium import webdriver
        import time
        import urllib.request
        import os
        from members.models import Team

        driver = webdriver.Chrome('/Users/mac/projects/ChromeWebDriver/chromedriver')

        driver.implicitly_wait(3)

        driver.get('http://www.nba.com/teams/')
        time.sleep(3)

        team_url_list = driver.find_elements_by_xpath("//div/div/div[@class='team__list']/a")
        team_name = [url.get_attribute("innerText") for url in team_url_list]
        team_img_urls = driver.find_elements_by_xpath("//div/div/div[@class='team__list']/img")
        team_img_url = [url.get_attribute("src") for url in team_img_urls]

        for url, name in zip(team_img_url, team_name):

            try:
                # Create target Directory
                os.mkdir(f'static/{name}')

                urllib.request.urlretrieve(url, f'static/{name}/{name}.svg')
                f = open(os.path.join(settings.BASE_DIR, f'static/{name}/{name}.svg'), 'rb')

                team = Team.objects.create(
                    name=name,
                    team_image=File(f),

                )
                print("Directory ", name, " Created ")
                f.close()

            except FileExistsError:
                print("already exists ", name)

        driver.close()


class Player(models.Model):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
    )

    # 선수 스탯
    playin_time = models.CharField(verbose_name='출장 시간', max_length=100)
    FGP = models.CharField(verbose_name='야투 성공률', max_length=50)
    T3PP = models.CharField(verbose_name='3점 야투 성공률', max_length=50)
    FTP = models.CharField(verbose_name='자유투 성공률', max_length=50)
    PPG = models.CharField(verbose_name='게임 평균 득점', max_length=50)
    RPG = models.CharField(verbose_name='게임 평균 리바운드', max_length=50)
    APG = models.CharField(verbose_name='게임 평균 어시스트', max_length=50)
    BPG = models.CharField(verbose_name='게임 평균 블락', max_length=50)

    # 선수 프로필
    name = models.CharField('풀네임', max_length=100)
    back_number = models.CharField(verbose_name='선수 등 번호', max_length=100)
    position = models.CharField(verbose_name='선수 포지션', max_length=5)
    first_name = models.CharField(verbose_name='선수 이름', max_length=50)
    last_name = models.CharField(verbose_name='선수 성씨', max_length=50)
    height = models.CharField(verbose_name='선수 키', max_length=100)
    weight = models.CharField(verbose_name='선수 무게', max_length=100)
    born = models.CharField(verbose_name='선수 생년월일', max_length=50)
    hometown = models.CharField(verbose_name='선수 고향', max_length=50)
    nba_debut = models.CharField(verbose_name='데뷔 년도', max_length=50)
    image = models.ImageField(upload_to=player_path, verbose_name='선수 사진', blank=True, null=True, default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'NBA 선수'
        verbose_name_plural = f'{verbose_name} 목록'

    @staticmethod
    def crawler():
        from selenium import webdriver
        import time
        import urllib.request
        import os
        from members.models import Team, Player
        from django.core.exceptions import ObjectDoesNotExist
        import collections

        driver = webdriver.Chrome('/Users/mac/projects/ChromeWebDriver/chromedriver')

        driver.implicitly_wait(3)

        driver.get('http://www.nba.com/teams/')
        time.sleep(3)

        ### 각 팀별 url 페이지
        team_url_list = driver.find_elements_by_xpath("//div/div/div[@class='team__list']/a")
        detail_urls = [url.get_attribute("href") for url in team_url_list]

        try:
            Teams = Team.objects.get(pk=1)
            Teams = Team.objects.all()
        except ObjectDoesNotExist:
            Teams = Team
            Teams.crawler()
            Teams = Team.objects.all()

        for index, url in enumerate(detail_urls):
            # 팀별 url 접근
            driver.get(url)
            time.sleep(2)

            # 선수들 url 추출
            all_players_urls = driver.find_elements_by_class_name("nba-player-index__trending-item")
            player_url_a_tags = [url.find_elements_by_tag_name('a') for url in all_players_urls]
            player_url = [url[0].get_attribute("href") for url in player_url_a_tags]

            variable = collections.namedtuple('variable', ['MPG', 'FGP', 'T3PP', 'FTP', 'PPG', 'RPG', 'APG', 'BPG',
                                                           'back_number', 'position', 'first_name', 'last_name',
                                                           'height', 'weight', 'born', 'hometown', 'nba_debut',
                                                           'name',
                                                           ])
            # 선수별 url 접근

            for url in player_url:
                driver.get(url)
                time.sleep(2)

                player_img_url_section = driver.find_elements_by_xpath(
                    '//*[@id="block-league-content"]/player-detail/section[1]/header/section[1]/img')
                player_img_src = player_img_url_section[0].get_attribute("src")
                season_stat_tbody = driver.find_elements_by_xpath(
                    '//*[@id="block-league-content"]/player-detail/player-snapshot-career/section/table/tbody')
                tr_data = season_stat_tbody[0].find_elements_by_tag_name('tr')
                tr_data[0].find_elements_by_tag_name('td')

                player_stats = [url.get_attribute("innerText") for url in
                                tr_data[0].find_elements_by_tag_name('td')]
                # NamedTuple
                variable.MPG = player_stats[0]
                variable.FGP = player_stats[1]
                variable.T3PP = player_stats[2]
                variable.FTP = player_stats[3]
                variable.PPG = player_stats[4]
                variable.RPG = player_stats[5]
                variable.APG = player_stats[6]
                variable.BPG = player_stats[7]

                variable.back_number = driver.find_element_by_xpath(
                    '//*[@id="block-league-content"]/player-detail/section[1]/header/section[2]/p/span[1]').get_attribute(
                    "innerText")[1:]
                variable.position = driver.find_element_by_xpath(
                    '//*[@id="block-league-content"]/player-detail/section[1]/header/section[2]/p/span[3]').get_attribute(
                    'innerText')
                variable.first_name = driver.find_element_by_xpath(
                    '//*[@id="block-league-content"]/player-detail/section[1]/header/section[2]/section/p[1]').get_attribute(
                    'innerText')
                variable.last_name = driver.find_element_by_xpath(
                    '//*[@id="block-league-content"]/player-detail/section[1]/header/section[2]/section/p[2]').get_attribute(
                    'innerText')
                variable.height = driver.find_element_by_xpath(
                    '//*[@id="player-tabs-Info"]/section/section[1]/section[1]/section[1]/p[3]').get_attribute(
                    'innerText')[2:]
                variable.weight = driver.find_element_by_xpath(
                    '//*[@id="player-tabs-Info"]/section/section[1]/section[1]/section[2]/p[3]').get_attribute(
                    'innerText')[2:]
                variable.born = driver.find_element_by_xpath(
                    '//*[@id="player-tabs-Info"]/section/section[1]/section[2]/ul/li[1]/span[2]').get_attribute(
                    'innerText')
                variable.hometown = driver.find_element_by_xpath(
                    '//*[@id="player-tabs-Info"]/section/section[1]/section[2]/ul/li[3]/span[2]').get_attribute(
                    'innerText')
                variable.nba_debut = driver.find_element_by_xpath(
                    '//*[@id="player-tabs-Info"]/section/section[1]/section[2]/ul/li[4]/span[2]').get_attribute(
                    'innerText')
                variable.name = variable.first_name + variable.last_name

                try:
                    player_path = variable.back_number + " " + variable.first_name + " " + variable.last_name
                    urllib.request.urlretrieve(player_img_src, f'static/{Teams[index].name}/{player_path}.png')

                    f = open(os.path.join(settings.BASE_DIR, f'static/{Teams[index].name}/{player_path}.png'), 'rb')
                    obj = Player.objects.get(name=f'{variable.name}')
                    # player_path, is_boolean = Player.objects.get_or_create(
                    # MPG 를 pycharm 에서 playin_time으로 작성함
                except Player.DoesNotExist:
                    obj = Player.objects.create(
                        name=variable.name,
                        team=Teams[index],

                        playin_time=variable.MPG,
                        FGP=variable.FGP,
                        T3PP=variable.T3PP,
                        FTP=variable.FTP,
                        PPG=variable.PPG,
                        RPG=variable.RPG,
                        APG=variable.APG,
                        BPG=variable.BPG,

                        back_number=variable.back_number,
                        position=variable.position,
                        first_name=variable.first_name,
                        last_name=variable.last_name,
                        height=variable.height,
                        weight=variable.weight,
                        born=variable.born,
                        hometown=variable.hometown,
                        nba_debut=variable.nba_debut,
                        image=File(f),
                    )
                    f.close()
                    print(player_path, " Created ===========", Teams[index])
                except FileExistsError:
                    print("already exists ", player_path)
                    pass
                except IndexError:
                    print(player_path, "인덱스 에러 발생")
                    pass

    def call_by_crawler(player_model, requset, queryset):
        Player.crawler()

    call_by_crawler.short_description = "선수 버튼 실행"
