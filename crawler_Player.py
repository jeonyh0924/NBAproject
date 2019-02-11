for url, team_name in zip(detail_urls, team_name):
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
