from selenium import webdriver
from time import sleep

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="")

    def openDatingApp(self):
        self.driver.get("https://tinder.com/en-GB")



bot = TinderBot()
bot.openDatingApp()