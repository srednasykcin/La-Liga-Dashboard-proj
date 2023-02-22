import requests
import datetime

GroupMe_URL = 'https://api.groupme.com/v3/bots/post'

now = datetime.datetime.now()
today8am = now.replace(hour=8, minute=0, second=0, microsecond=0)
today11am = now.replace(hour=11, minute=0, second=0, microsecond=0)


today = datetime.datetime.today()

# print(datetime.datetime.now())

# if datetime.datetime.weekday(today) == 0 and today.strftime('%x') != '02/20/23':

if today8am < now < today11am:
    message = 'I am just here to give a late-season update on the La Liga rankings!'
    data = {
        'bot_id': 'BOT ID',
        'text': message
      }
    response = requests.post(url=GroupMe_URL, json=data)
print(response.text)

