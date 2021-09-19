#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 16:50:08 2021

@author: jesus
"""

from booking.booking import Booking


with Booking() as bot:
    bot.land_first_page()
    bot.change_currency( currency='EUR' )  
    bot.selected_place_to_go( 'Sevilla' )
    bot.select_dates(check_in  = '2021-09-20', 
                     check_out = '2021-09-27' )
    bot.select_adults( 2 )
    bot.click_search()
    bot.apply_filtrations()

