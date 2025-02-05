from selenium import webdriver       #import selenium module
from selenium.webdriver.support.ui import Select  

def print_list_of_devices():
    driver.get("https://www.bell.ca/Mobility/Smartphones_and_mobile_internet_devices") 
    at = driver.find_elements_by_xpath("//a[@class='rsx-product-hotspot']") #selecting elements to retrive Device description 

    print("**TOP 12 DEVICES:**") 
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
    print("6 {}".format(li1[1]))                 #evice 7th

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

    li = at[11].text
    li1 = li.split('\n')
    print("11 {}".format(li1[1]))                # device 12th
    
def perform_task(i):
    click_on_device(i)
    name_of_device()
    select_click_elements()
    print_description(i)
    ask_user_print_list()
    
def click_on_device(i):                          #clicking on device to navigate webpage
    l1 = driver.find_elements_by_xpath('//a[@class="rsx-product-hotspot"]')
    driver.implicitly_wait(3)
    l1[i].click()


def name_of_device():                           #Fetching name of device after clicking on device from webpage
    n1 = driver.find_element_by_xpath("//h1[@class='rsx-bell-font txtBlack2']")
    print("NAME OF DEVICE:  {}".format(n1.text))
    print("\n")

def select_click_elements():                     #Selecting elements to fetch subsidized phone price info

    p1 = driver.find_element_by_xpath(
        '//div[@class="bcx-pricing-options-header1 rsx-txt-center rsx-bell-font rsx-txt-white rsx-txt-size-22"]')
    print("UNDER: {}".format(p1.text))            #print heading

    r1 = driver.find_elements_by_xpath('//span[@class="rsx-radio"]')
    r1[1].click()                                 #click on subsidize radio option
    driver.implicitly_wait(6)

    t1 = driver.find_elements_by_xpath('//span[@class="title"]')  # Print title: Pay a subsidized phone price
    print("OPTION SELECTED {}".format(t1[1].text))
    
def print_description(i):
    pr = driver.find_elements_by_xpath('//div[@class="rsx-price"]')        #Starting price
    pl = driver.find_elements_by_xpath('//p[@class="rsx-txt-size-18"]')    #selecting elements to print terms
    pl2 = driver.find_elements_by_xpath('//p[@class="1rsx-note"]')         #selecting elements to print terms
    pl23 = driver.find_elements_by_xpath('//p[@style="font-size:12px;"]')  #selecting elements to print terms

    if i in [0,1,4,5,6,7,8,10]:                                            #Printing Starting Prices and Terms
        print("1. Price: {}\n   Terms: {}\n          {}\n".format(pr[0].text,pl[0].text,pl2[0].text))
        print("2. Price: {}\n   Terms: {}\n          {}\n".format(pr[1].text, pl[1].text, pl2[1].text))
        print("3. Price: {}\n   Terms: {}\n".format(pr[2].text, pl[2].text, pl2[1].text))


    elif i in [2,3,9]:                                                     #Printing Starting Prices and Terms
        print("1. Price: {}\n   Terms: {}\n          {}\n          {}\n".format(pr[0].text,pl[0].text,pl2[0].text,pl23[0].text))  # Printing Starting Prices and Terms
        print("2. Price: {}\n   Terms: {}\n          {}\n".format(pr[1].text,pl[1].text,pl2[1].text))
        print("3. Price: {}\n   Terms: {}\n          {}\n".format(pr[2].text, pl[2].text, pl2[2].text))
        print("4. Price: {}\n   Terms: {}\n".format(pr[3].text,pl[3].text))


    elif i == 11:                                                          #Printing Starting Prices and Terms
        print("1. Price: {}\n   Terms: {}\n          {}\n".format(pr[0].text,pl[0].text,pl2[0].text))  # Printing Starting Price and Terms
        print("2. Price: {}\n   Terms: {}\n          {}\n".format(pr[1].text, pl[1].text, pl2[1].text))

def ask_user_print_list():                                                  #function to ask user to print list again
    print('Enter "Y" to print list of devices again ')
    ans = input()
    if ans == 'Y':
        print_list_of_devices()

    driver.get("https://www.bell.ca/Mobility/Smartphones_and_mobile_internet_devices")
     #if 'Y' not selected program will navigate back to main webpage, user can again input device ID to get information. 
    print("**********************************************************************************")
    print("Enter the ID Number of device you want to select (mentioned with names of devices)")
    print("**********************************************************************************")

# Setting driver to Google Chrome, Giving execulatbe path of chromedriver
driver = webdriver.Chrome(executable_path="/Users/asmitasharma/Downloads/chromedriver 3")

# welcome Message
print("*************************")
print("WELCOME TO BELL MOBILITY!")
print("*************************")

print_list_of_devices()  #Function calling names of devices

print("**********************************************************************************")
print("Enter the ID Number of device you want to select (mentioned with names of devices)")
print("**********************************************************************************")

while True:

    i = int(input()) #input device ID 
    if i in range(0,12):
        perform_task(i) 
        continue

    else:
        print('Invalid Device ID, Enter again:')
