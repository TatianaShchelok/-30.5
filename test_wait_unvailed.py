from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
base_url = 'https://petfriends.skillfactory.ru'


def test_petfriends(web_browser):
    """ Search some phrase in google and make a screenshot of the page. """
    webdriver = web_browser
    # Open PetFriends base page:
    webdriver.get(base_url)

    # Click on the New User Button
    btn_new_user = webdriver.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]")
    WebDriverWait(webdriver, 10).until(ec.element_to_be_clickable((By.XPATH,
                            "//button[@onclick=\"document.location='/new_user';\"]")))

    btn_new_user.click()
    # Ищем надпись "У меня уже есть аккаунт" и нажимаем на нее

    btn_exist_acc = webdriver.find_element(By.LINK_TEXT, u"У меня уже есть аккаунт")
    btn_exist_acc.click()
    # add email

    field_email = webdriver.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys("lms.skillfactory@ru")
    # add password

    field_pass = webdriver.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys("HDm@WEB95JtkFzu")
    # click submit button

    btn_submit = webdriver.find_element(By.XPATH, "//button[@type='submit']")
    btn_submit.click()

    WebDriverWait(webdriver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div/div/"
                                                                                 "div[2]/div[3]")))

    if webdriver.current_url == f'{base_url}/all_pets':
        # Make the screenshot of browser window:
        webdriver.save_screenshot('result_petfriends.png')
    else:
        raise Exception("login error")
