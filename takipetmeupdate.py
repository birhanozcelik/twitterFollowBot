from selenium import webdriver
import userInfo
import time
import random

browser = webdriver.Firefox()

url = "https://twitter.com/"

browser.get(url)

time.sleep(3)

giris_yap = browser.find_element_by_xpath("//*[@id='doc']/div/div[1]/div[1]/div[2]/div[2]/div/a[2]");

giris_yap.click()

time.sleep(2)
username = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input");
password = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input");

username.send_keys(userInfo.username)
password.send_keys(userInfo.password)
time.sleep(2)

login = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/div[2]/button")
login.click()
time.sleep(5);

search = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div/header/div/div/div/div/div[2]/nav/a[2]/div");
search.click()
time.sleep(2)

browser.get("https://twitter.com/Kurulusosmanatv/followers")
time.sleep(2)


lenOfPage = browser.execute_script("window.scrollTo(0,document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount=lenOfPage
    elements=browser.find_elements_by_css_selector(r".css-18t94o4.css-1dbjc4n.r-1niwhzg.r-p1n3y5.r-sdzlij.r-1phboty.r-rs99b7.r-1w2pmg.r-1vsu8ta.r-aj3cln.r-1fneopy.r-o7ynqc.r-6416eg.r-lrvibr")
    for element in elements:
        print(len(elements))    
        try:
            element.click()
            randomDeger = random.randrange(15,20)
            time.sleep(randomDeger)
        except Exception as e:
            print(e)
    lenOfPage = browser.execute_script("window.scrollTo(0,document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    ##lastCount= lenOfPage
    time.sleep(3)
    if lastCount == lenOfPage:
        match = True
time.sleep(5)

browser.close()
