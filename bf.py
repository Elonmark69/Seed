from selenium import webdriver
from time import sleep
from datetime import datetime
import threading


class phraser:

    def __init__(self):

        # vars
        self.url = 'http://localhost:4000'
        self.crypto = 'TCsT2K8eJc45yzYNsFZPLJG3WWKdh5VM5q'
        self.address = ''
        self.phrase = ''
        self.threads = []
        self.now = datetime.now().strftime("%H:%M:%S")
        # open browser
        self.driver = webdriver.Chrome('/home/sask/Downloads/chromedriver')
        self.driver.get(self.url)
        # execute function
         #Logger
        self.f = open("logs.txt", "a")
        self.success = '[-] ['+self.now+'] FOUND ! PHRASE : ' + self.phrase
        self.fail = '[+] ['+self.now+'] Not Found'
        
        while self.address != self.crypto:
            self.f.writelines('\n'+self.fail)
            print (self.fail)
            self.get_seed()
        else:
          print (self.success)
          self.f.writelines('\n'+self.success)

    def get_seed(self):
        self.driver.find_element_by_id('btn generate').click()
        sleep(3)
        self.address = self.driver.find_element_by_id('address').text
        self.phrase = self.driver.find_element_by_id('phrase').get_attribute('value')

    def threader(self):    
        for _ in range(10):
    	    self.t = threading.Thread(target=self.get_seed)
    	    self.t.start()
    	    self.threads.append(self.t)

        for thread in self.threads:

    	    thread.join()

    
		
s = phraser()