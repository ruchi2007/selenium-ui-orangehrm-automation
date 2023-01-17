class PerformancePage:
    def __init__(self,driver):
        self.driver = driver
        self.performance_btn = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span"
        self.my_trackers_icon = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a"
        self.employee_trackers_icon = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[4]/a"

    def click_performance_btn(self):
        self.driver.find_element_by_xpath(self.performance_btn).click()
        self.driver.find_element_by_xpath(self.my_trackers_icon).click()
        self.driver.find_element_by_xpath(self.employee_trackers_icon).click()