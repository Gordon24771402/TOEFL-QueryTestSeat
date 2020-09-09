# -*- coding: utf-8 -*-
"""
-----------------------
@Author    Hao Kang
@GitHub    Gordon24771402
-----------------------
Created on Tue Sep 8 08:18:30 2020
"""

from selenium import webdriver
from playsound import playsound
import time
import re

# Setup WebDriver
driver = webdriver.Firefox()

# TOEFL WebSite
driver.get('https://toefl.neea.cn/login')

# Manually Login (Verification Code)
while driver.current_url == 'https://toefl.neea.cn/login':
    time.sleep(1)

# City & TestDate
citiesList = ["DONGGUAN", "SHENZHEN", "GUANGZHOU"]
daysList = ["2020-09-26", "2020-09-27", "2020-10-10", "2020-10-14", "2020-10-17", "2020-10-24"]

# Check Seat
while True:
    time.sleep(5)
    driver.refresh()
    time.sleep(5)
    for i in range(5):
        for city in citiesList:
            for date in daysList:
                js = 'return $.ajax({url: "testSeat/queryTestSeats",type: "GET",data: {' + f'city: "{city}",testDay: "{date}"' + '},dataType: "text",async: false,}).responseText;'
                dataJSON = driver.execute_script(js)
                if "true" in dataJSON:
                    seatStatus = re.findall(r'<status>(\d+)</status>', dataJSON)
                    if '1' in seatStatus:
                        print('City: {} Date: {} Available'.format(city, date))
                        while True:
                            playsound('Alarm01.wav')
        time.sleep(60)
