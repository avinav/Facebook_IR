import os
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromeDriver = "/home/avinav/applications/chromedriver";
driver = webdriver.Chrome(chromeDriver);
driver.get("http://www.facebook.com");
file = open("/home/avinav/test/pass");
password = file.readline();
eEmail = driver.find_element_by_name("email");
ePass = driver.find_element_by_name("pass");
eEmail.send_keys("sharan.avinav@gmail.com");
ePass.send_keys(password);
#driver.execute_script("document.getElementById('pass').value+='hello'");

#eSearch = WebDriverWait(driver, 10).until(
#	EC.presence_of_element_located(By.NAME("q"))
#	)

#eSearch = wait.until(EC.visibility_of_element_located((By.NAME,'q')))
eSearch = driver.execute_script("return document.getElementsByName('q')[0]")
#eSearch = driver.find.element_by_id("u_0_d");
print eSearch

eSearch.send_keys("people at university at buffalo\n");
driver.implicitly_wait(10)
list = driver.execute_script("return document.getElementById('browse_result_area')")
print list
#driver.execute_script("return document.getElementsByName('q')[0]");

#eButton = driver.find_element_by_class_name('_585_');
#eButton.click();

