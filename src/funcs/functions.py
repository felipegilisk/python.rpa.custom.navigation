"""
Funções criadas para o projeto
"""
import os
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import xlsxwriter
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
    data_headers = [[ i.text for i in browser.find_elements(By.CSS_SELECTOR, 'body > div > div.main-container > div > table > tbody > tr:nth-child(1) > th')]]
    while "Oooops" not in browser.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/p').text:
        html_table_rows = browser.find_elements(By.CSS_SELECTOR, 'body > div > div.main-container > div > table > tbody > tr')
        for i, row in enumerate(html_table_rows):
            if i > 0:
                collected_data += [[column.text for column in row.find_elements(By.TAG_NAME, 'td')]]
        page += 1
        browser.get(urls.ACME_WORK_ITEMS_PATTERN + str(page))
        time.sleep(2)
    
    return data_headers + collected_data


def data_to_excel(data: list, file_name: str):
    data_count = dict()
    wb = xlsxwriter.Workbook(file_name)
    sheet1 = wb.add_worksheet('Work Items')
    for index_row, row in enumerate(data):
        for index_col, col in enumerate(row):
            sheet1.write(index_row, index_col, col)
            if index_col == 3 and index_row > 0:
                if col in data_count:
                    data_count[col] += 1
                else:
                    data_count[col] = 1

    wb.close()

    return data_count
