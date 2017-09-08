# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 23:51:06 2017

@author: haris
"""

from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.support.select import Select;
from selenium.common.exceptions import NoSuchElementException;
import time;


# Data
email = "dumbo.cvbh@gmail.com";
password = "john1234";


howDidYouHear = {'Google': '0', 'Course Report': '1', 'Switchup': '2', 'SkilledUp': '3', 'Quora': '4', 'Facebook': '5', 'Meetup/Events': '6', 'Word of Mouth': '7', 'Partner': '8', 'Other': '9', 'DataAspirant': '10', 'Bhive': '11', 'Cowrks': '12', '91springboard': '13', 'Reddit': '14', 'Blog Post': '15'};

linkTitles = {'Choose Your Location', 'New York Application', 'Remote Application', 'Singapore Application', 'India Application', 'Upload Supporting Documents (Optional)'}

onSiteId = 'id_6aP4FoF0RJ_0_0';
remoteId = 'id_6aP4FoF0RJ_0_1';

newYorkOnsite = 'id_h1OyesBrlH_0_0';
singaporeOnsite = 'id_h1OyesBrlH_0_1';
indiaOnsite = 'id_h1OyesBrlH_0_2';

bootcampId = 'id_EKst40ZHuc_0_0';
minicourseId = 'id_EKst40ZHuc_0_1';

webdriver.f

#Initialize
driver = webdriver.Chrome("../Documents/chromedriver");
driver.get("https://byteacademy.fluidreview.com");

# Sign up
#driver.find_element_by_id("frontpage-sign-up").click();

# Sign In
driver.find_element_by_id("id_email").send_keys(email);
driver.find_element_by_id("id_password").send_keys(password);
driver.find_element_by_id("frontpage-sign-in").click();

# Delay Expected due to AJAX requests in the page
for i in range(1,11):
    try:
        x = driver.find_element_by_xpath("//div//a[@title='Choose Your Location']");
        break;
    except NoSuchElementException:
        time.sleep(1);

x.click();

# Fill the Location Form        
driver.find_element_by_xpath("//input[@title='First Name']").send_keys("Harish");
driver.find_element_by_xpath("//input[@title='Last Name']").send_keys("Rongala");
driver.find_element_by_xpath("//input[@title='Email']").send_keys("test@gmail.com");
driver.find_element_by_xpath("//input[@title='Phone Number']").send_keys("123456789");

# Conditional

# How did you hear about us
Select(driver.find_element_by_id("id_xwFvMdCxg3")).select_by_value('0');

# Conditional




# Onsite Radio
driver.find_element_by_id(onSiteId).click();



# Remote Radio
#driver.find_element_by_id(remoteId).click();



driver.find_element_by_name("submitbutton").click();


# Filling the Remote Application
# Delay Expected due to AJAX requests in the page
for i in range(1,11):
    try:
        x = driver.find_element_by_xpath("//div//a[@title='Remote Application']");
        break;
    except NoSuchElementException:
        time.sleep(1);
x.click();



#driver.find_element_by_id("frontpage-sign-up").click();
#driver.find_element_by_id("id_first_name").send_keys("Harish Test");
#driver.find_element_by_id("id_last_name").send_keys("Kumar Test");
#driver.find_element_by_id("id_email").send_keys("testing@gmail.com");
#driver.find_element_by_id("id_password").send_keys("iforgotit");
#driver.find_element_by_id("id_password2").send_keys("iforgotit");
#driver.find_element_by_name("field__20346").send_keys("123456789");
#driver.find_element_by_xpath("//input[@type='submit']").click();
