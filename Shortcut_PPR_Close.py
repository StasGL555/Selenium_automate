import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False


#f = open('C:\Users\Stas\AppData\Local\Programs\Python\Python36-32\id_url.txt', 'r')
f = open('id_url.txt', 'r')
url = f.readline()[0:-1]
#url = 'http://127.0.0.1:62468/hub'
session_id = f.readline()
#session_id = '6057e91b-1bfc-43a1-bae1-68f65d7f317c'
print('Connect to existing session:')
print(url)
print(session_id)


#class SessionRemote(webdriver.Remote):
#    def start_session(self, desired_capabilities, browser_profile=None):
#        # Skip the NEW_SESSION command issued by the original driver
#        # and set only some required attributes
#        self.w3c = True

#driver = SessionRemote(command_executor=url, desired_capabilities=cap)
#driver.session_id = session_id


driver = webdriver.Remote(command_executor=url,desired_capabilities={})
driver.session_id = session_id
f.close()
work_time = '00:40' #4 наряда
#work_time = '00:30' #5
#work_time = '00:20' #8
#work_time = '00:10' #16       
#work_time = '00:05'  #32



##########################################В работу button.click##############################################################
def To_Work_Btn():
    for j in range(1,5):
        try:
            #WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, 'button')))
            for i in driver.find_elements_by_tag_name('button'):
                    print(i.text)
                    if i.text == 'В работу':
                        print('(В работу) click() success')
                        i.click()
                        return
        except:
            print('Cant find button (В работу), skip button(В работу) click()')
        time.sleep(0.5)

#WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.TAG_NAME, 'button')))
#driver.switch_to_default_content()
#driver.switch_to_frame('mif-comp-783582')
frames = driver.find_elements_by_tag_name('iframe')
print(len(frames))
for frame in frames:
    print(frame.size, frame.location, frame.get_attribute('name'))


#########################################заполнение трудозатрат######################################################
def HourMin_Fill():
    try:
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.TAG_NAME, 'iframe')))
    except:
        print ('Cant find iframe or its already visible ')
    frames = driver.find_elements_by_tag_name('iframe')
    print(len(frames))
##    for frame in frames:
##        print(frame.size, frame.location, frame.get_attribute('name'))
##        if (frame.get_attribute('name')) != '':
##            print ('Switched to frame:', frame.get_attribute('name'))
##            driver.switch_to_frame(frame.get_attribute('name'))
##            break

    driver.execute_script("window.scrollTo(0, 720)") 
    time.sleep(0.3)
    #Проверка, анализ журнала событий устройства
    X26_45 = driver.find_element_by_id('X26_45')
    X26_45.send_keys(Keys.CONTROL + "a")
    X26_45.send_keys(Keys.DELETE)
    X26_45.send_keys(work_time)
    print('Find X26_45!!!!!!')
    
    #Анализ/сохранение результатов выполнения команд диагностики    
    time.sleep(0.3)
    X26_46 = driver.find_element_by_id('X26_46')
    X26_46.send_keys(Keys.CONTROL + "a")
    X26_46.send_keys(Keys.DELETE)
    X26_46.send_keys(work_time)
    print('Find X26_46!!!!!!')

    #Выполнение аудита технической документации
    time.sleep(0.3)
    X26_52 = driver.find_element_by_id('X26_52')
    X26_52.send_keys(Keys.CONTROL + "a")
    X26_52.send_keys(Keys.DELETE)
    X26_52.send_keys(work_time)
    print('Find X26_52!!!!!!')

    driver.switch_to_default_content()


############################################Завершить списание button.click()#####################################
def End_WriteOff_Btn():
    try:
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.TAG_NAME, 'button')))
    except:
        print('Button(Завершить списание) didnt find or already visible')
    for i in driver.find_elements_by_tag_name('button'):
            print(i.text)
            if i.text == 'Завершить списание':
                i.click()
                break


