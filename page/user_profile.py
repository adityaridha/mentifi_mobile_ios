from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import pytest


class UserProfile():


    profile_picture_id = "ic_account_circle_48pt"
    biography_id = "Biography"
    work_address_id = "Work Address"
    education_name = "Education"
    experience_id = "Experience"
    preferences_id "Preferences"
    logout_button_id = "Logout"
    edit_button_id = "Edit"


    def __init__(self, driver):
        self.driver = driver

    def verified_all_element(self):
        try:
            WebDriverWait(self.driver, 30).until(ec.presence_of_element_located((By.ID, self.profile_picture_id)))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.ID, self.biography_id)))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.NAME, self.education_name)))
            print("Profile page is compleately loaded")
        except TimeoutException:
            print("Profile page is not ready")

    def tap_logout(self):

        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, self.logout_id)))
            print("Log out button is found")
        except TimeoutException:
            print("Log out button not ready")


        self.driver.find_element_by_id(self.loc_logout_id).click()