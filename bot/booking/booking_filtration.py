#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 11:37:05 2021



@author: jesus

"""

from selenium.webdriver.remote.webdriver import WebDriver


class BookingFiltration:
    
    def __init__( self, driver:WebDriver ):
        self.driver = driver
        
    "No aplica bien el filtrado"
    def apply_star_rating( self, *star_values ):
        father_element = self.driver.find_element_by_id( 'filter_class' )
        chield_elements = father_element.find_elements_by_css_selector('*')
        
        for star_value in star_values:
            if not self.is_valid_star_value( star_value ):
                continue
            for element in chield_elements:
                if str( element.get_attribute('innerHTML') ).strip() == f'{star_value} stars':  # Return tag element Ex: <h1>VIC</h1>  --> return VIC
                    element.click()    
        

    def is_valid_star_value( self, star_val:int ):
        if star_val > 5:
            return False
        if star_val <= 0:
            return False
        return True