############################################Выполнить button.click()#####################################
def Perform_Btn():
    find_b = False
    Count = 0
    driver.switch_to_default_content()
    while True:
        try:
            for i in driver.find_elements_by_tag_name('button'):
                print(i.text)
                if i.text == 'Выполнить':
                    find_b = True
                    break
            #WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.TAG_NAME, 'button')))
            #WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Инициатор')))
        except:
            print('Exception Rised, Button(Выполнить) didnt find or already visible, try again')
        if  Count > 10 :
            print('Button (Выполнить) didnt find, Count > 10')
            break
        elif find_b == True:
            i.click()
            print('Button (Выполнить) find and clicked')
            break                
        Count = Count  + 1 
        print (Count)
        time.sleep(0.5)
    #for i in driver.find_elements_by_tag_name('button'):
    #        print(i.text)
    #        if i.text == 'Выполнить':
    #            i.click()
    #            break


############################################Закрыть button.click()#####################################
def Close_Btn():
    find_b = False
    Count = 0
    driver.switch_to_default_content()
    while True:
        try:
            for i in driver.find_elements_by_tag_name('button'):
                print(i.text)
                if i.text == 'Закрыть':
                    find_b = True
                    break
        except:
            print('Exception Rised, Button(Закрыть) didnt find or already visible, try again')
        if  Count > 10 :
            print('Button (Закрыть) didnt find, Count > 10')
            break
        elif find_b == True:
            i.click()
            print('Button (Закрыть) find and clicked')
            break                
        Count = Count  + 1 
        print (Count)
        time.sleep(0.5)




    #try:
    #    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.TAG_NAME, 'button')))
    #except:
    #    print('Button didnt find or already visible')
    #driver.switch_to_default_content()
    
    #for i in driver.find_elements_by_tag_name('button'):
    #        print(i.text)
    #        if i.text == 'Закрыть':
    #            i.click()
    #            break



#########################################Трудозатраты hyperlink Click()##############################################
def Trud_Hyperlink():
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.TAG_NAME, 'iframe')))
    time.sleep(2)
    frames = driver.find_elements_by_tag_name('iframe')
    print(len(frames))
    for frame in frames:
        print(frame.size, frame.location, frame.get_attribute('name'))
        if (frame.get_attribute('name')) != '':
            print ('Switched to frame:', frame.get_attribute('name'))
            driver.switch_to_frame(frame.get_attribute('name'))
            break
    #time.sleep(1)
    text_hyperlink = driver.find_element_by_link_text('Выполнение регламентных работ на СПД - ОУ (О3.2.2.2) (СПД Выполнение регламентных работ (О3.2.2.2)-оу)')
    #text_hyperlink.click()
    #time.sleep(1)
    #text_hyperlink.click()
    text_hyperlink.send_keys(Keys.RETURN)
    
    
    print('Find!!!!!!')
    time.sleep(2)

###########################################Заполнение решения########################################################
def Solution_Fill():
    frames = driver.find_elements_by_tag_name('iframe')
    print(len(frames))
    for frame in frames:
        print(frame.size, frame.location, frame.get_attribute('name'))
        if (frame.get_attribute('name')) != '':
            print ('Switched to frame:', frame.get_attribute('name'))
            driver.switch_to_frame(frame.get_attribute('name'))
            break
    try:
        Text_Box = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'X35')))
    except:
        print ('Exception raised WebDriverWait')
    try:
        Text_Box = driver.find_element_by_id('X35')
    except:
        print ('Exception raised driver.find_elements_by_id')

    print(Text_Box.text)
    Text_Box.send_keys(Keys.CONTROL + "a")
    Text_Box.send_keys(Keys.DELETE)
    
    Text_Box.send_keys('Профилактическое обслуживание оборудования СПД на узле согласно графика ППР')
    driver.switch_to_default_content()


############################################Списать трудозатраты button.click()#####################################
def Spis_Trud_Btn():
    #WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.TAG_NAME, 'button')))
    
        for j in range(1,10):
            try:
                for i in driver.find_elements_by_tag_name('button'):
                        print(i.text)
                        if i.text == 'Списать трудозатраты':
                            i.click()
                            return
            except:
                print('Exception rised while try to find btn Списать тродозатраты ')
            time.sleep(0.5)
    
       

