# La-Liga-Dashboard-proj

Simple GroupMe bot called "BizBot" who utilizes the following APIs:
  1) GroupMe -- posts league standings and top performers on a weekly basis 
  2) espn_api.basketball -- collects data from the league to pass into GroupMe bot's message post

get_standings.py uses Selenium to login to ESPN and screenshot the league standings and saving as .png before uploading to GroupMe image service and eventually posting in group

get_top_performers.py pulls categorical statistics posted by teams in fantasy basketball league and stores them in a dictionary; GroupMe bot then posts messages of top performers in each category from last week's matchups

main.py runs depending on time of day, so as to not spam the group with too many messages all at once
