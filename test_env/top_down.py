from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException as nse
from selenium.common.exceptions import TimeoutException as toe
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException as noclick


options = webdriver.ChromeOptions()

URL = 'https://www.instagram.com'
user_email = 'ryanchimichanga'
user_password = 'C0mputer1998'

# Register the driver

chrome_browser = webdriver.Chrome(executable_path='/Users/Imraj/Desktop/Drivers/chromedriver', options=options)
chrome_browser.get(URL)

time.sleep(2)

chrome_browser.find_element_by_xpath('//input[@class="_2hvTZ pexuQ zyHYP"]').send_keys(user_email)
chrome_browser.find_element_by_xpath('//input[@name="password"]').send_keys(user_password)
time.sleep(1)
chrome_browser.find_element_by_xpath('//button[@type="submit"]').click()

profile_page_button = WebDriverWait(chrome_browser, 25).until(EC.element_to_be_clickable((By.XPATH, '//span[@role="link"]')))
profile_page_button.click()

profile_button = WebDriverWait(chrome_browser, 25).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="-qQT3"]')))
profile_button.click()

scroll_time = 15

# click following and scroll down the list for 40 seconds 
liquorcoy_following_list = WebDriverWait(chrome_browser, scroll_time).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/ryanchimichanga/following/"]')))
liquorcoy_following_list.click()

print()
print('Scroll down following list for at most {} seconds!'.format(scroll_time))

# time.sleep(15) #break to scroll down to decent length
time.sleep(8)

# /html/body/div[5]/div/div/div[2]

# scroll_bar = WebDriverWait(chrome_browser, 5).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="isgrP"]')))
# scroll_bar.click()

for x in range(100):
   # this line of code below is what will make the page scroll down 
   scroll_bar = WebDriverWait(chrome_browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="isgrP"]')))
   scroll_bar.click()
   chrome_browser.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
   
   if x % 20 == 0:
      print(x)
   else:
      pass
      


print()
print('Beginning unfollowing sequence, do not click anywhere on instagram as the program may be interrupted.\nYou may switch to another tab if you like.')
print()
print('If you wish to stop the program, simply close the Instagram window.')

def unfollow_sequence():


        # select unfollow if confirmation appears and then go back to liquorcoy's following list 
   def select_confirm_unfollow(x):

      WebDriverWait(chrome_browser, x).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="aOOlW -Cab_   "]'))).click()

      #chrome_browser.find_element_by_xpath('//button[@class="aOOlW -Cab_   "]').click() #click red unfollow button for confirmation
      chrome_browser.back()
   
   # going back to liquorcoy's following list if subject is following liquorcoy(2 backs)
   def back_to_beginning(n):

      chrome_browser.back()
      time.sleep(1)
      chrome_browser.back()
      return helper(n+1)

         # for combining going back once, unfollowing, and if the subject has a private account
   def unfollow_with_back(n):

      # assuming that the following list is still open
      chrome_browser.back()
      time.sleep(2)

      # click_unfollow = chrome_browser.find_element_by_xpath('//button@class="_5f5mN    -fzfL     _6VtSN     yZn4P   "]').click()
      def helperrr():

         #clicks on unfollow button
         #unfollow_click_second = chrome_browser.find_element_by_xpath('//button[@class="sqdOP  L3NKy    _8A5w5    "]') #clicks on unfollow button
         # following_count = chrome_browser.find_element_by_xpath('//span[@class="g47SY"]').text()

        
            
         # # press unfollower button 
         # chrome_browser.find_element_by_xpath('//button[@class="_5f5mN    -fzfL     _6VtSN     yZn4P   "]').click()
         # try:
         #    # press unfollower button 
         #    chrome_browser.find_element_by_xpath('//button[@class="_5f5mN    -fzfL     _6VtSN     yZn4P   "]').click()
         # except noclick:
         #    # that means they are public account, and you have already unfollowed
         #    pass
         
         # this will be for those who have follower_count > 0
         try:
            chrome_browser.find_element_by_xpath('//button[@class="_5f5mN    -fzfL     _6VtSN     yZn4P   "]').click()
         except nse:
            chrome_browser.find_element_by_xpath('//button[@class="sqdOP  L3NKy    _8A5w5    "]').click()
      
         try: 
            chrome_browser.find_element_by_xpath('//button[@class="aOOlW -Cab_   "]').click()
         except nse:
            # means the person has already been unfollowed, and has a public account 
            pass
         
      helperrr()   
      time.sleep(1)
      print('Unfollowed')
      
      if ('Unfollow' in chrome_browser.page_source):
        select_confirm_unfollow(2)
      else: 
         chrome_browser.back() #go back to LiquorCoy's following list

      return helper(n+1)

   def helper(n): 

      #                                                              /html/body/div[5]/div/div/div[2]/ul/div/li[2]/div/div[2]/div[1]/div/div/span/a
      # click nth following                                          /html/body/div[5]/div/div/div[2]/ul/div/li[1]/div/div[2]/div[1]/div/div/span/a
      
      
      try:
         WebDriverWait(chrome_browser, 4).until(EC.element_to_be_clickable((By.XPATH, ('//div[@class="PZuss"]/li[{}]/div/div[1]/div[2]/div[1]/span/a').format(n)))).click()
      except toe:
         WebDriverWait(chrome_browser, 7).until(EC.element_to_be_clickable((By.XPATH, ('//div[@class="PZuss"]/li[{}]/div/div[2]/div[1]/div/div/span/a').format(n)))).click()

      try:
         # this code is to click following list
         WebDriverWait(chrome_browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//ul[@class="k9GMp "]/li[3]/a'))).click()
      except noclick:
         # click intercepted exception, meaning the person has 0 following
         unfollow_with_back(1)

      # see if user has liquorcoy in their following list, till the 7th person
      def it_is_liquorcoy(x):

         time.sleep(x)

         def foo(g):
            if (g == 8):
               unfollow_with_back(n)
            else:
               def checker(g):
                     
                  try:
                     name = WebDriverWait(chrome_browser, 3).until(EC.element_to_be_clickable((By.XPATH, ('//div[@class="PZuss"]/li[{}]/div/div[2]/div[1]/div/div/span/a').format(g)))).text
                  except toe:
                     unfollow_with_back(n)
                     print(n)
                     helper(n+1)

                  return back_to_beginning(n) if (name == 'ryanchimichanga') else foo(g+1)
               checker(g)
            
         return foo(1)

      it_is_liquorcoy(1)

   return helper(1)

unfollow_sequence()