import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import random
import requests
import os

# Set location of webdriver
chrome_driver_path = Service(r'C:\Users\sande\OneDrive\Desktop\Apps n stuff\Chrome\chromedriver_win32\chromedriver')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


# Create Class to get standings
class LaLigaStandingsBot:
    def __init__(self):
        # Set bot_id, access token, GroupMe and image upload endpoints, image path, chrome driver, preamble list
        self.image_response = None
        self.bot_id = os.environ['bot_id']
        self.GROUPME_ACCESS_TOKEN = os.environ['GROUPME_ACCESS_TOKEN']
        self.ESPN_LOGIN = os.environ['ESPN_LOGIN']
        self.ESPN_PWD = os.environ['ESPN_PWD']
        self.GroupMe_URL = 'https://api.groupme.com/v3/bots/post'
        self.image_upload_url = 'https://image.groupme.com/pictures'
        self.image_path = 'la_liga_standings.png'
        self.driver = webdriver.Chrome(options=options, service=chrome_driver_path)
        self.standings_preamble_list = ["What's that? You want the latest standings?\n",
                                        "It's a bird! It's a plane! No! It's the La Liga Standings!\n",
                                        "Some of you might not like this update as much as others...\n",
                                        "Can I getta' Shibuya roll call?\n",
                                        "Umm, sir? This is a Wendy's.\n",
                                        "It's that time of week again fellas!\n",
                                        "Tight race eh?? Well, maybe not for everyone.\n"]

    def login(self):
        self.driver.get("https://fantasy.espn.com/basketball/league?leagueId=197496&seasonId=2023")
        time.sleep(1)
        self.driver.maximize_window()
        self.driver.switch_to.frame('disneyid-iframe')
        login = self.driver.find_element(by=By.XPATH,
                                         value='/html/body/div[1]/div/div/section/section/form/section/div[1]/div/label/span[2]/input')
        login.send_keys(self.ESPN_LOGIN)
        pwd = self.driver.find_element(by=By.XPATH,
                                       value='/html/body/div[1]/div/div/section/section/form/section/div[2]/div/label/span[2]/input')
        pwd.send_keys(self.ESPN_PWD, Keys.ENTER)
        time.sleep(4)

    def screenshot_standings(self):
        self.driver.switch_to.parent_frame()
        standings = self.driver.find_element(by=By.XPATH,
                                             value='/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[2]/div[3]/div[2]/div')
        self.driver.execute_script("arguments[0].scrollIntoView();", standings)
        self.driver.execute_script("window.scrollBy(0,-100)", "")
        time.sleep(1)
        standings.screenshot(f'la_liga_standings.png')

    # Get image from GroupMe's Image Service
    def get_image_url(self):
        # Open the image file and read its contents
        with open(self.image_path, 'rb') as image_file:
            image_data = image_file.read()

        # Create the payload for the image upload request
        image_payload = {
            'bot_id': self.bot_id,
            'access_token': self.GROUPME_ACCESS_TOKEN,
            'file': image_data,
        }

        # Send the image upload request
        self.image_response = requests.post(self.image_upload_url, files={'file': image_data}, data=image_payload)

        # Check the response status code
        if self.image_response.status_code == 200:
            print('Image uploaded successfully')
        else:
            print(f'Error uploading image: {self.image_response.status_code}')

    # Post img to group with BizBot
    def post_image(self):
        group_msg_payload = {
            'bot_id': self.bot_id,
            'text': f'{random.choice(self.standings_preamble_list)}\n',
            'attachments': [
                {
                    'type': 'image',
                    'url': self.image_response.json()['payload']['url']
                },
            ],
        }
        msg_post_response = requests.post(self.GroupMe_URL, json=group_msg_payload,
                                          params={'token': self.GROUPME_ACCESS_TOKEN})

        # Check the response status code
        if msg_post_response.status_code == 202:
            print('Message posted successfully')
        else:
            print(f'Error posting message: {msg_post_response.status_code} {msg_post_response.__dict__}')

# standings_bot = LaLigaStandingsBot()
# standings_bot.login()
# standings_bot.screenshot_standings()
# standings_bot.get_image_url()
# standings_bot.post_image()
