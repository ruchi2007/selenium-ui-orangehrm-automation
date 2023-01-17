class AdminPage:
    def __init__(self,driver):
        self.driver = driver
        self.admin_btn = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span"
        self.add_btn = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button"
        self.admin_user_role_dropdown_icon = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div"

    def click_admin_btn(self):
        self.driver.find_element_by_xpath(self.admin_btn).click()
        self.driver.find_element_by_xpath(self.add_btn).click()
        self.driver.find_element_by_xpath(self.admin_user_role_dropdown_icon).click()

