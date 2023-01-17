import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_login_successfully(self):
        username = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
        password = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
        login = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
        self.driver.find_element_by_xpath(username).send_keys("Admin")
        self.driver.find_element_by_xpath(password).send_keys("admin123")
        self.driver.find_element_by_xpath(login).click()
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        actual_url = self.driver.current_url
        self.driver.save_screenshot("image.png")
        assert expected_url == actual_url
        print(self.driver.current_url)
        title = self.driver.title
        assert title == "OrangeHRM"
        print("\n tc1...........>success")

    def test_logout_successfully(self):
        # username = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
        # password = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
        # login = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
        paul = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p"
        logout = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a"
        # self.driver.find_element_by_xpath(username).send_keys("Admin")
        # self.driver.find_element_by_xpath(password).send_keys("admin123")
        # self.driver.find_element_by_xpath(login).click()
        self.driver.find_element_by_xpath(paul).click()
        self.driver.find_element_by_xpath(logout).click()
        print("\n tc2...........>success")

    def test_user_should_not_login_with_invalid_credential(self):
        username = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
        password = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
        login = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
        invalid_message = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p"
        self.driver.find_element_by_xpath(username).send_keys("abc")
        self.driver.find_element_by_xpath(password).send_keys("admin12345")
        self.driver.find_element_by_xpath(login).click()
        error_message = self.driver.find_element_by_xpath(invalid_message).text
        assert "Invalid credentials" in error_message
        print("\n tc3...........>success")

    # def test_close_browser(self):
    #     self.driver.close()
