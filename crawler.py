from selenium import webdriver
import time
from bs4 import BeautifulSoup
import urllib.request
import os
from members.models import Team , Player

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
        team = Team.objects.create(
            name=name,
            team_image=url,
        )

    except FileExistsError:
        print("already exists ", dirName)
        pass
    urllib.request.urlretrieve(url, f'static/{name}/{name}.svg')

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

        player_img_url_section = driver.find_elements_by_xpath('//*[@id="block-league-content"]/player-detail/section[1]/header/section[1]/img')
        player_img_src = player_img_url_section[0].get_attribute("src")
        season_stat_tbody= driver.find_elements_by_xpath('//*[@id="block-league-content"]/player-detail/player-snapshot-career/section/table/tbody')
        tr_data = season_stat_tbody[0].find_elements_by_tag_name('tr')
        tr_data[0].find_elements_by_tag_name('td')


        player_stats = [ url.get_attribute("innerText") for url in tr_data[0].find_elements_by_tag_name('td')]
        MPG = player_stats[0]
        FGP = player_stats[1]
        T3PP = player_stats[2]
        FTP = player_stats[3]
        PPG = player_stats[4]
        RPG = player_stats[5]
        APG = player_stats[6]
        BPG = player_stats[7]

        player_back_number = driver.find_element_by_xpath('//*[@id="block-league-content"]/player-detail/section[1]/header/section[2]/p/span[1]').get_attribute("innerText")[1:]
        player_position = driver.find_element_by_xpath('//*[@id="block-league-content"]/player-detail/section[1]/header/section[2]/p/span[3]').get_attribute('innerText')
        player_first_name = driver.find_element_by_xpath('//*[@id="block-league-content"]/player-detail/section[1]/header/section[2]/section/p[1]').get_attribute('innerText')
        player_last_name = driver.find_element_by_xpath('//*[@id="block-league-content"]/player-detail/section[1]/header/section[2]/section/p[2]').get_attribute('innerText')
        player_height = driver.find_element_by_xpath('//*[@id="player-tabs-Info"]/section/section[1]/section[1]/section[1]/p[3]').get_attribute('innerText')[2:]
        player_weight = driver.find_element_by_xpath('//*[@id="player-tabs-Info"]/section/section[1]/section[1]/section[2]/p[3]').get_attribute('innerText')[2:]
        player_born = driver.find_element_by_xpath('//*[@id="player-tabs-Info"]/section/section[1]/section[2]/ul/li[1]/span[2]').get_attribute('innerText')
        player_hometown = driver.find_element_by_xpath('//*[@id="player-tabs-Info"]/section/section[1]/section[2]/ul/li[3]/span[2]').get_attribute('innerText')
        player_nba_debut = driver.find_element_by_xpath('//*[@id="player-tabs-Info"]/section/section[1]/section[2]/ul/li[4]/span[2]').get_attribute('innerText')
        name = player_first_name + player_last_name

        try:
            player_path = player_back_number + " " + player_first_name + " " + player_last_name
            urllib.request.urlretrieve(player_img_src, f'static/{Teams[index].name}/{player_path}.png')

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

                player_back_number=player_back_number,
                player_position=player_position,
                player_first_name=player_first_name,
                player_last_name=player_last_name,
                player_height=player_height,
                player_weight=player_weight,
                player_born=player_born,
                player_hometown=player_hometown,
                player_nba_debut=player_nba_debut,
                player_image=player_img_src,
            )
            print(player_path, " Created ===========")

        except FileExistsError:
            print("already exists ", player_path)
            pass
