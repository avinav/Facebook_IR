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
wait = WebDriverWait(driver, 10);
eSearch = wait.until(EC.visibility_of_element_located((By.NAME,'q')))



#eSearch = driver.find.element_by_id("u_0_d");
#eSearch.send_keys("people at university at buffalo");


js = """document.getElementsByName('q')[0].focus();
	document.getElementsByName('q')[0].value='people at university at buffalo';
	var ev = document.createEvent('KeyboardEvent');
	ev.initKeyEvent( 'keydown', true, true, window, false, false, false, false, 13, 0); 
	document.body.dispatchEvent(ev);""";
js1 = """document.getElementsByName('q')[0].focus();
document.getElementsByName('q')[0].value='People who go to University at Buffalo Graduate School ';
Podium = {};
Podium.keydown = function(k) {
    var oEvent = document.createEvent('KeyboardEvent');

    // Chromium Hack
    Object.defineProperty(oEvent, 'keyCode', {
                get : function() {
                    return this.keyCodeVal;
                }
    });     
    Object.defineProperty(oEvent, 'which', {
                get : function() {
                    return this.keyCodeVal;
                }
    });     

    if (oEvent.initKeyboardEvent) {
        oEvent.initKeyboardEvent("keydown", true, true, document.defaultView, false, false, false, false, k, k);
    } else {
        oEvent.initKeyEvent("keydown", true, true, document.defaultView, false, false, false, false, k, 0);
    }

    oEvent.keyCodeVal = k;

    if (oEvent.keyCode !== k) {
        alert("keyCode mismatch " + oEvent.keyCode + "(" + oEvent.which + ")");
    }

    document.dispatchEvent(oEvent);
}
Podium.keydown(13);"""
driver.execute_script(js1);

#eButton = driver.find_element_by_class_name('_585_');
#eButton.click();

