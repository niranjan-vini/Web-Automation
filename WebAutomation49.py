from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os


class WebAutomation:
    def __init__(self):
        # define driver,option,and service
        chrome_option = Options()
        chrome_option.add_argument("--disable-search-engine-choice-screen")
        service = Service("chroma driver/chromedriver.exe")

        download_path = os.getcwd()
        images = {"download.default_directory": download_path}
        chrome_option.add_experimental_option("prefs", images)
        self.driver = webdriver.Chrome(options=chrome_option, service=service)

    def login(self,username,password1):
        # load webpage
        self.driver.get("https://demoqa.com/login")

        # locate username,password and login button
        user_name = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, 'userName')))
        password = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, 'password')))
        login = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, 'login')))

        # fill in username and password
        user_name.send_keys(username)
        password.send_keys(password1)
        login.click()

    def fill_form(self,username,gmail,currentaddress,permanentaddress):

        element = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH,
                                                     '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
        element.click()

        text_box = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.ID, 'item-0')))
        text_box.click()

        # located thr form filed and submit button
        fill_name = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.ID, 'userName')))
        email = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.ID, 'userEmail')))
        current_address = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.ID, 'currentAddress')))
        permanent_address = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.ID, 'permanentAddress')))
        submit_button = self.driver.find_element(By.ID, 'submit')

        # fill in the form fileds
        fill_name.send_keys(username)
        email.send_keys(gmail)
        current_address.send_keys(currentaddress)
        permanent_address.send_keys(permanentaddress)
        self.driver.execute_script("arguments[0].click();", submit_button)

    def download(self):
        # located the upload and download section and download button

        upload_download = WebDriverWait(self.driver
                                        , 10).until(ec.visibility_of_element_located((By.ID, 'item-7')))
        upload_download.click()
        download_button = self.driver.find_element(By.ID, 'downloadButton')
        self.driver.execute_script("arguments[0].click();", download_button)

    def close(self):
        input("press enter to close browser")
        self.driver.quit()

WebAutomation=WebAutomation()
WebAutomation.login("vinay","Vinay8722@")
WebAutomation.fill_form("niranjan","niranjan@gmail.com","chakkere",
                        "channapatna")
WebAutomation.download()
WebAutomation.close()