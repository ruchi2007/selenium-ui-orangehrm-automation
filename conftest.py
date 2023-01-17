import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from utils import environment_url


@pytest.fixture(scope="class")
def setup(request):
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(environment_url.qa_url)
    driver.implicitly_wait(1000)
    request.cls.driver = driver

    yield
    driver.close()
