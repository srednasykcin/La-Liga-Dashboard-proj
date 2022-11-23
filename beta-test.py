import requests

GroupMe_URL = 'https://api.groupme.com/v3/bots/post'



message = "Your butt is real explosive and prone to injury."

data = {
    'bot_id': 'a869b1af9f3d009ac92236703e',
    'text': message
  }
response = requests.post(url=GroupMe_URL, json=data)
print(response.text)



