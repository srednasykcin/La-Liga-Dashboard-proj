import datetime
from get_standings import LaLigaStandingsBot
from get_top_performers import LaLigaPerformersBot


now = datetime.datetime.now()
today = datetime.datetime.today()
today8am = now.replace(hour=8, minute=0, second=0, microsecond=0)
today11am = now.replace(hour=11, minute=0, second=0, microsecond=0)


# If Monday before 8am...
if datetime.datetime.weekday(today) == 0 and now < today8am:
    standings_bot = LaLigaStandingsBot()
    standings_bot.login()
    standings_bot.screenshot_standings()
    standings_bot.get_image_url()
    standings_bot.post_image()

# If Monday before 11am, but AFTER 8am
if datetime.datetime.weekday(today) == 0 and today.strftime('%x') != '02/20/23' and today8am < now < today11am:
    performers_bot = LaLigaPerformersBot()
    performers_bot.create_master_dict()
    performers_bot.post_top_performers()
