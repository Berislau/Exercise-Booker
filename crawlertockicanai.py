from selenium import webdriver
from selenium.webdriver.common.by import By

import utils
from utils import highlight
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class CrawlerTockicanai:

    def __init__(self):
        self.__base_url = "https://www.tockicanai.hr/raspored-tekuci-tjedan/"
        self.__driver = webdriver.Chrome()
        self.__driver.get(self.__base_url)

    def find_exercise(self, exercise_name):
        try:
            # exercise_hyperlink = self.__driver.find_element(By.XPATH, "//*[contains(text()," + exercise_name + " )]")
            # utils.highlight(exercise_hyperlink)
            # exercise_hyperlinks = WebDriverWait(self.__driver, 10).until(
            # EC.presence_of_all_elements_located((By.XPATH, "//*[contains(text()," + exercise_name + " )]")))
            sdasdas= 0
            exercise_hyperlink = self.__driver.find_element(By.ID, "mec_skin_events_4147")
            exercise_hyperlinks = exercise_hyperlink.find_elements(By.XPATH, "//*/div/div")

            for i in range(1,6):
                nesto = exercise_hyperlink.find_elements(By.XPATH, "//*/div/div/article["+i.__str__()+"]")
                for bla in nesto:
                    print(bla.text)
        finally:
            pass

        # for  hyperlinks in exercise_hyperlinks:
        #     print(hyperlinks.text)


    def book_exercise(self):
        pass
