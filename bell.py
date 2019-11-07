from selenium import webdriver
from selenium.webdriver.support.ui import Select

def print_list_of_devices():
    driver.get("https://www.bell.ca/Mobility/Smartphones_and_mobile_internet_devices")
    # Retreving names of Top 12 Smartphone devices by selcting elements through its class
    at = driver.find_elements_by_xpath("//a[@class='rsx-product-hotspot']")

    print("**TOP 12 DEVICES:**")
    #Due to different formating fetching names of devices as following:
    #Fetching names from main webpage

    for i in range(0, 4):
        li = at[i].text
        li1 = li.split('\n')
        print("{} {}".format(i, li1[1]))       # Device 1,2,3,4

    for i in range(4, 6):
        li = at[i].text
        li1 = li.split('\n')
        print("{} {}".format(i, li1[0]))        # Device 5,6th

    li = at[6].text
    li1 = li.split('\n')
    print("6 {}".format(li1[1]))                # device 7th

    for i in range(7, 9):
        li = at[i].text
        li1 = li.split('\n')
        print("{} {}".format(i, li1[0]))         # device 8th,9th

    li = at[9].text
    li1 = li.split('\n')
    print("9 {}".format(li1[1]))                 # device 10th

    li = at[10].text
    li1 = li.split('\n')
    print("10 {}".format(li1[0]))                # device 11th

    # device 12th
    li = at[11].text
    li1 = li.split('\n')
    print("11 {}".format(li1[1]))                 # device 12th
    
    
def click_on_device(i):
    l1 = driver.find_elements_by_xpath('//a[@class="rsx-product-hotspot"]')
    driver.implicitly_wait(3)
    l1[i].click()


def name_of_device():
    n1 = driver.find_element_by_xpath("//h1[@class='rsx-bell-font txtBlack2']")
    print("NAME OF DEVICE:  {}".format(n1.text))
    print("\n")

def select_click_elements():
    # Selecting elements to fetch subsidized phone price info

    p1 = driver.find_element_by_xpath(
        '//div[@class="bcx-pricing-options-header1 rsx-txt-center rsx-bell-font rsx-txt-white rsx-txt-size-22"]')
    print("UNDER: {}".format(p1.text))  # print heading

    r1 = driver.find_elements_by_xpath('//span[@class="rsx-radio"]')
    r1[1].click()  # Selecting elements to fetch subsidized phone price info
    driver.implicitly_wait(6)

    t1 = driver.find_elements_by_xpath('//span[@class="title"]')  # Priint title: Pay a subsidized phone price
    print("OPTION SELECTED {}".format(t1[1].text))


# Setting driver to Google Chrome, Giving execulatbe path of chromedriver
driver = webdriver.Chrome(executable_path="/Users/asmitasharma/Downloads/chromedriver 3")

# welcome Message
print("*************************")
print("WELCOME TO BELL MOBILITY!")
print("*************************")

print_list_of_devices()  # Function calling names of devices

print("**********************************************************************************")
print("Enter the ID Number of device you want to select (mentioned with names of devices)")
print("**********************************************************************************")

while True:

    i = int(input())
    if i in range(0,12):
        perform_task(i)
        continue

    else:
        print('Invalid Device ID, Enter again:')
