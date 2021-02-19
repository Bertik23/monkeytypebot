from selenium import webdriver
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from selenium.webdriver.opera.options import Options

import random

import time

operaOptions = webdriver.ChromeOptions()
operaOptions.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    executable_path=OperaDriverManager().install(),
    options=operaOptions)

driver.get("https://monkeytype.com")
actions = ActionChains(driver)

WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.CLASS_NAME, "words")))


def makeDriverGlobal():
    global driver
    pass


run = input("Run? ") != "n"
time.sleep(2)
while run:
    wordsInput = driver.find_element_by_id("wordsInput")
    print(wordsInput)
    while True:
        try:
            for word in driver.find_elements_by_class_name("word"):
                if word.get_attribute("class") != "word active":
                    print(word.text, word.get_attribute("class"))
                    continue
                print(word.text)
                for letter in word.text+" ":
                    wordsInput.send_keys(letter)
                    time.sleep(0.02+random.random()*0.01)
        except Exception as e:
            print(e)
            break
    run = input("Run? ") != "n"
    time.sleep(2)
