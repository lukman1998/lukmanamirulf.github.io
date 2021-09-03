import time 
from selenium import webdriver

browser = webdriver.Chrome('/Users/acer/Desktop/chromedriver')
#Link Browser
browser.get("https://shopee.co.id/product/52635036/6259445668/")
buyButton = False

while not buyButton:
    try:
        # if this work then the button is not pytopen
        addToCartBtn = addButton = browser.find_element_by_class_name("btn btn-tinted")
        
        # button isnt open restrat the script 
        print("Button isnt ready yet.")
        
        # Refresh page after a delay
        time.sleep(1)
        browser.refresh()
    
    except:
        addToCartBtn = addButton = browser.find_element_by_class_name("btn btn-solid-primary")
        
        # Click the button and end the script
        print("Button was clicked")
        addToCartBtn.click()
        buyButton = True
