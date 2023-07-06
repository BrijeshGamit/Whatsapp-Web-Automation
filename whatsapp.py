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
user_name = "ToDo list"
#user_name = "Nitin Bhai"
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
	media = driver.find_element_by_css_selector("#main > footer > div._2lSWV._3cjY2.copyable-area > div > span:nth-child(2) > div > div._2xy_p._1bAtO > div._1OT67 > div > span > div > div > ul > li:nth-child(1) > button")
	media.click()
	input_file = driver.find_element_by_css_selector("#main > footer > div._2lSWV._3cjY2.copyable-area > div > span:nth-child(2) > div > div._2xy_p._1bAtO > div._1OT67 > div > span > div > div > ul > li:nth-child(1) > button > input[type=file]")
	input_file.send_keys(file)
	driver.implicitly_wait(1000)
	send_btn = driver.find_element_by_css_selector("#app > div > div > div._2QgSC > div._2Ts6i._2xAQV > span > div > span > div > div > div.g0rxnol2.thghmljt.p357zi0d.rjo8vgbg.ggj6brxn.f8m0rgwh.gfz4du6o.r7fjleex.bs7a17vp > div > div.O2_ew > div._3wFFT > div > div > span")
	send_btn.click()
	time.sleep(5)
	printit()
printit()
#msg_box = driver.find_element_by_xpath("//div[@data-tab='6']")
#msg_box.send_keys(msg)

#will code new feature here.

#driver.implicitly_wait(10)

#send_btn = driver.find_element_by_class_name('_2Ujuu')
# txt_box = driver.find_element_by_name("q")
# txt_box.send_keys(search)
# driver.implicitly_wait(10)
# search_btn = driver.find_element_by_name("btnK")
# search_btn.click()