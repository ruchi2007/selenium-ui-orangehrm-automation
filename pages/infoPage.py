class InfoPage:
    def __init__(self, driver):
        self.driver = driver
        self.myinfo_btn = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span"
        self.firstname_editbox = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input"
        self.lastname_editbox = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input"

    def click_myinfo_btn(self):
        self.driver.find_element_by_xpath(self.myinfo_btn).click()

    def enter_firstname(self, firstname):
        self.driver.find_element_by_xpath(self.firstname_editbox).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element_by_xpath(self.lastname_editbox).send_keys(lastname)
