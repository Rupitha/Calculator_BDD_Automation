#import time
from selenium import webdriver
#rom urllib.parse import urljoin
from selenium.webdriver.common.keys import Keys

class Calculator_app:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Calculator_app()
        return cls.instance

    def __init__(self):
       self.driver = webdriver.Chrome(executable_path="/home/rupz/Chrome/chromedriver")
        # if str(settings['browser']).lower() is "firefox":
        #     self.driver = webdriver.Firefox()
        # elif str(settings['browser']).lower() is "chrome":
        #     self.driver = webdriver.Chrome(executable_path="/home/rupz/Chrome/chromedriver")
        # else:
        #     self.driver = webdriver.Chrome(executable_path="/home/rupz/Chrome/chromedriver")

    def get_driver(self):
        return self.driver

    def load_website(self):
        self.driver.get("https://online-calculator.com/full-screen-calculator/")

    def do_math(self, math_op):
        element = self.driver.find_element_by_id("fullframe")
        element.send_keys(math_op)
        element.send_keys(Keys.ENTER)

    def close_driver(self):
        return self.driver.close()


calcapp = Calculator_app.get_instance()