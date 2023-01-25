from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@given('i go to login page')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome()
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.driver.implicitly_wait(10)


@when('i enter username "{user}"')
def step_impl(context, user):
    username = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
    context.driver.find_element_by_xpath(username).send_keys(user)


@when('i enter password "{pwd}"')
def step_impl(context, pwd):
    password = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
    context.driver.find_element_by_xpath(password).send_keys(pwd)


@when('i click on submit button')
def step_impl(context):
    submit_btn = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
    context.driver.find_element_by_xpath(submit_btn).click()


@then('i should login successfully to the dashboard page')
def step_impl(context):
    try:
        text = context.driver.find_element_by_xpath("//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]").text
    except:
        context.driver.close()
        assert False, "Test Failed!!!!"
    if text == "Dashboard":
        context.driver.close()
        assert True, "Test PASSED"