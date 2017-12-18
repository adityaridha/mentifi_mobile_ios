from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import time


class Navbar():

    dashboard_id = "Dashboard"
    networks_id = "Networks"
    bulletin_id = "Bulletin"
    messages_id = "Message"
    profile_id = "Profile"

    def __init__(self, driver):
        self.driver = driver

    def tap_dashboard(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, self.dashboard_id)))
            print("Dashboard menu is Ready")
        except TimeoutException:
            print("Can't find dashboard menu")

        self.driver.find_element_by_id(self.dashboard_id).click()

    def tap_networks_menu(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, self.networks_id)))
            print("Networks menu is Ready")
        except TimeoutException:
            print("Can't tap networks menu")

        self.driver.find_element_by_id(self.networks_id).click()

    def tap_bulletin_menu(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, self.bulletin_id)))
            print("Bulletin menu is Ready")
        except TimeoutException:
            print("Can't tap feature menu")

        self.driver.find_element_by_id(self.bulletin_id).click()

    def tap_messages_menu(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, self.messages_id)))
            print("Messages menu is Ready")
        except TimeoutException:
            print("Can't tap feature menu")

        self.driver.find_element_by_id(self.messages_id).click()

    def tap_profile_menu(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, self.profile_id)))
            print("Profile menu is Ready")
        except TimeoutException:
            print("Can't tap feature menu")

        self.driver.find_element_by_id(self.profile_id).click()