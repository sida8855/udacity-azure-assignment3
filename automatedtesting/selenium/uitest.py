# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from datetime import datetime 

def print_info(info):
    print("{},{}".format(datetime.now(),info))

# Start the browser and login with standard_user
def login ():
    print_info ('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    #driver = webdriver.Chrome()
    print_info ('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')

    print_info("Login with username standard_user and password secret_sauce")
    driver.find_element_by_css_selector("input[id='user-name']").send_keys("standard_user")
    driver.find_element_by_css_selector("input[id='password']").send_keys('secret_sauce')
    driver.find_element_by_css_selector("input[id='login-button']").click()
    print_info("Login successful")
    
    return driver

def add_items_to_cart(driver):
    items = driver.find_elements_by_css_selector("div[class=inventory_item_description]")
    print_info("Find " + str(len(items)) + " items to be added to cart")
    for each in items:
        product_name = each.find_element_by_css_selector("div[class=inventory_item_name]").text
        each.find_element_by_css_selector("button[class='btn btn_primary btn_small btn_inventory']").click()
        print_info("Item " + product_name + " is added to cart")

    print_info("All items are added to cart")

def remove_items_from_cart(driver):
    items = driver.find_elements_by_css_selector("div[class=inventory_item_description]")
    print_info("Find " + str(len(items)) + " items to be removed from cart")
    for each in items:
        product_name = each.find_element_by_css_selector("div[class=inventory_item_name]").text
        each.find_element_by_css_selector("button[class='btn btn_secondary btn_small btn_inventory']").click()
        print_info("Item " + product_name + " is removed from cart")

    print_info("All items are removed from cart") 

driver_login = login()
add_items_to_cart(driver_login)
remove_items_from_cart(driver_login)

