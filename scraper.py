from selenium import webdriver
import time
import os
import csv

def pretty_print():
    print "****************************************"

""" function to write scraped data to csv file """
def write_to_csv(content):
    with open("petrol-rates.csv", "wb") as csvfile:
        writer = csv.DictWriter(csvfile, content[0].keys())
        writer.writeheader()
        writer.writerows(content)

""" function returns selenium mac driver """
def chrome_driver():
        driver = os.getcwd() + os.path.sep + "driver" + os.path.sep + "chromedriver"
        #print driver
        os.environ["webdriver.chrome.driver"] = driver
        return driver

to_csv = []

url = "http://www.mypetrolprice.com/5/Petrol-price-in-Chennai"
chrome = webdriver.Chrome(chrome_driver())
chrome.get(url)

for i in range(30):
    print "page #{}".format(i+1)
    pretty_print()

    """
    after inspecting source code of http://www.mypetrolprice.com/5/Petrol-price-in-Chennai
    it is found that:
    span element with class name price contains price. find and extract """
    prices = chrome.find_elements_by_css_selector("span[class='price']")
    """span element with class name alignment contains date. find and extract """
    dates = chrome.find_elements_by_css_selector("span[class='alignment']")

    for i, val in enumerate(prices):
        price = str(prices[i].text).split("=")[1].strip()
        date = str(dates[i].text).split(":")[1].strip().replace(")", "")

        entry = {}
        entry["rate"] = price
        entry["date"] = date
        to_csv.append(entry)
        print "Gold rate is {} as on {}".format(price, date)

    pretty_print()
    chrome.find_element_by_xpath("//input[@id='CPH1_GridView1_GridViewPager_ImageButtonNext']").click()

write_to_csv(to_csv)
chrome.quit()
