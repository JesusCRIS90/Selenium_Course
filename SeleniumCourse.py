#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 17:38:09 2021

Selenium: Web Scrapping Course

@author: jesus
"""

# import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


url_button_ex = "https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html"
url_Example_SendingKeys_AND_CCS_Selector = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"

path_chrome_driver = r'/home/jesus/SeleniumDrivers/chromedriver'

implicity_wait_global = 8

def Example_Buttons_CLicks( _url_ ):
    
    _driver_ = webdriver.Chrome( executable_path = path_chrome_driver )
    _driver_.get( _url_ )
    _driver_.implicitly_wait( implicity_wait_global )
    
    # Clicking buttons
    element_1 = _driver_.find_element_by_id( "downloadButton" )
    element_1.click()


    result = WebDriverWait( _driver_, 30 ).until(
                EC.text_to_be_present_in_element(
                    (By.CLASS_NAME, 'progress-label'),  # Element filtration
                    'Complete!'                         # The expected text
                    )
                )

    if result:
        element_1 = _driver_.find_element_by_class_name( "ui-dialog-buttonset" ).click()
        _driver_.close()


def Example_SendingKeys_AND_CCS_Selector( _url_ ):
    
    _driver_ = webdriver.Chrome( executable_path = path_chrome_driver )
    _driver_.get( _url_ )
    _driver_.implicitly_wait( implicity_wait_global )
    
    try:
        no_btn = _driver_.find_element_by_class_name('at-cm-no-button')
        no_btn.click()
    except:
        print( "No element with this class name. Skipping ...." )
        
    # Finding Elements
    element_1 = _driver_.find_element_by_id( "sum1" )
    element_2 = _driver_.find_element_by_id( "sum2" )
    btn = _driver_.find_element_by_css_selector( 'button[onclick="return total()"]' )
    
    element_1.send_keys( 10 )
    element_2.send_keys( 12 )
    
    btn.click()
    
    result = _driver_.find_element_by_id( "displayvalue" )
    value = result.get_property("displayvalue")
    print( value )
    
    


ptr_fun = Example_Buttons_CLicks

ptr_fun( url_button_ex )

# Example_Buttons_CLicks( url_button_ex )
# Example_SendingKeys_AND_CCS_Selector( url_Example_SendingKeys_AND_CCS_Selector )

