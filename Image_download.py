
#argv[1]="D:\\USF\Selenium\chromedriver.exe"
#argv[2]='D:\\USF\\Selenium\\'
# The outcome will be saved with the following name For eg. "30#####. png" in the same location where the file has been executed
desti
# The example running script will look like the following:
# AuthorName: Sameera Prasad, Vivek Singh

#################################################################################################
# download pages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
import openpyxl
import csv
import time
import pandas as pd
import urllib.request
import datetime
import shutil
import os 
import sys



chromeoptions = Options()
#driver = webdriver.Chrome(executable_path=argv[1], chrome_options=chromeoptions)
chromeoptions.add_argument('headless')
try:
	driver = webdriver.Chrome(executable_path="D:\\USF\Selenium\chromedriver.exe", chrome_options=chromeoptions)

except:
	pass
#time.sleep(10)

fp=open('20190213.csv')				#file containin g all the url generated
urls=fp.readlines()
data_m=pd.DataFrame()
now = datetime.datetime.now()
current_date = now.strftime("%Y-%m-%d")			#prints today's date and stores in current_date variable
image_path=sys.argv[2]				#path of the folder
destination=os.path.join(image_path+current_date)			#file being name with today's date
os.makedirs(destination)				#folder getting created with name destionation hence can be ignored
for url in urls:
	try:

		driver.get(url)
		time.sleep(10)

		image_element = driver.find_elements_by_xpath("//a[@class='classroom-photo js-classroom-photo-format-retina-bg ']")  #image extraction
		image_url = 'http:' + image_element[0].get_attribute('style').split(':')[2].split('"')[0]
		file_name = url.split('/')[-2] + '.png'
		urllib.request.urlretrieve(image_url,destination+'\\'+ file_name)			#filename being saved
		
		
		#fp.close()
	except:
		print("imagenotfound_"+url)
	
	#except:
		#print(url)
#time.sleep(10)

