from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

class allrecipessearch():

    def searchrecipe(self):

        SEARCHWORD = "Thin creast pizza"
        baseURL = "https://www.allrecipes.com/"
        XPATHFORRECIPE = "//div[@class= 'component card card__recipe card__facetedSearchResult']"

        chromedriver = r"C:\Users\Daily_use\Downloads\chromedriver_win32\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        driver = webdriver.Chrome(chromedriver)
        time.sleep(5);
        driver.get(baseURL)
        driver.maximize_window()

        # Verify if the right web page was opened
        try:
            assert "Allrecipes" in driver.title
            print("The title of the web page is correct")
        except Exception as e:
            print("Wrong page was opened")

            # Search for a recipe in the website

        searchForRecipe = driver.find_element(By.XPATH, ".//input[@id='search-block']")
        searchForRecipe.send_keys(SEARCHWORD)
        time.sleep(5)

        clickOnSearchButton = driver.find_element_by_css_selector(".button.searchButton")
        clickOnSearchButton.click()
        time.sleep(5)

        clickOnrecipe = driver.find_element_by_xpath(XPATHFORRECIPE)
        clickOnrecipe.click()

        time.sleep(5)
        driver.close()

ff=allrecipessearch()
ff.searchrecipe()