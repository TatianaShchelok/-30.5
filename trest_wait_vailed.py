import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def web_driver():
    web_driver = webdriver.Chrome()
    # Переходим на страницу авторизации
    web_driver.get('https://petfriends.skillfactory.ru/login')
    yield web_driver

    web_driver.quit()


def test_all_cards_of_pets(web_driver):
    # Вводим email
    web_driver.find_element(By.ID, 'email').send_keys('lms.skillfactory@ru')
    # Вводим пароль
    web_driver.find_element(By.ID, 'pass').send_keys('HDm@WEB95JtkFzu')
    # Нажимаем на кнопку входа в аккаунт
    web_driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert web_driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    # Нажимаем кнопку "Мои питомцы"
    web_driver.find_element(By.CSS_SELECTOR, 'div#navbarNav > ul > li > a').click()
    # Проверяем, что мы оказались на странице пользователя:
    assert (web_driver.find_element(By.CSS_SELECTOR, 'div#navbarNav > ul > li > a').text ==
            "Мои питомцы")
    web_driver.implicitly_wait(3)
    images = web_driver.find_elements(By.TAG_NAME, 'img.marked-element')
    web_driver.implicitly_wait(3)
    names = web_driver.find_elements(By.TAG_NAME, 'td.marked-element')
    web_driver.implicitly_wait(3)
    ages = web_driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr.marked-element')
    species = web_driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr[0]/td[2]')

    for i in range(len(names)):
        name_text = names[i].text
        print(f'Name text: {name_text}')
        assert len(set(names[i].text)) == 4
    for i in range(len(images)):
        image_source = images[i].get_attribute('src')
        print(f"image source:{image_source}")
        assert len(image_source) > 2
    for i in range(len(ages)):
        age_text = ages[i].text
        print(f'age_text:{age_text}')
        assert len(ages[i].text) == 4
    for i in range(len(species)):
        specie_text = species[i].text
        print(f'Species text: {specie_text}')
        assert len(species[i].text) == 4
