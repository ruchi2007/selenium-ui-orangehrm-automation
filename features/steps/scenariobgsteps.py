from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@given('i navigate to login page')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome()
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.driver.implicitly_wait(10)


@when('i enter username')
def step_impl(context):
    username = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
    context.driver.find_element_by_xpath(username).send_keys('Admin')


@when('i enter password')
def step_impl(context):
    password = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
    context.driver.find_element_by_xpath(password).send_keys('admin123')


@when('i click submit button')
def step_impl(context):
    submit_btn = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
    context.driver.find_element_by_xpath(submit_btn).click()


@then('i should login to the dashboard page')
def step_impl(context):
    text = context.driver.find_element_by_xpath("//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]").text
    assert text == "Dashboard"
    context.driver.close()


@then('i should see logo')
def step_impl(context):
    logo = context.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/aside/nav/div[1]/a/div[2]/img').is_displayed()
    assert logo is True

@when('i click on profile picture')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p").click()

@then('i should see logout')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a").is_displayed()