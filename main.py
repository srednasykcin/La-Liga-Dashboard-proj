from espn_api.basketball import League
from _datetime import datetime
import requests

USERNAME = "Sanders.NicholasR@gmail.com"
PWD = "BuzzBuzz51"
SSID = "Ap4asI7NVAw5JRc4R"
SWID = "{8EBA6C75-F4B8-47E5-84BB-EDC7933D8FD3}"
espn_s2 = "AEAeqLSqglhFPZ%2BxmMdDtoMpFNOlBGu6u59hx07Cs8CaPQK5CRRy0Ot1b" \
          "%2F8sSJEU3sFRZfbomZ16Npq1J5A8hNPVpOuFWncRswUtjsfih2BySK0IFnjpD9CxoQ7xlYTd8oijq9prIpzajQbVfZxSIpy1" \
          "%2FkBh7PxVK7LiM5Jd9JgK%2FXc38lIGG3uF2riAJjCHjPbrt8wCgptauZgS2HjechnYMi7gyxGj7oAqKo2fv02Zo7ljm4" \
          "%2F1NhwScdIAPYrU%2Bk19fW%2Bv3R51HTDXiTqzkcqhFO6nPJAzVHEzdUGZfI27lg%3D%3D "

league = League(league_id=197496, year=2023, espn_s2=espn_s2, swid=SWID)
GroupMe_URL = 'https://api.groupme.com/v3/bots/post'

now = datetime.now().date()

# if str(now) == '2022-11-17':
#     week = 4
# elif str(now) == '2022-11-21':
#     week = 5
# elif str(now) == '2022-11-28':
#     week = 6
# elif str(now) == '2022-12-05':
#     week = 7
# elif str(now) == '2022-12-12':
#     week = 8
# elif str(now) == '2022-12-19':
#     week = 9
# elif str(now) == '2022-12-26':
#     week = 10
# elif str(now) == '2023-01-02':
#     week = 11
# elif str(now) == '2023-01-09':
#     week = 12
# elif str(now) == '2023-01-16':
#     week = 13
# elif str(now) == '2023-01-23':
#     week = 14
# elif str(now) == '2023-01-30':
#     week = 15
# elif str(now) == '2023-02-06':
#     week = 16
# elif str(now) == '2023-02-13':
#     week = 17
# elif str(now) == '2023-02-27':
#     week = 18
# elif str(now) == '2023-03-06':
#     week = 19
# elif str(now) == '2023-03-13':
#     week = 20
# elif str(now) == '2023-03-20':
#     week = 21
# elif str(now) == '2023-03-27':
#     week = 22

week = 3
box = league.box_scores(matchup_period=week, scoring_period=week, matchup_total=True)
max_PTS = 0
max_FG = -6
max_FT = -6
max_3PM = 0
max_REB = 0
max_AST = 0
max_STL = 0
max_BLK = 0
max_TOS = 1000

