class LeavePage:
    def __init__(self,driver):
        self.driver = driver
        self.leave_btn = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a"
        self.more_icon = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span"
        self.assign_leave_icon = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/div/li/a"
        self.leave_type_select_icon = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div"

    def click_leave_btn(self):
        self.driver.find_element_by_xpath(self.leave_btn).click()
        self.driver.find_element_by_xpath(self.more_icon).click()
        self.driver.find_element_by_xpath(self.assign_leave_icon).click()
        self.driver.find_element_by_xpath(self.leave_type_select_icon).click()
