import selenium 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
import sys
from selenium import webdriver 
import pandas as pd 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random 
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path = 'chromedriver.exe')

url = r'https://whoer.net/'
driver.get(url)

info = {
        'ISP' : [], 
        'Hostname' : [], 
        'OS' : [], 
        'Browser' : [], 
        'DNS' : [], 
        'Proxy' : [], 
        'Anonymizer' : [], 
        'Blacklist' : [], 
        'Reversed' : [], 
        'Country' : [] , 
        'Region' : [], 
        'City' : [], 
        'ZIP' : [], 
        'Hostname' : [], 
        'Zone' : [], 
        'Local' : [], 
        'System' : [], 
        'IP range' : [], 
        'ISP' : [], 
        'Organization' : [], 
        'AS Organization' : [], 
        'AS Number' : [], 
        }
info['ISP'].append(driver.find_element_by_xpath('//*[@id="main"]/section[1]/div/div/div/div[3]/div[1]/div[1]/div[3]/div/span').text)
info['Hostname'].append(driver.find_element_by_xpath('//*[@id="main"]/section[1]/div/div/div/div[3]/div[1]/div[2]/div[3]/div/span').text)
info['OS'].append(driver.find_element_by_xpath('//*[@id="main"]/section[1]/div/div/div/div[3]/div[1]/div[3]/div[3]/div/span').text)
info['Browser'].append(driver.find_element_by_xpath('//*[@id="main"]/section[1]/div/div/div/div[3]/div[1]/div[4]/div[3]/div/span').text)
info['DNS'].append(driver.find_element_by_xpath('//*[@id="main"]/section[1]/div/div/div/div[3]/div[2]/div[1]/div[3]/div/div[2]/div/span[2]/span[1]').text)
info['Proxy'].append(driver.find_element_by_xpath('//*[@id="main"]/section[1]/div/div/div/div[3]/div[2]/div[2]/div[3]/div/span[2]').text)
info['Anonymizer'].append(driver.find_element_by_xpath('//*[@id="anonymizer"]/div/span[2]').text)
info['Blacklist'].append(driver.find_element_by_xpath('//*[@id="main"]/section[1]/div/div/div/div[3]/div[2]/div[4]/div[3]/div/span[2]/a').text)
info['Reversed'].append(driver.find_element_by_xpath('//*[@id="main"]/section[5]/div/div/div/div[1]/div[1]/div[1]/div[1]/div/div/div[2]/div[6]/div[2]/span').text)
info['Country'].append(driver.find_element_by_xpath('//*[@id="main"]/section[5]/div/div/div/div[1]/div[1]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/span/span[1]').text)
info['Region'].append(driver.find_element_by_xpath('//*[@id="main"]/section[5]/div/div/div/div[1]/div[1]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/span').text)
info['City'].append(driver.find_element_by_xpath('//*[@id="main"]/section[5]/div/div/div/div[1]/div[1]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/span').text)
info['ZIP'].append(driver.find_element_by_xpath('//*[@id="main"]/section[5]/div/div/div/div[1]/div[1]/div[1]/div[1]/div/div/div[2]/div[4]/div[2]/span').text)
info['Hostname'].append(driver.find_element_by_xpath('//*[@id="main"]/section[5]/div/div/div/div[1]/div[1]/div[1]/div[1]/div/div/div[2]/div[5]/div[2]').text)
info['Zone'].append(driver.find_element_by_xpath('//*[@id="main"]/section[5]/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/div[2]').text)
info['Local'].append(driver.find_element_by_xpath('//*[@id="main"]/section[5]/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/div[2]').text)
info['System'].append(driver.find_element_by_xpath('//*[@id="main"]/section[5]/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/div[2]/span').text)
info['IP range'].append(driver.find_element_by_xpath('//*[@id="main"]/section[5]/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/div[2]/span').text)
info['ISP'].append(driver.find_element_by_xpath('//*[@id="main"]/section[5]/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/div[2]/span').text)
info['Organization'].append(driver.find_element_by_xpath('//*[@id="main"]/section[5]/div/div/div/div[1]/div[1]/div[1]/div[1]/div/div/div[2]/div[9]/div[2]').text)
info['AS Organization'].append(driver.find_element_by_xpath('//*[@id="main"]/section[5]/div/div/div/div[1]/div[1]/div[1]/div[1]/div/div/div[2]/div[10]/div[2]').text)
info['AS Number'].append(driver.find_element_by_xpath('//*[@id="main"]/section[5]/div/div/div/div[1]/div[1]/div[1]/div[1]/div/div/div[2]/div[11]/div[2]').text)


print(info)