from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ImdbMoviePage(BasePage):
    MOVIE_NAME = (By.CLASS_NAME, "hero__primary-text")
    MOVIE_RATING = (By.XPATH,"/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[2]/div[1]/div/div[1]/a/span/div/div[2]/div[1]/span[1]")

    def get_movie_name(self):
        return self.find_element(self.MOVIE_NAME).text
    
    def get_movie_rating(self):
        return self.find_element(self.MOVIE_RATING).text