import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


def test_setup():
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    driver.implicitly_wait(10)


def test_login_successfully():
    # login
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    driver.implicitly_wait(10)
    username = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
    password = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
    login = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
    time.sleep(2)
    driver.find_element_by_xpath(username).send_keys("Admin")
    time.sleep(2)
    driver.find_element_by_xpath(password).send_keys("admin123")
    time.sleep(2)
    driver.find_element_by_xpath(login).click()

    # myinfo
    myinfo_btn = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span"
    firstname_path = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input"
    lastname_path = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input"
    time.sleep(2)
    driver.find_element_by_xpath(myinfo_btn).click()
    time.sleep(2)
    driver.find_element_by_xpath(firstname_path).send_keys("nihad")
    time.sleep(2)
    driver.find_element_by_xpath(lastname_path).send_keys("ferdousi")

    # admin
    admin_path = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span"
    add_path = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button"
    admin_user_role_dropdown_path = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div"
    time.sleep(2)
    driver.find_element_by_xpath(admin_path).click()
    time.sleep(2)
    driver.find_element_by_xpath(add_path).click()
    time.sleep(2)
    driver.find_element_by_xpath(admin_user_role_dropdown_path).click()

    # leave
    leave_btn = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a"
    more_path = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span"
    assign_leave_icon = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[7]/a"
    leave_type_select_path = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div"
    time.sleep(2)
    driver.find_element_by_xpath(leave_btn).click()
    time.sleep(2)
    driver.find_element_by_xpath(more_path).click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/div/li/a").click()
    #driver.find_element_by_xpath(assign_leave_icon).click()
    #time.sleep(2)
    driver.find_element_by_xpath(leave_type_select_path).click()

    # performance
    performance_icon = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span"
    my_trackers_path = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a"
    employee_trackers_path = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[4]/a"
    time.sleep(2)
    driver.find_element_by_xpath(performance_icon).click()
    time.sleep(2)
    driver.find_element_by_xpath(my_trackers_path).click()
    time.sleep(2)
    driver.find_element_by_xpath(employee_trackers_path).click()
    time.sleep(2)
    expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/performance/viewEmployeePerformanceTrackerList"
    actual_url = driver.current_url
    assert expected_url == actual_url
    print(driver.current_url)
    driver.save_screenshot("image.png")
    title = driver.title
    assert title == "OrangeHRM"


def test_logout_successfully():
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    driver.implicitly_wait(1000)
    username = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
    password = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
    login = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
    paul = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p"
    logout = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a"
    driver.find_element_by_xpath(username).send_keys("Admin")
    driver.find_element_by_xpath(password).send_keys("admin123")
    driver.find_element_by_xpath(login).click()
    driver.find_element_by_xpath(paul).click()
    driver.find_element_by_xpath(logout).click()


def test_user_should_not_login_with_invalid_credential():
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    driver.implicitly_wait(1000)
    username = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
    password = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
    login = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
    invalid_message = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p"
    driver.find_element_by_xpath(username).send_keys("abc")
    driver.find_element_by_xpath(password).send_keys("admin12345")
    driver.find_element_by_xpath(login).click()
    error_message = driver.find_element_by_xpath(invalid_message).text
    assert "Invalid credentials" in error_message


def test_closebrowser():
    driver.close()
    driver.quit()
