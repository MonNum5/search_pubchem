

from selenium import webdriver
import time
import os

gecko_path = r'geckodriver.exe'
root_path = os.getcwd()

# Set Firefox profile
profile = webdriver.FirefoxProfile()

profile.set_preference("browser.download.dir",os.path.join(root_path,'Downloads'));
profile.set_preference("browser.download.folderList",2);
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/csv,application/excel,application/vnd.msexcel,application/vnd.ms-excel,text/anytext,text/comma-separated-values,text/csv,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/octet-stream");
profile.set_preference("browser.download.manager.showWhenStarting",False);
profile.set_preference("browser.helperApps.neverAsk.openFile","application/csv,application/excel,application/vnd.msexcel,application/vnd.ms-excel,text/anytext,text/comma-separated-values,text/csv,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/octet-stream");
profile.set_preference("browser.helperApps.alwaysAsk.force", False);
profile.set_preference("browser.download.manager.useWindow", False);
profile.set_preference("browser.download.manager.focusWhenStarting", False);
profile.set_preference("browser.download.manager.alertOnEXEOpen", False);
profile.set_preference("browser.download.manager.showAlertOnComplete", False);
profile.set_preference("browser.download.manager.closeWhenDone", True);
profile.set_preference("pdfjs.disabled", True);

# start driver
driver = webdriver.Firefox(executable_path=gecko_path, firefox_profile=profile)

molecular_formula = 'c8h10'

# get all possible molecules
driver.get("https://pubchem.ncbi.nlm.nih.gov/#query={}".format(molecular_formula))

time.sleep(3)
# click to download summary table
download_element = driver.find_element_by_id('Download')
download_element.click()

download_element = driver.find_elements_by_link_text('CSV')
time.sleep(1.5)
download_element[0].click()
time.sleep(1.5)
driver.close()

import pandas as pd

df = pd.read_csv('Downloads/PubChem_compound_text_c8h10.csv',sep=',')

# for every cid open pubchem database entry
for _id in ['11355451']:#df['cid']: 
    driver = webdriver.Firefox(executable_path=gecko_path, firefox_profile=profile)
    driver.get('https://pubchem.ncbi.nlm.nih.gov/compound/{}'.format(_id))
    
    #Click Download Button
    time.sleep(2)
    download_element = driver.find_element_by_xpath('//*[@title="Download data used to display this page"]')
    download_element.click()
    time.sleep(1)
    download_element = driver.find_elements_by_link_text('Save')
    download_element[0].click()
    time.sleep(1.5)
    driver.close()
    


#browser.find_element_by_xpath('//*[@title="Download data used to display this page"]').click()
#https://pubchem.ncbi.nlm.nih.gov/#query=c8h10