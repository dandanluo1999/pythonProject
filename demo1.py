from time import sleep

from selenium import webdriver

from selenium.webdriver.common.by import By


# with webdriver.Chrome() as driver:
#     driver = driver.get("https://baidu.com/")
class TestCase:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://trace2-sim.vbhledger.com/login/index")

    def aa(self):
        self.driver.find_element(By.NAME,'username').send_keys('18888888888')
        self.driver.find_element(By.NAME, 'password').send_keys('qaz123456')
        self.driver.find_element(By.CSS_SELECTOR,"#app > div > div.login-main > div.form > form > button > span").click()
        sleep(3)
        self.driver.quit()
if __name__ == '__main__':
    mytest=TestCase()
    mytest.aa()

print("hello")