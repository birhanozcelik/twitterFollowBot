from selenium import webdriver
import userInfo
import time

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

browser.get("https://twitter.com/search?q=%23KurulusOsman&src=recent_search_click")
time.sleep(3)


lenOfPage = browser.execute_script("window.scrollTo(0,document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount= lenOfPage
    lenOfPage = browser.execute_script("window.scrollTo(0,document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    time.sleep(3)
    elements=browser.find_elements_by_css_selector(".r-4qtqp9.r-yyyyoo.r-1xvli5t.r-dnmrzs.r-bnwqim.r-1plcrui.r-lrvibr.r-1hdv0qi")
    for element in elements[2::8]:
        try:
            print(len(elements))
            element.click()
            time.sleep(3)
        except Exception as e:
            print(e)
    if lastCount == lenOfPage:
        match = True

elements=browser.find_elements_by_css_selector(".css-1dbjc4n.r-xoduu5")
for element in elements:
    try:
        element.click()
        time.sleep(3)
    except Exception as e:
        print(e)
    

time.sleep(5)

browser.close()
