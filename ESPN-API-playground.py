from espn_api.basketball import League
import pandas as pd

USERNAME = "Sanders.NicholasR@gmail.com"
PWD = "BuzzBuzz51"
SSID = "Ap4asI7NVAw5JRc4R"
SWID = "{8EBA6C75-F4B8-47E5-84BB-EDC7933D8FD3}"
espn_s2 = "AEAeqLSqglhFPZ%2BxmMdDtoMpFNOlBGu6u59hx07Cs8CaPQK5CRRy0Ot1b" \
          "%2F8sSJEU3sFRZfbomZ16Npq1J5A8hNPVpOuFWncRswUtjsfih2BySK0IFnjpD9CxoQ7xlYTd8oijq9prIpzajQbVfZxSIpy1" \
          "%2FkBh7PxVK7LiM5Jd9JgK%2FXc38lIGG3uF2riAJjCHjPbrt8wCgptauZgS2HjechnYMi7gyxGj7oAqKo2fv02Zo7ljm4" \
          "%2F1NhwScdIAPYrU%2Bk19fW%2Bv3R51HTDXiTqzkcqhFO6nPJAzVHEzdUGZfI27lg%3D%3D "

stats_list = ['FG%', 'FT%', '3PTM', 'REB', 'AST', 'STL', 'BLK', 'TO', 'PTS']
league = League(league_id=197496, year=2023, espn_s2=espn_s2, swid=SWID)

cum_season_stats_dict = dict()

for matchup_num in range(1, league.currentMatchupPeriod):
    # print(f'Now starting matchup # {matchup_num} scrape')
    box = league.box_scores(matchup_period=matchup_num, scoring_period=matchup_num, matchup_total=True)
    weekly_stats_dict = dict()
    temp_weekly_dict = dict()
    temp_dict = dict()
    for stat in stats_list:
        cat_stats_dict = dict()
        cat_stats_dict.update({(str(box[_].home_team).replace('Team(', '')).replace(')', ''): box[_].home_stats[stat]['value'] for _ in range(5)})
        cat_stats_dict.update({(str(box[_].away_team).replace('Team(', '')).replace(')', ''): box[_].away_stats[stat]['value'] for _ in range(5)})
        # print(f'This is the cat_stats_dict @ line34: {cat_stats_dict}')
        # cat_stats_dict = {stat: cat_stats_dict for stat in stats_list}

        temp_dict = {stat: cat_stats_dict}
        # print(f'This is the temp_dict @ line38: {temp_dict}')
        # temp_dict = {matchup_num: weekly_stats_dict}
        # print(weekly_stats)
        weekly_stats_dict.update(temp_dict)
    #     print(f'Weekly stats_dict update line 45: {weekly_stats_dict}')
    # print(f'I just finished iteration #{matchup_num} of acquiring matchup stats')
    # print('-------------------------')
    # print(weekly_stats_dict)
    # print('-------------------------')
    # temp_weekly_dict = {matchup_num: weekly_stats_dict}
    temp_weekly_dict = {matchup_num: weekly_stats_dict}
    # print(f'This is the temp_weekly_dict on iteration number {matchup_num}: \n'
    #       f'-----------------------------------\n'
    #       f'{temp_weekly_dict}')
    cum_season_stats_dict = cum_season_stats_dict | temp_weekly_dict
    # cum_season_stats_dict = {cum_season_stats_dict: temp_weekly_dict}
    # print(f'I just finished iteration #{matchup_num} of updating cum_season_stats\n'
    #       f'------------------------\n'
    #       f'{cum_season_stats_dict}')
    # print('-------------------------')

# print(cum_season_stats_dict)

la_liga_data = pd.DataFrame.from_dict(cum_season_stats_dict)

# print(type(la_liga_data))
# print(la_liga_data.columns)
print(la_liga_data[1]['FG%']['Silky Soo'])
