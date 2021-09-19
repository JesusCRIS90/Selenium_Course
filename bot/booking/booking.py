#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 16:50:08 2021

@author: jesus
"""

import booking.constants as const
from selenium import webdriver
from booking.booking_filtration import BookingFiltration


class Booking( webdriver.Chrome ):
    
    def __init__( self, driver_path = r'/home/jesus/SeleniumDrivers/chromedriver', teardown = False ):
        self.driver_path = driver_path
        self.teardown = teardown
        super(Booking, self).__init__( executable_path = self.driver_path )
        self.implicitly_wait( 15 )
        self.maximize_window()
        
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

        
    def land_first_page( self ):
        self.get( const.BASE_URL )


    def change_currency( self, currency = None ):
        currency_element = self.find_element_by_css_selector( 
            'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()
        
        selected_currency_element = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency_element.click()
        
        
    def selected_place_to_go( self, place_to_go ):
        search_field = self.find_element_by_id( 'ss' )
        search_field.clear()
        search_field.send_keys( place_to_go )
        
        first_result = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )
        first_result.click()
        
    def select_dates( self, check_in, check_out ):
        check_in_element = self.find_element_by_css_selector(
            f'td[data-date="{check_in}"]'
        )
        check_in_element.click()
        
        check_out_element = self.find_element_by_css_selector(
            f'td[data-date="{check_out}"]'
        )
        check_out_element.click()
        
    def select_adults( self, counts = 1 ):
        
        if counts > 30:
            counts = 30
        if counts <= 0:
            counts = 1
        
        field_element = self.find_element_by_id( 'xp__guests__toggle' )
        field_element.click()
        
        while True:
            
            current_adult_value = self.get_current_adults_selected()
            
            if current_adult_value < counts:
                self.increase_adults()
        
            if current_adult_value > counts:
                self.decrease_adults()
            
            if current_adult_value == counts:
                break
            
    
        
    def get_current_adults_selected( self ):
        adult_number_element = self.find_element_by_id( 'group_adults' )
        return int( adult_number_element.get_attribute( 'value' ) )
    
    
    def decrease_adults( self ):
        element = self.find_element_by_css_selector( 
            'button[aria-label="Decrease number of Adults"]'
        )
        element.click()
        
    def increase_adults( self ):
        element = self.find_element_by_css_selector( 
            'button[aria-label="Increase number of Adults"]'
        )
        element.click()
        
    def click_search( self ):
        element = self.find_element_by_css_selector( 
            'button[type="submit"]'    
        )
        element.click()
        
    def apply_filtrations( self ):
        filtration = BookingFiltration( driver = self )
        filtration.apply_star_rating( 5, 4, 3 )
        
        
        
