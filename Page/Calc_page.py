import io
from Calculator.Calculator_app import calcapp
from pytesseract import image_to_string
from PIL import Image
from selenium import webdriver


class Calc_page():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Calc_page()
        return cls.instance



    def __init__(self):
        self.driver = calcapp.get_driver()
        self.driver.set_window_size(1400, 1000)


    def check_result(self, expected_result):
        element = self.driver.find_element_by_id("fullframe")
        image = element.screenshot_as_png
        imageStream = io.BytesIO(image)
        im = Image.open(imageStream)
        # im.save("screenshot.png")

        #location = element.location

        x = 600
        y = 40
        width = 330
        height = 50
        left = x
        top = y
        right = x + width
        bottom = y + height


        im = im.crop((left, top, right, bottom)) # defines crop points
        im.save("screenshot.png")
        assert image_to_string(im, config="--psm 6") == expected_result

calcpage = Calc_page.get_instance()