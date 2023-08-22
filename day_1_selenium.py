import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver = webdriver.Chrome("C:\Program Files\drivers.exe\chromedriver.exe")

driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element(By.NAME, "email").send_keys("7709540623")
driver.find_element(By.ID, "pass").send_keys("sahu1996")
driver.find_element(By.NAME, "login").click()
print(f"Page Title :{driver.title}")
print(f"Page URL :{driver.current_url}")

driver.find_element(By.XPATH, "//a[@id='u_7_s_Ii']//div[@class='_7om2 _52we _6ra0 _6rvk']").click()
driver.close()
# time.sleep(20)