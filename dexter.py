from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
 
post = input("what do you want to post on facebook? : ")
id = input("E-mail : ")
pw = input("Password : ")
driver = webdriver.Firefox()

driver.get('https://www.facebook.com/')
print("Opened facebook...")
time.sleep(2)

email = driver.find_element_by_xpath("//input[@id='email' or @name='email']")
email.send_keys(id)
print("Email Id entered...")
time.sleep(2)

password = driver.find_element_by_xpath("//input[@id='pass']")
password.send_keys(pw)
print("Password entered...")
time.sleep(2)

button = driver.find_element_by_xpath("//input[@id='u_0_2' or @value='Log In']")
button.click()
print("logged in...")
time.sleep(2)
driver.get("https://www.facebook.com/arnab.bhattacharya007")

button = driver.find_element_by_xpath("//div[@class='notranslate _5rpu']")

button.send_keys(post)
button.send_keys(Keys.ENTER)
time.sleep(2)
driver.execute_script("window.scrollTo(0, 150)") 
button = driver.find_element_by_xpath("//button[@class='_1mf7 _4r1q _4jy0 _4jy3 _4jy1 _51sy selected _42ft']")
button.click()
time.sleep(5)
driver.close()

