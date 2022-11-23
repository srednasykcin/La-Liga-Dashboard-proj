import requests

GroupMe_URL = 'https://api.groupme.com/v3/bots/post'



messages = ['Hello world!', 'Poop test', 'BRUH']


for message in messages:
  data = {
    'bot_id': '27c3313828b1950b0b7f833df2',
    'text': message
  }
  response = requests.post(url=GroupMe_URL, json=data)
  print(response.text)


