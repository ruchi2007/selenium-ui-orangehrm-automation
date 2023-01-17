class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_editbox = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
        self.password_editbox = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
        self.submit_btn = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
        self.invalid_error = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p"

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.username_editbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_editbox).send_keys(password)

    def click_submit_btn(self):
        self.driver.find_element_by_xpath(self.submit_btn).click()

    def error_text_message(self):
        return self.driver.find_element_by_xpath(self.invalid_error).text