#####################################Процесс заполнить#########################################################

def Process_Fill():
    try:
        frames = driver.find_elements_by_tag_name('iframe')
        print(len(frames))
        for frame in frames:
            print(frame.size, frame.location, frame.get_attribute('name'))
            if (frame.get_attribute('name')) != '':
                print ('Switched to frame:', frame.get_attribute('name'))
                driver.switch_to_frame(frame.get_attribute('name'))
                break
        try:
            Proc_OD_Btn = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'X16')))
        except:
            print ('Exception raised WebDriverWait X11FillButton')
        try:
            Proc_OD_Btn = driver.find_element_by_id('X16')
        except:
            print ('Exception raised driver.find_elements_by_id X11FillButton')

        Proc_OD_Btn.send_keys(Keys.RETURN)
        time.sleep(3)

        try:
            HyperLnk = driver.find_element_by_link_text('СПД Выполнение регламентных работ (О3.2.2.2)')
        except:
            print ('Exception raised in Выполнение регламентных работ на СПД - ОУ (О3.2.2.2)')

        print ('enter press')
        print (HyperLnk.text)
        HyperLnk.click()
        #HyperLnk.send_keys(Keys.RETURN)
        time.sleep(3)
        

        try:
            HyperLnk = driver.find_element_by_link_text('Выполнение регламентных работ на СПД - ОУ (О3.2.2.2)')
        except:
            print ('Exception raised in Выполнение регламентных работ на СПД - ОУ (О3.2.2.2)')

        #HyperLnk.send_keys(Keys.RETURN)
        HyperLnk.click()
        
        #print(Text_Box.text)
        #Text_Box.send_keys(Keys.CONTROL + "a")
        #Text_Box.send_keys(Keys.DELETE)
        
        #Text_Box.send_keys('Профилактическое обслуживание оборудования СПД на узле согласно графика ППР')
        driver.switch_to_default_content()
    except:
        print('Maybe process already fill')
        driver.switch_to_default_content()



##########################################ФИО Заполнение################################################
def FIO_Fill():
    frames = driver.find_elements_by_tag_name('iframe')
    print(len(frames))
    for frame in frames:
        print(frame.size, frame.location, frame.get_attribute('name'))
        if (frame.get_attribute('name')) != '':
            print ('Switched to frame:', frame.get_attribute('name'))
            driver.switch_to_frame(frame.get_attribute('name'))
            break
    try:
        FIO_Field = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'X23')))
    except:
        print ('Exception raised WebDriverWait X23_Field')
    try:
        FIO_Field = driver.find_element_by_id('X23')
    except:
        print ('Exception raised driver.find_elements_by_id X23_Field')

    FIO_Field.send_keys(Keys.CONTROL + "a")
    FIO_Field.send_keys(Keys.DELETE)
    FIO_Field.send_keys('STANISLAV')
    FIO_Field.send_keys(Keys.RETURN)
    driver.switch_to_default_content()

#WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, 'button')))

#size = (driver.find_element_by_tag_name('iframe')).size();
#print(size)


frames = driver.find_elements_by_tag_name('iframe')
print(len(frames))
for frame in frames:
    print(frame.size, frame.location, frame.get_attribute('name'))





FIO_Fill()
Solution_Fill()
Process_Fill()
To_Work_Btn()
#time.sleep(2)
Spis_Trud_Btn()
Trud_Hyperlink()
HourMin_Fill()
End_WriteOff_Btn()
####time.sleep(2)
Perform_Btn()
####time.sleep(2)
Close_Btn()






#for i in driver.find_elements_by_tag_name('iframe'):
#        print(i.text)
#        print('find')
        #if i.text == 'Списать трудозатраты':
        #     i.click()
        #     break


##for i in driver.find_elements_by_tag_name('button'):
##        print(i.text)
##        if i.text == 'Списать трудозатраты':
##            i.click()
##            break


#login_btn = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'LoginBtn')))
#login_btn.click()
