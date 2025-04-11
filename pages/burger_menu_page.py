from locators.burger_menu import BurgerMenuLocators

class BurgerMenuPage:
    def __init__(self, driver):
        self.driver = driver

    def click_burger_menu(self):
        self.driver.find_element("xpath", BurgerMenuLocators.BURGER_ICON).click()

