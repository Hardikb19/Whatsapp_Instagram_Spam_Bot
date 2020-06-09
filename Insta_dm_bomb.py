from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import getpass


limit = 1 #Chnage limit if you want to spam


def autoSendMessage():
    #Input From User
    username = input("Enter Your Username (Eg: qwerty.123) :")
    print("Enter Username (Typed Password will not be displayed):")
    password = getpass.getpass()
    send_to_username = input("Enter reciever's Username (Eg: qwerty.123):")
    limit = int(input("Enter Number of Messages to send (1-1000): "))
    message = input("Enter Message to send: ")

    #Let it work its magic                
    usernames = [send_to_username] #add all usernames to list you want to send message to
    chrome_options = Options()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--remote-debugging-port=9222')
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
    browser = webdriver.Chrome("./chromedriver.exe", options=chrome_options)
    browser.get('https://www.instagram.com/accounts/login/')
    #Login
    time.sleep(2)
    username_bar = browser.find_element_by_name('username')
    password_bar = browser.find_element_by_name('password')    
    username_bar.send_keys(username)
    password_bar.send_keys(password + Keys.ENTER)
    time.sleep(5)
    def send_msg(user):
        #Open New Direct Message
        browser.get('https://www.instagram.com/direct/new/')
        time.sleep(1)
        #Search for User
        to_btn = browser.find_element_by_name('queryBox')
        to_btn.send_keys(user)

        time.sleep(1)
        #Select User
        chk_mrk = browser.find_element_by_class_name('dCJp8 ')
        chk_mrk.click()

        time.sleep(1)
    
        nxt_btn = browser.find_element_by_xpath('//div[@class="mXkkY KDuQp"]')
        nxt_btn.click()

        time.sleep(1)

        for _ in range(limit):
            time.sleep(1)
            #Type Text
            txt_box = browser.find_element_by_tag_name('textarea')
            txt_box.send_keys(message)  # Customize your message

            time.sleep(1)
            #Send
            snd_btn = browser.find_elements_by_tag_name('button')
            pos = len(snd_btn)-1
            snd_btnn = snd_btn.__getitem__(pos)
            snd_btnn.click()

        time.sleep(4)

    #Main Control to Send Message
    try:
        for usr in usernames:
            send_msg(usr)
    except TypeError:
        print('Failed!')
    #Close Browser
    browser.quit()

#Main Program
try:
    autoSendMessage()
except TypeError:
    pass
