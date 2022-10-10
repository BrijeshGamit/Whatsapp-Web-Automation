from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import os
import time

chrome_driver = "C:/python/webauto/chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress","127.0.0.1:9222")

#user_name = "Mummy"
#user_name = "Apne😊😇😊"
#user_name = "ToDo list"
user_name = "Nitin Bhai"
#msg = "Good night \n"



driver = webdriver.Chrome(chrome_driver,options=chrome_options)
#driver.get("https://web.whatsapp.com/")
#input("Enter anything after qr scan")
#user = driver.find_element_by_xpath("//span[@title='{}']".format(user_name))
def printit():
	time.sleep(10)
	#threading.Timer(5.0, printit).start()
	attach = driver.find_element_by_css_selector("div[title='Attach']")
	attach.click()
	path="C:/python/webauto/imgs/"
	files=os.listdir(path)
	d=random.choice(files)
	file = "C:/python/webauto/imgs/"+d
	media = driver.find_element_by_css_selector("#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._3HQNh._1un-p > div._2jitM > div > span > div > div > ul > li:nth-child(1)")
	media.click()
	input_file = driver.find_element_by_css_selector("#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._3HQNh._1un-p > div._2jitM > div > span > div > div > ul > li:nth-child(1) > button > input[type=file]")
	input_file.send_keys(file)
	driver.implicitly_wait(1000)
	send_btn = driver.find_element_by_css_selector("#app > div > div > div._3ArsE > div.ldL67._3sh5K > span > div > span > div > div > div.KPJpj._2M_x0 > div > div._1HI4Y > div._33pCO > div")
	send_btn.click()
	time.sleep(5)
	printit()
printit()
#msg_box = driver.find_element_by_xpath("//div[@data-tab='6']")
#msg_box.send_keys(msg)



#driver.implicitly_wait(10)

#send_btn = driver.find_element_by_class_name('_2Ujuu')
# txt_box = driver.find_element_by_name("q")
# txt_box.send_keys(search)
# driver.implicitly_wait(10)
# search_btn = driver.find_element_by_name("btnK")
# search_btn.click()