# Bell: Starting Price Lookup
### Objective
To develop program which enables user to select device and then fetch starting prices and terms for it. Following expectations are fulfilled. 
- Program navigates to given webpage and reterive top 12 devices. 
- Program provides user list of top 12 devices. 
- Program takes input from user to select device, selenium runs to visit webpage and click on the specific device. 
- Program is fuctioned to select option: Pay a subsidize phone price, under Payment and pricing option. 
- Name of device, Starting prices and terms are printed as output of program. 
- Programs is developed to again show list of devices and again select a different device to fetch information. 

### Technologies Used
- Programming language: Python (Version- Python 3.7.5)
- Code is developed in Pycharm environment and tested in Pycharm and Command-line. 
- Selenium Webdriver. 
- Chrome driver is used as automated webdriver. 

### How to run Program 
- Download bell.py file. 
- Make sure selenium Module is imported using "pip install selenium" on command line. 
- Provide correct executatbe path for chromedriver at following 115th line of code
  driver = webdriver.Chrome(executable_path= "    ")
- After updating your bell.py file, save it in a folder and open that folder in command line using command: *cd foldername*.
- Run python code as a command in given format: python bell.py
- Program should work on command line, user will get welcome message and list of devices to select one device. 
