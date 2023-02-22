from espn_api.basketball import League
import requests
import datetime
import os

# SWID = os.environ['SWID']
# espn_s2 = os.environ['espn_s2']
GroupMe_URL = 'https://api.groupme.com/v3/bots/post'

league = League(league_id=197496, year=2023, espn_s2=os.environ['espn_s2'], swid=os.environ['SWID'])
week = (league.currentMatchupPeriod - 1)
box = league.box_scores(matchup_period=week, scoring_period=week, matchup_total=True)


class LaLigaPerformersBot:
    def __init__(self):
        self.counting_stat_categories = {'PTS': {}, 'BLK': {}, 'STL': {}, 'AST': {}, 'REB': {}, 'TO': {}, 'FGM': {},
                                         'FGA': {}, 'FTM': {}, 'FTA': {}, '3PTM': {}, 'FG%': {}, 'FT%': {}}
        self.pct_stat_categories = {'FG%': {}, 'FT%': {}}
        self.top_performer_categories = ['PTS', 'FG%', 'FT%', '3PTM', 'REB', 'AST', 'STL', 'BLK', 'TO']
        self.master_cat_dict = dict()
        self.bot_id = os.environ['bot_id']

    def create_master_dict(self):
        for matchup in range(5):
            for stat in self.counting_stat_categories.keys():  # counting stats
                # home team formatting and dict update
                home_team = str(box[matchup].home_team).replace('Team(', '').replace(')', '')
                home_stat = format(float(box[matchup].home_stats[stat]['value']), '.0f')
                self.counting_stat_categories[stat][home_team] = home_stat

                # away team formatting and dict update
                away_team = str(box[matchup].away_team).replace('Team(', '').replace(')', '')
                away_stat = format(float(box[matchup].away_stats[stat]['value']), '.0f')
                self.counting_stat_categories[stat][away_team] = away_stat
            self.master_cat_dict.update(self.counting_stat_categories)

            for stat in self.pct_stat_categories.keys():  # percentage stats
                # home team formatting and dict update
                home_team = str(box[matchup].home_team).replace('Team(', '').replace(')', '')
                home_stat = round(float(box[matchup].home_stats[stat]['value']) * 100, 3)
                self.pct_stat_categories[stat][home_team] = home_stat

                # away team formatting and dict update
                away_team = str(box[matchup].away_team).replace('Team(', '').replace(')', '')
                away_stat = round(float(box[matchup].away_stats[stat]['value']) * 100, 3)
                self.pct_stat_categories[stat][away_team] = away_stat
            self.master_cat_dict.update(self.pct_stat_categories)

    def post_top_performers(self):
        big_msg = ''
        messages = [f'Good morning La Liga!\n'
                    f"BizBot here with last week's top performers!",

                    "Happy hoopin' and I'll see ya next week!"]

        for stat in self.top_performer_categories:
            if '%' in stat:
                new_msg = f'{max(self.master_cat_dict[stat], key=self.master_cat_dict[stat].get)} recorded the best {stat} with {max(self.master_cat_dict[stat].values())}%\n'
                big_msg += new_msg
            elif stat != 'TO':
                new_msg = f'{max(self.master_cat_dict[stat], key=self.master_cat_dict[stat].get)} recorded the most {stat} with {max(self.master_cat_dict[stat].values())}\n'
                big_msg += new_msg
            else:
                new_msg = f'{min(self.master_cat_dict[stat], key=self.master_cat_dict[stat].get)} recorded the fewest {stat} with {min(self.master_cat_dict[stat].values())}\n'
                big_msg += new_msg

        messages.insert(1, big_msg)

        today = datetime.datetime.today()

        for message in messages:
            data = {
                'bot_id': self.bot_id,
                'text': message
            }
            response = requests.post(url=GroupMe_URL, json=data)
            print(response.text)
        print(messages)

# print(master_cat_dict)
