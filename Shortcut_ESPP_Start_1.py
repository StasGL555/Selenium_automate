import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary



from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False



binary = FirefoxBinary('F:\FirefoxPortableLegacy45\FirefoxPortable.exe')
driver = webdriver.Firefox(firefox_binary=binary, capabilities=cap, executable_path=r'C:\Users\Stas\Desktop\Selenium\FireFox\geckodriver.exe')

url = driver.command_executor._url       #"http://127.0.0.1:60622/hub"
session_id = driver.session_id            #'4e167f26-dc1d-4f51-a207-f761eaf73c31'
f = open('id_url.txt', 'w')
f.write(url + '\n')
f.write(session_id)
f.close()
driver.get('http://espp/sm/index.do')
login_box = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'LoginUsername')))
login_box.send_keys('user')
pass_box = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'LoginPassword')))
pass_box.send_keys('pass')
pass_box.send_keys(Keys.RETURN)
        

#Find inactive session message and click OK
count = 0
while True:
    try:
        while True:
            frames = driver.find_elements_by_tag_name('iframe')
            print(len(frames))
            for frame in frames:
                print(frame.size, frame.location, frame.get_attribute('name'))

         
            try:
                for i in range(1,14):
                    print('Window caption:', driver.title)
                    if (driver.title).find('Your inactive session will terminate') >= 0:
                        for i in driver.find_elements_by_tag_name('button'):
                            if i.text != '':
                                print('Button caption:', i.text)
                            if i.text == 'OK' or i.text == 'ОК':
                                i.click()
                                time.sleep(5)
                                break
                        break
                    time.sleep(0.2)
            except:
                print("Exception raised when search inactive session")
                
                
            try:
                for i in driver.find_elements_by_tag_name('button'):
                    if i.text != '':
                        print('Button caption:', i.text)
                        if i.text == 'Обновить' and count >= 160:
                            count = 0 
                            print('Time to refresh, click refresh button')
                            i.click()
                            break
            except:
                print("Exception raised while refresh procedure")
                    

            count = count + 1
            time.sleep(22)
    except Exception as e:
        print("What the fuck occur, see exception:")
        print(e)
        #input("Press any key to exit")
    time.sleep(30)
    
