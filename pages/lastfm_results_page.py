from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LastfmResultPage(BasePage):
    ARTIST_LINK = (By.CLASS_NAME, "link-block-target")

    def press_artist_link(self):
        self.click(self.ARTIST_LINK)

    def press_link(self):
        return self.press_artist_link()