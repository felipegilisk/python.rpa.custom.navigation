"""
Funções criadas para o projeto
"""
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import os, time
from funcs import urls


def start_chrome():
    browser = Chrome()
    browser.maximize_window()
    return browser


def acme_login(browser: Chrome):
    browser.get(urls.ACME_HOME)
    time.sleep(2)

    browser.execute_script(f"document.querySelector('#email').value = '{os.environ.get('ACME_USERNAME')}'")
    time.sleep(1)
    browser.execute_script(f"document.querySelector('#password').value = '{os.environ.get('ACME_PWORD')}'")
    time.sleep(2)

    browser.execute_script("document.querySelector('body > div > div.main-container > div > div > div > form > button').click()")


def acme_logout(browser: Chrome):
    browser.get(urls.ACME_LOGOUT)


def acme_get_work_items_data(browser: Chrome):
    page = 1
    browser.get(urls.ACME_WORK_ITEMS_PATTERN + str(page))
    time.sleep(2)
    collected_data = []
    data_headers = [ i.text for i in browser.find_elements(By.CSS_SELECTOR, 'body > div > div.main-container > div > table > tbody > tr:nth-child(1) > th')]
    while "Oooops" not in browser.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/p').text:
        html_table_rows = browser.find_elements(By.CSS_SELECTOR, 'body > div > div.main-container > div > table > tbody > tr')
        for i, row in enumerate(html_table_rows):
            if i > 0:
                print(row.text)
                for column in row.find_elements(By.CSS_SELECTOR('td')):
                    collected_data += column.text
        page += 1
        browser.get(urls.ACME_WORK_ITEMS_PATTERN + str(page))
        time.sleep(2)
    
    return data_headers + collected_data

