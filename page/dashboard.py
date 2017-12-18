from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class Dashboard():


    notif = "notificationIcon"
    connected_mentors_id = "Connected Mentors"
    pending_mentors_id ="Pending Mentors"


    def __init__(self, driver):
        self.driver = driver

    def verified_all_element(self):
        try:
            WebDriverWait(self.driver, 60).until(ec.presence_of_element_located((By.ID, self.connected_mentors_id)))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.ID, self.pending_mentors_id)))
            print("Dadshboard page is compleately loaded")
        except TimeoutException:
            print("Dashboard element not ready")

    def tap_connected_mentors(self):
        self.driver.find_element_by_id(self.connected_mentors_id).click()

    def tap_pending_mentors(self):
        self.driver.find_element_by_id(self.pending_mentors_id).click()


