from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def init_session():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    # options.add_argument("--headless")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options, executable_path='main/parser/chromedriver.exe')

    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win64",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    return driver


def switch_window(driver):
    handler = driver.current_window_handle
    driver.switch_to.window(handler)

    return driver

def auth_elib(driver):
    input_login = driver.find_element(By.ID, "login")
    input_login.send_keys("KappaRoss")

    with open(f"E:/Study/Diploma/auth.txt", 'r') as f:
        password = f.readline()

    input_password = driver.find_element(By.ID, "password")
    input_password.send_keys(password)
    input_password.send_keys(Keys.ENTER)


def find_copy(driver, doi):
    driver.get("https://elibrary.ru/defaultx.asp?")
    time.sleep(1)
    input_element = driver.find_element(By.CLASS_NAME, "left-panel").find_element(By.CLASS_NAME,"formfr")\
        .find_element(By.ID,"ftext")
    input_element.send_keys(doi)
    input_element.send_keys(Keys.ENTER)

    time.sleep(1)

    switch_window(driver)

    try:
        article = driver.find_element(By.ID, "restab").find_element(By.TAG_NAME, "a").text
        driver.find_element(By.LINK_TEXT, article).click()
    except:
        driver.close()
        return "Копия не найдена"

    switch_window(driver)

    auth_elib(driver)

    time.sleep(1)

    copy = driver.find_element(By.CLASS_NAME, "right-panel").find_element(By.CLASS_NAME, "help").text
    driver.find_element(By.LINK_TEXT, copy).click()

    time.sleep(1)

    if copy == "":
        driver.close()
        return "Копия не найдена"
    else:
        handler = driver.window_handles[1]
        driver.switch_to.window(handler)

    try:
        copy = driver.find_element(By.ID, "panel").find_element(By.CLASS_NAME, "help").text
        driver.find_element(By.LINK_TEXT, copy).click()
    except:
        copy = driver.current_url
        driver.close()
        return copy

    handler = driver.window_handles[2]
    driver.switch_to.window(handler)

    copy = driver.current_url

    driver.close()

    return copy


# driver = init_session()
# print(find_copy(driver, "10.1088/0741-3335/48/10/004"))