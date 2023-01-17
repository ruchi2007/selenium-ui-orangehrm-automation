class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.logout_icon = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p"
        self.logout_btn = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a"

    def click_logout_icon(self):
        self.driver.find_element_by_xpath(self.logout_icon).click()
        self.driver.find_element_by_xpath(self.logout_btn).click()
