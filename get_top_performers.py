from espn_api.basketball import League
import requests
import datetime
import os


GroupMe_URL = 'https://api.groupme.com/v3/bots/post'

league = League(league_id=197496, year=2023, espn_s2=os.environ['espn_s2'], swid=os.environ['SWID'])
week = (league.currentMatchupPeriod - 1)
box = league.box_scores(matchup_period=week, scoring_period=week, matchup_total=True)


class LaLigaPerformersBot:
    def __init__(self):
        self.away_stat = None
        self.home_stat = None
        self.home_team = None
        self.away_team = None
        self.counting_stat_categories = {'PTS': {}, 'BLK': {}, 'STL': {}, 'AST': {}, 'REB': {}, 'TO': {}, 'FGM': {},
                                         'FGA': {}, 'FTM': {}, 'FTA': {}, '3PTM': {}, 'FG%': {}, 'FT%': {}}
        self.pct_stat_categories = {'FG%': {}, 'FT%': {}}
        self.top_performer_categories = ['PTS', 'FG%', 'FT%', '3PTM', 'REB', 'AST', 'STL', 'BLK', 'TO']
        self.master_cat_dict = dict()
        self.bot_id = os.environ['bot_id']

    def assign_home_vars(self, matchup, stat):
        self.home_team = str(box[matchup].home_team).replace('Team(', '').replace(')', '')
        self.home_stat = float(box[matchup].home_stats[stat]['value'])

    def assign_away_vars(self, matchup, stat):
        self.away_team = str(box[matchup].away_team).replace('Team(', '').replace(')', '')
        self.away_stat = float(box[matchup].away_stats[stat]['value'])

    def create_master_dict(self):
        for matchup in range(5):
            for stat in self.counting_stat_categories.keys():  # counting stats
                # home team formatting + dict update
                self.assign_home_vars(matchup=matchup, stat=stat)
                self.counting_stat_categories[stat][self.home_team] = int(format(self.home_stat, '.0f'))

                # away team formatting + dict update
                self.assign_away_vars(matchup=matchup, stat=stat)
                self.counting_stat_categories[stat][self.away_team] = int(format(self.away_stat, '.0f'))
            self.master_cat_dict.update(self.counting_stat_categories)

            for stat in self.pct_stat_categories.keys():  # percentage stats
                # home team formatting + dict update
                self.assign_home_vars(matchup=matchup, stat=stat)
                self.pct_stat_categories[stat][self.home_team] = round(self.home_stat * 100, 3)

                # away team formatting + dict update
                self.assign_away_vars(matchup=matchup, stat=stat)
                self.pct_stat_categories[stat][self.away_team] = round(self.away_stat * 100, 3)
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


# performers_bot = LaLigaPerformersBot()
# performers_bot.create_master_dict()
# performers_bot.post_top_performers()
