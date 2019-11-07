from selenium import webdriver
from selenium.webdriver.support.ui import Select


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
