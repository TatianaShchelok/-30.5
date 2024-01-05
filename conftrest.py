from selenium import webdriver   # подключение библиотеки
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import uuid


@pytest.fixture()
def driver():
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window()
    yield driver
    driver.save_screenshot('result.png')
    driver.quit()


@pytest.fixture
def web_browser(request, driver):
    browser = driver
    browser.set_window_size(1400, 1000)  # Вернуть объект браузера
    yield browser
#  Этот код выполнится после отрабатывания теста:
    if request.node.rep_call.failed:
        try:  # Делаем скриншот, если тест провалится:
            browser.execute_script('document.body.bg.Color="white";')
        except:
            pass
#  Создаем папку screenshots и кладем туда скриншот с генерированным именем:
    browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')
#  Для дебагинга печатаем информацию в консоль
    print('URL:, browser_current_url')
    print('Browser logs:')
    for log in browser.get_log('browser'):
        print(log)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    # This function helps to detect that some test failed
    # and pass this information to teardown:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
