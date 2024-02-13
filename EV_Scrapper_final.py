import pandas as pd
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pprint import pprint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def EV_Scrapper_function():
    project_dir = os.path.abspath(os.path.dirname(__file__))
    download_dir = os.path.join(project_dir, "downloads")
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    url = 'https://vahan.parivahan.gov.in/vahan4dashboard/vahan/vahan/view/reportview.xhtml'

    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("detach", True)

    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")  # Optional: Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,  # Disable download prompt
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(url)

    # ---- functions -------------------------

    def caliber():
        Region_button_xpath = '/html/body/form/div[2]/div/div/div[1]/div[2]/div[3]/div/div[3]/span'
        Region_button = driver.find_element(By.XPATH, value=Region_button_xpath)
        Region_button.click()
        xpath = '/html/body/div[3]/div/ul/li[10]'
        Ele = driver.find_element(By.XPATH, value=xpath)
        time.sleep(1)
        Ele.click()
        time.sleep(1)
        # ----------------------------
        Y_button_xpath = '/html/body/form/div[2]/div/div/div[1]/div[3]/div[2]/div[1]/div[1]/div/div[3]/span'
        Y_button = driver.find_element(By.XPATH, value=Y_button_xpath)
        Y_button.click()
        xpath = '/html/body/div[4]/div/ul/li[5]'
        Ele = driver.find_element(By.XPATH, value=xpath)
        time.sleep(1)
        Ele.click()
        time.sleep(1)
        # ----------------------------
        X_button_xpath = '/html/body/form/div[2]/div/div/div[1]/div[3]/div[2]/div[1]/div[2]/div/div[3]/span'
        X_button = driver.find_element(By.XPATH, value=X_button_xpath)
        X_button.click()
        css_selector = 'ul.ui-selectonemenu-items[id="xaxisVar_items"] li.ui-selectonemenu-item[data-label="Vehicle Category"]'
        # xpath = '/html/body/div[6]/div/ul/li[1]'
        Ele = driver.find_element(By.CSS_SELECTOR, value=css_selector)
        time.sleep(1)
        Ele.click()
        time.sleep(1)
        return

    def year_selector(year):
        # index = (2023-year)+4
        Year_button_xpath = '/html/body/form/div[2]/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div/div[3]/span'
        Year_button = driver.find_element(By.XPATH, value=Year_button_xpath)
        Year_button.click()
        Yeas_css_selector = f'li.ui-selectonemenu-item[data-label="{year}"]'
        # Year_xpath = '/html/body/div[6]/div/ul/li['+f'{index}'+']'
        # Year = driver.find_element(By.XPATH, value=Year_xpath)
        Year = driver.find_element(By.CSS_SELECTOR, value=Yeas_css_selector)
        time.sleep(1)
        Year.click()
        time.sleep(1)
        return

    def main_refresh():
        main_refresh_xpath = '/html/body/form/div[2]/div/div/div[1]/div[3]/div[3]/div/button/span[2]'
        main_refresh_button = driver.find_element(By.XPATH, value=main_refresh_xpath)
        main_refresh_button.click()
        return

    def filter_EV():
        # css_selector = 'table.ui-selectmanycheckbox[id="fuel"]'
        # table = driver.find_element(By.CSS_SELECTOR, value=css_selector)
        electric_css = 'table.ui-selectmanycheckbox.ui-widget[id="fuel"] tbody tr:nth-child(8) td div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default'
        # electric_xpath = '//*/tr[8]/td/div/div[2]/span'
        electric_button = driver.find_element(By.CSS_SELECTOR, value=electric_css)
        electric_button.click()
        time.sleep(2)
        # refresh_xpath = '/html/body/form/div[2]/div/div/div[3]/div/div[1]/div[1]/span/button/span[2]'
        refresh_button = driver.find_element(By.CSS_SELECTOR, value='button.ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-icon-left[id="j_idt75"]')
        refresh_button.click()
        time.sleep(2)
        return

    def download_file():
        time.sleep(2)
        xpath = '/html/body/form/div[2]/div/div/div[3]/div/div[2]/div/div/div[1]/div[1]/a/img'
        button = driver.find_element(By.XPATH, value=xpath)
        button.click()
        time.sleep(2)

    def get_most_recent_download(download_dir):
        time.sleep(2)
        files = os.listdir(download_dir)
        files_info = [(f, os.path.getmtime(os.path.join(download_dir, f))) for f in files if
                      os.path.isfile(os.path.join(download_dir, f))]
        sorted_files = sorted(files_info, key=lambda x: x[1], reverse=True)
        if sorted_files:
            return sorted_files[0][0]
        else:
            return None

    def rename_file(recent_file_path, year):
        old_file_path = os.path.join(download_dir, recent_file_path)
        new_file_path = os.path.join(download_dir, f"{year}.xlsx")
        os.rename(old_file_path, new_file_path)
        return

    # -----------------------------
    time.sleep(2)
    # click_here_xpath = '/html/body/form/div[2]/div/div/div[3]/div/div[3]/div/span/a/span'
    click_here_css = "span.ui-icon.ui-icon-arrow-4-diag"
    # click_here_button = driver.find_element(By.XPATH, value=click_here_xpath)
    click_here_button = driver.find_element(By.CSS_SELECTOR, value=click_here_css)
    click_here_button.click()
    time.sleep(1)

    for year in range(2019,2024):
        caliber()
        year_selector(year)
        main_refresh()
        time.sleep(2)
        filter_EV()
        download_file()
        recent_file_path = get_most_recent_download(download_dir)
        rename_file(recent_file_path, year)
        time.sleep(2)
    time.sleep(5)
    driver.quit()
    return

EV_Scrapper_function()