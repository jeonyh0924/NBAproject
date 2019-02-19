from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.files import File
from django.db import models


class User(AbstractUser):
    pass


def team_path(instance, filename):
    a = f'{instance.name}/{instance.name}.svg'
    return a


def player_path(instance, filename):
    a = f'{instance.team.name}/{instance.name}.png'
    return a


class Team(models.Model):
    name = models.CharField(verbose_name='팀 이름', max_length=100)
    team_image = models.ImageField(upload_to=team_path, verbose_name='팀 사진', blank=True, null=True, default=True)

    def __str__(self):
        return self.name


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

    @staticmethod
    def crawler():
        from selenium import webdriver
        import time
        from bs4 import BeautifulSoup
        import urllib.request
        import os
        from members.models import Team, Player

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

        for url, name in zip(team_img_url, team_name):
            dirName = name
            try:
                # Create target Directory
                os.mkdir(f'static/{dirName}')

                urllib.request.urlretrieve(url, f'static/{name}/{name}.svg')
                f = open(os.path.join(settings.BASE_DIR, f'static/{name}/{name}.svg'), 'rb')

                team = Team.objects.create(
                    name=name,
                    team_image=File(f),
                )
                print("Directory ", dirName, " Created ")
                f.close()

            except FileExistsError:
                print("already exists ", dirName)
                pass

        Teams = Team.objects.all()

        for index, url in enumerate(detail_urls):
            # 팀별 url 접근
            driver.get(url)
            time.sleep(2)

            # 선수들 url 추출
            all_players_urls = driver.find_elements_by_class_name("nba-player-index__trending-item")
            player_url_a_tags = [url.find_elements_by_tag_name('a') for url in all_players_urls]
            player_url = [url[0].get_attribute("href") for url in player_url_a_tags]

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

                player_stats = [url.get_attribute("innerText") for url in tr_data[0].find_elements_by_tag_name('td')]
                # NamedTuple
                MPG = player_stats[0]
                FGP = player_stats[1]
                T3PP = player_stats[2]
                FTP = player_stats[3]
                PPG = player_stats[4]
                RPG = player_stats[5]
                APG = player_stats[6]
                BPG = player_stats[7]

                back_number = driver.find_element_by_xpath(
                    '//*[@id="block-league-content"]/player-detail/section[1]/header/section[2]/p/span[1]').get_attribute(
                    "innerText")[1:]
                position = driver.find_element_by_xpath(
                    '//*[@id="block-league-content"]/player-detail/section[1]/header/section[2]/p/span[3]').get_attribute(
                    'innerText')
                first_name = driver.find_element_by_xpath(
                    '//*[@id="block-league-content"]/player-detail/section[1]/header/section[2]/section/p[1]').get_attribute(
                    'innerText')
                last_name = driver.find_element_by_xpath(
                    '//*[@id="block-league-content"]/player-detail/section[1]/header/section[2]/section/p[2]').get_attribute(
                    'innerText')
                height = driver.find_element_by_xpath(
                    '//*[@id="player-tabs-Info"]/section/section[1]/section[1]/section[1]/p[3]').get_attribute(
                    'innerText')[2:]
                weight = driver.find_element_by_xpath(
                    '//*[@id="player-tabs-Info"]/section/section[1]/section[1]/section[2]/p[3]').get_attribute(
                    'innerText')[2:]
                born = driver.find_element_by_xpath(
                    '//*[@id="player-tabs-Info"]/section/section[1]/section[2]/ul/li[1]/span[2]').get_attribute(
                    'innerText')
                hometown = driver.find_element_by_xpath(
                    '//*[@id="player-tabs-Info"]/section/section[1]/section[2]/ul/li[3]/span[2]').get_attribute(
                    'innerText')
                nba_debut = driver.find_element_by_xpath(
                    '//*[@id="player-tabs-Info"]/section/section[1]/section[2]/ul/li[4]/span[2]').get_attribute(
                    'innerText')
                name = first_name + last_name

                try:
                    player_path = back_number + " " + first_name + " " + last_name
                    urllib.request.urlretrieve(player_img_src, f'static/{Teams[index].name}/{player_path}.png')

                    f = open(os.path.join(settings.BASE_DIR, f'static/{Teams[index].name}/{player_path}.png'), 'rb')

                    player_path = Player.objects.create(
                        # MPG 를 pycharm 에서 playin_time으로 작성함
                        name=name,
                        team=Teams[index],
                        playin_time=MPG,
                        FGP=FGP,
                        T3PP=T3PP,
                        FTP=FTP,
                        PPG=PPG,
                        RPG=RPG,
                        APG=APG,
                        BPG=BPG,

                        back_number=back_number,
                        position=position,
                        first_name=first_name,
                        last_name=last_name,
                        height=height,
                        weight=weight,
                        born=born,
                        hometown=hometown,
                        nba_debut=nba_debut,
                        image=File(f),
                    )
                    f.close()
                    print(player_path, " Created ===========")

                except FileExistsError:
                    print("already exists ", player_path)
                    pass