for _ in range(5):
    # PTS
    current_home_PTS = box[_].home_stats['PTS']['value']
    if current_home_PTS > max_PTS:
        max_PTS = current_home_PTS
        PTS_leader = box[_].home_team

    current_away_PTS = box[_].away_stats['PTS']['value']
    if current_away_PTS > max_PTS:
        max_PTS = current_away_PTS
        PTS_leader = box[_].away_team
    PTS_leader = (str(PTS_leader).replace('Team(', '')).replace(')', '')


    # FG%
    current_home_FG = box[_].home_stats['FG%']['value']
    if current_home_FG > max_FG:
        max_FG = current_home_FG
        FG_leader = box[_].home_team

    current_away_FG = box[_].away_stats['FG%']['value']
    if current_away_FG > max_FG:
        max_FG = current_away_FG
        FG_leader = box[_].away_team
    FG_leader = (str(FG_leader).replace('Team(', '')).replace(')', '')


    # FT%
    current_home_FT = box[_].home_stats['FT%']['value']
    if current_home_FT > max_FT:
        max_FT = current_home_FT
        FT_leader = box[_].home_team

    current_away_FT = box[_].away_stats['FT%']['value']
    if current_away_FT > max_FT:
        max_FT = current_away_FT
        FT_leader = box[_].away_team
    FT_leader = (str(FT_leader).replace('Team(', '')).replace(')', '')


    # 3PM
    current_home_3PM = box[_].home_stats['3PTM']['value']
    if current_home_3PM > max_3PM:
        max_3PM = current_home_3PM
        TPM_leader = box[_].home_team

    current_away_3PM = box[_].away_stats['3PTM']['value']
    if current_away_3PM > max_3PM:
        max_3PM = current_away_3PM
        TPM_leader = box[_].away_team
    TPM_leader = (str(TPM_leader).replace('Team(', '')).replace(')', '')


    # REB
    current_home_REB = box[_].home_stats['REB']['value']
    if current_home_REB > max_REB:
        max_REB = current_home_REB
        REB_leader = box[_].home_team

    current_away_REB = box[_].away_stats['REB']['value']
    if current_away_REB > max_REB:
        max_REB = current_away_REB
        REB_leader = box[_].away_team
    REB_leader = (str(REB_leader).replace('Team(', '')).replace(')', '')


    # AST
    current_home_AST = box[_].home_stats['AST']['value']
    if current_home_AST > max_AST:
        max_AST = current_home_AST
        AST_leader = box[_].home_team

    current_away_AST = box[_].away_stats['AST']['value']
    if current_away_AST > max_AST:
        max_AST = current_away_AST
        AST_leader = box[_].away_team
    AST_leader = (str(AST_leader).replace('Team(', '')).replace(')', '')


    # STL
    current_home_STL = box[_].home_stats['STL']['value']
    if current_home_STL > max_STL:
        max_STL = current_home_STL
        STL_leader = box[_].home_team

    current_away_STL = box[_].away_stats['STL']['value']
    if current_away_STL > max_STL:
        max_STL = current_away_STL
        STL_leader = box[_].away_team
    STL_leader = (str(STL_leader).replace('Team(', '')).replace(')', '')


    # BLK
    current_home_BLK = box[_].home_stats['BLK']['value']
    if current_home_BLK > max_BLK:
        max_BLK = current_home_BLK
        BLK_leader = box[_].home_team

    current_away_BLK = box[_].away_stats['BLK']['value']
    if current_away_BLK > max_BLK:
        max_BLK = current_away_BLK
        BLK_leader = box[_].away_team
    BLK_leader = (str(BLK_leader).replace('Team(', '')).replace(')', '')


    # TOS
    current_home_TOS = box[_].home_stats['TO']['value']
    if current_home_TOS < max_TOS:
        max_TOS = current_home_TOS
        TOS_leader = box[_].home_team

    current_away_TOS = box[_].away_stats['TO']['value']
    if current_away_TOS < max_TOS:
        max_TOS = current_away_TOS
        TOS_leader = box[_].away_team
    TOS_leader = (str(TOS_leader).replace('Team(', '')).replace(')', '')


messages = [f'Happy hooping morning La Liga pals!\n' \
          f"BizBot here with last week's top performers!",

          f'{PTS_leader} scored the most with {int(max_PTS)} points\n\n' \
          f'{FG_leader} had the best FG% by shooting {round(max_FG*100,3)}% from the field\n\n' \
          f'{FT_leader} had the best FT% by shooting {round(max_FT*100,3)}% from the charity stripe\n\n' \
          f'{TPM_leader} had the most 3PM by draining {int(max_3PM)} 3-pointers\n\n' \
          f'{REB_leader} had the most gimme-thats by securing {int(max_REB)} rebounds\n\n' \
          f'{AST_leader} had the most here-ya-goes by providing {int(max_AST)} assists\n\n' \
          f'{STL_leader} had the most cookies by recording {int(max_STL)} steals\n\n' \
          f'{BLK_leader} had the most code-reds by posting {int(max_BLK)} blocks\n\n' \
          f'{TOS_leader} had the fewest oopsies by only committing {round(max_TOS)} turnovers',

            "That's all for today. Happy hooping and I'll see ya next Monday!"]

for message in messages:
  data = {
    'bot_id': '27c3313828b1950b0b7f833df2',
    'text': message
  }
  response = requests.post(url=GroupMe_URL, json=data)
  print(response.text)

