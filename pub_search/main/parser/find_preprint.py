from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    return driver

def find_preprint(driver, doi):
    driver.get("https://arxiv.org/")
    input_element = driver.find_element(By.CLASS_NAME, "search-block").find_element(By.CLASS_NAME, "control").\
        find_element(By.CLASS_NAME, "input")

    input_element.send_keys(doi)
    input_element.send_keys(Keys.ENTER)

    handler = driver.current_window_handle
    driver.switch_to.window(handler)

    try:free_version = driver.find_element(By.CLASS_NAME, "list-title").find_element(By.TAG_NAME, "span").\
        find_element(By.TAG_NAME, "a").get_attribute("href")
    except:
        free_version = "Препринт не найден"

    driver.close()

    return free_version
